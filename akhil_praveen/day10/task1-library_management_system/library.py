# library.py
from models import (
    Book, User, Transaction,
    InvalidBookError, InvalidUserError,
    BookNotAvailableError, UserNotAllowedError,
    TransactionError, ValidationError
)
from utils import today, due_after_14_days, generate_id
from storage import CSVStorage


class Library:
    def __init__(self):
        self.storage = CSVStorage()

        # Load all data into memory
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.transactions = self.storage.load_transactions()

    # ============================================================
    #                         BOOKS
    # ============================================================

    def add_book(self, data):
        # unique ID validation
        if any(b.book_id == data["book_id"] for b in self.books):
            raise InvalidBookError("Book ID already exists")

        # unique ISBN validation
        if any(b.isbn == data["isbn"] for b in self.books):
            raise ValidationError("ISBN already exists")

        # create book object
        new_book = Book(**data)

        # update memory
        self.books.append(new_book)

        # append to CSV (NO overwrite)
        self.storage.append_book(new_book)

        return new_book

    def get_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        raise InvalidBookError("Book not found")

    def update_book(self, book_id, updates):
        book = self.get_book(book_id)
        book.update(**updates)

        # rewrite entire CSV to reflect update
        self.storage.save_books(self.books)

        return book

    def remove_book(self, book_id):
        book = self.get_book(book_id)

        # check active loans
        for tx in self.transactions:
            if tx.book_id == book_id and tx.status == "borrowed":
                raise ValidationError("Cannot remove: active loans exist")

        self.books = [b for b in self.books if b.book_id != book_id]

        # rewrite CSV
        self.storage.save_books(self.books)

    def list_books(self):
        return self.books

    # ============================================================
    #                         USERS
    # ============================================================

    def add_user(self, data):
        if any(u.user_id == data["user_id"] for u in self.users):
            raise InvalidUserError("User ID already exists")

        new_user = User(**data)
        self.users.append(new_user)

        # append new user only
        self.storage.append_user(new_user)

        return new_user

    def get_user(self, user_id):
        for u in self.users:
            if u.user_id == user_id:
                return u
        raise InvalidUserError("User not found")

    def update_user(self, user_id, updates):
        user = self.get_user(user_id)

        for key, value in updates.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)

        # save entire CSV after update
        self.storage.save_users(self.users)

        return user

    def list_users(self):
        return self.users

    # ============================================================
    #                    BORROW & RETURN
    # ============================================================

    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        # check borrowing rules
        active_loans = self._active_loans_count(user_id)

        if not user.can_borrow(active_loans):
            raise UserNotAllowedError("User not allowed to borrow")

        if not book.is_available():
            raise BookNotAvailableError("Book not available")

        # generate transaction ID
        tx_id = generate_id("T", self.transactions)

        new_tx = Transaction(
            tx_id=tx_id,
            book_id=book_id,
            user_id=user_id,
            borrow_date=today(),
            due_date=due_after_14_days(),
            return_date=None,
            status="borrowed"
        )

        # update memory
        self.transactions.append(new_tx)
        book.available_copies -= 1

        # update book CSV and append transaction CSV
        self.storage.save_books(self.books)
        self.storage.append_transaction(new_tx)

        return new_tx

    def return_book(self, tx_id):
        tx = self._get_transaction(tx_id)
        book = self.get_book(tx.book_id)

        if tx.status != "borrowed":
            raise TransactionError("Book already returned")

        tx.mark_returned(today())
        book.available_copies += 1

        # save updated CSVs
        self.storage.save_books(self.books)
        self.storage.save_transactions(self.transactions)

        return tx

    # ============================================================
    #                        SEARCH
    # ============================================================

    def search_books(self, title=None, author=None, tag=None):
        result = self.books

        if title:
            result = [b for b in result if title.lower() in b.title.lower()]

        if author:
            result = [
                b for b in result
                if any(author.lower() in a.lower() for a in b.authors)
            ]

        if tag:
            result = [
                b for b in result
                if any(tag.lower() in t.lower() for t in b.tags)
            ]

        return result

    # ============================================================
    #                        REPORTS
    # ============================================================

    def report_summary(self):
        return {
            "total_books": len(self.books),
            "total_users": len(self.users),
            "active_loans": len([t for t in self.transactions if t.status == "borrowed"]),
            "overdue_loans": len([
                t for t in self.transactions
                if t.status == "borrowed" and t.is_overdue(today())
            ])
        }

    def user_history(self, user_id):
        self.get_user(user_id)  # validate

        return [t for t in self.transactions if t.user_id == user_id]

    # ============================================================
    #                    INTERNAL HELPERS
    # ============================================================

    def _active_loans_count(self, user_id):
        return sum(
            1 for t in self.transactions
            if t.user_id == user_id and t.status == "borrowed"
        )

    def _get_transaction(self, tx_id):
        for t in self.transactions:
            if t.tx_id == tx_id:
                return t
        raise TransactionError("Invalid transaction ID")

    # ============================================================
    #                        SAVE ALL
    # ============================================================

    def save_all(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)
