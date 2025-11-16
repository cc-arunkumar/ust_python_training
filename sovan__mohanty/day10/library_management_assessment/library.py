from models import (
    Book, User, Transaction,
    InvalidBookError, InvalidUserError,
    BookNotAvailableError, UserNotAllowedError,
    TransactionError, ValidationError
)
from storage import CSVStorage
from utils import today_str, due_date_str

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
        if book.isbn and any(b.isbn == book.isbn for b in self.books):
            raise ValidationError("Duplicate ISBN.")
        self.books.append(book)

    def update_book(self, book_id, **kw):
        book = self.get_book(book_id)
        return book.update(**kw)

    def remove_book(self, book_id):
        book = self.get_book(book_id)
        if any(tx.book_id == book_id and tx.status == "borrowed" for tx in self.transactions):
            raise BookNotAvailableError("Book has active loans.")
        self.books.remove(book)

    def get_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        raise InvalidBookError("Book not found.")

    def list_books(self):
        return self.books

    # SEARCH FEATURE
    def search_books(self, title_substr=None, author=None, tag=None):
        results = self.books
        if title_substr:
            results = [b for b in results if title_substr.lower() in b.title.lower()]
        if author:
            results = [b for b in results if author.lower() in (", ".join(b.authors)).lower()]
        if tag:
            results = [b for b in results if tag.lower() in (", ".join(b.tags)).lower()]
        return results

    # ---------------- USERS ----------------
    def add_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            raise ValidationError("Duplicate User ID.")
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
            raise ValidationError("Bad status.")
        return user

    # ---------------- BORROW ----------------
    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if not book.is_available():
            raise BookNotAvailableError("Book not available.")

        active_loans = sum(1 for tx in self.transactions if tx.user_id == user_id and tx.status == "borrowed")
        user.can_borrow(active_loans)

        tx_id = f"T{len(self.transactions) + 1}"
        borrow_date = today_str()
        due_date = due_date_str(14)

        tx = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
        self.transactions.append(tx)

        book.decrease_copies(1)
        return tx

    # ---------------- RETURN ----------------
    def return_book(self, tx_id):
        tx = None
        for t in self.transactions:
            if t.tx_id == tx_id:
                tx = t
                break
        if not tx:
            raise TransactionError("Transaction not found.")
        tx.mark_returned(today_str())
        book = self.get_book(tx.book_id)
        book.increase_copies(1)
        return tx

    # ---------------- REPORTS ----------------
    def report_summary(self):
        return {
            "Total books": len(self.books),
            "Total users": len(self.users),
            "Active loans": sum(1 for tx in self.transactions if tx.status == "borrowed"),
            "Overdue loans": sum(1 for tx in self.transactions if tx.is_overdue(today_str()))
        }

    def report_user(self, user_id):
        self.get_user(user_id)  # ensure exists
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
