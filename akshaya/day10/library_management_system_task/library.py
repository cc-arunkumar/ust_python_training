# library .py 
from datetime import datetime
import uuid
from akshaya.day10.library_management_system_task.models import Book, User, Transaction, InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError
from akshaya.day10.library_management_system_task.storage import CSVStorage
from akshaya.day10.library_management_system_task.utils import today_str, due_date_str

class Library:
    def __init__(self):
        self.storage = CSVStorage()
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.transactions = self.storage.load_transactions()

    # ---------------- BOOKS ----------------
    def add_book(self, book):
        if any(b.book_id == book.book_id for b in self.books):
            raise ValidationError("Duplicate Book ID.")
        if book.isbn and any(b.isbn == book.isbn for b in self.books if b.title != "DELETED"):
            raise ValidationError("Duplicate ISBN.")
        self.books.append(book)

    def update_book(self, book_id, **kw):
        book = self.get_book(book_id)
        if book.title == "DELETED":
            raise InvalidBookError("Book is deleted and cannot be updated.")
        return book.update(**kw)

    def remove_book(self, book_id):
        book = self.get_book(book_id)
        # Check if the book is already soft-deleted
        if book.is_removed:
            raise InvalidBookError("Book has already been removed (soft-deleted).")
        
        # If book has active borrowed txs, forbid deletion
        if any(tx.book_id == book_id and tx.status == "borrowed" for tx in self.transactions):
            raise BookNotAvailableError("Book has active loans and cannot be removed.")
        
        # Soft delete: set title to 'DELETED', available_copies 0, clear tags/authors/isbn
        book.soft_delete()
        return book

    def get_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        raise InvalidBookError("Book not found.")

    def list_books(self, include_deleted=False):
        if include_deleted:
            return self.books
        return [b for b in self.books if not b.is_removed]

    def search_books(self, title_substr=None, author=None, tag=None):
        results = [b for b in self.books if b.title != "DELETED"]
        if title_substr:
            results = [b for b in results if title_substr.lower() in b.title.lower()]
        if author:
            results = [b for b in results if any(author.lower() in a.lower() for a in b.authors)]
        if tag:
            results = [b for b in results if any(tag.lower() in t.lower() for t in b.tags)]
        return results

    # ---------------- USERS ----------------
    def add_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            raise ValidationError("Duplicate User ID.")

        # If max_loans is 0, set it to 1
        if user.max_loans == 0:
            user.max_loans = 1
        
        self.users.append(user)

    def update_user(self, user_id, **kw):
        user = self.get_user(user_id)
        return user.update(**kw)

    def get_user(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        raise InvalidUserError("User not found.")

    def list_users(self):
        return self.users

    def set_user_status(self, user_id, status):
        user = self.get_user(user_id)
        if status == "activate":
            user.activate()
        elif status == "deactivate":
            user.deactivate()
        elif status == "ban":
            user.ban()
        else:
            raise ValidationError("Unknown status.")
        return user

    # ---------------- BORROW ----------------
    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        # Ensure that the book is not deleted and available
        if book.title == "DELETED":
            raise BookNotAvailableError("Book not available (deleted).")
        
        # Ensure book is available for borrowing
        if not book.is_available():
            raise BookNotAvailableError("Book not available for borrowing.")  # Ensure it handles returned books

        active_loans = sum(1 for tx in self.transactions if tx.user_id == user_id and tx.status == "borrowed")
        user.can_borrow(active_loans)

        tx_id = f"T{len(self.transactions) + 1}"
        borrow_date = today_str()
        due = due_date_str(14)

        tx = Transaction(tx_id, book_id, user_id, borrow_date, due)
        self.transactions.append(tx)
        
        # Decrease the book's available copies when borrowed
        book.decrease_copies(1)
        return tx

    # ---------------- RETURN ----------------
    def return_book(self, tx_id):
        tx = next((t for t in self.transactions if t.tx_id == tx_id), None)
        if not tx:
            raise TransactionError("Transaction not found.")
        if tx.status != "borrowed":
            raise TransactionError("This transaction is already returned or overdue.")  # Ensure only borrowed can be returned
        
        tx.mark_returned(today_str())
        book = self.get_book(tx.book_id)
        
        # Increase the book's available copies when returned
        if book.title != "DELETED":
            book.increase_copies(1)

        # Save data after returning the book
        self.save_all()  # Ensure changes are saved to the CSV file
        return tx

    # ---------------- REPORTS ----------------
    def report_summary(self):
        total_books = len([b for b in self.books if b.title != "DELETED"])
        total_users = len(self.users)
        active_loans = sum(1 for tx in self.transactions if tx.status == "borrowed")
        overdue_loans = sum(1 for tx in self.transactions if tx.status == "borrowed" and tx.is_overdue(today_str()))
        return {
            "Total books": total_books,
            "Total users": total_users,
            "Active loans": active_loans,
            "Overdue loans": overdue_loans
        }

    def report_user(self, user_id):
        self.get_user(user_id)  # validate exists
        return [tx for tx in self.transactions if tx.user_id == user_id]

    # ---------------- SAVE ----------------
    def save_all(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)

    # ---------------- LOANS ----------------
    def loans_active(self):
        return [tx for tx in self.transactions if tx.status == "borrowed"]

    def loans_overdue(self):
        today = today_str()
        return [tx for tx in self.transactions if tx.status == "borrowed" and tx.is_overdue(today)]

    def loans_user(self, user_id):
        return [tx for tx in self.transactions if tx.user_id == user_id]
