# library.py
# Business logic layer: handles rules, validations, and operations for Books, Users, and Transactions.

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
        # Initialize storage and load existing data from CSV files
        self.storage = CSVStorage()
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.transactions = self.storage.load_transactions()

    # ---------------- BOOKS ----------------
    def add_book(self, book: Book):
        """
        Add a new book to the library.
        Validates uniqueness of book_id and ISBN.
        """
        if any(b.book_id == book.book_id for b in self.books):
            raise ValidationError("Duplicate Book ID not allowed.")
        if book.isbn and any(b.isbn == book.isbn for b in self.books):
            raise ValidationError("Duplicate ISBN not allowed.")
        self.books.append(book)

    def update_book(self, book_id, **kwargs):
        """
        Update details of an existing book.
        Raises InvalidBookError if book not found.
        """
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            raise InvalidBookError("Book not found.")
        book.update(**kwargs)
        return book

    def remove_book(self, book_id):
        """
        Remove a book from the library.
        Cannot remove if the book has active loans.
        """
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            raise InvalidBookError("Book not found.")
        if any(tx.book_id == book_id and tx.status == "borrowed" for tx in self.transactions):
            raise BookNotAvailableError("Cannot remove book with active loans.")
        self.books.remove(book)

    def get_book(self, book_id):
        """
        Retrieve a book by its ID.
        Raises InvalidBookError if not found.
        """
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            raise InvalidBookError("Book not found.")
        return book

    def list_books(self):
        """Return a list of all books in the library."""
        return self.books

    # ---------------- USERS ----------------
    def add_user(self, user: User):
        """
        Add a new user to the library.
        Validates uniqueness of user_id.
        """
        if any(u.user_id == user.user_id for u in self.users):
            raise ValidationError("Duplicate User ID not allowed.")
        self.users.append(user)

    def update_user(self, user_id, **kwargs):
        """
        Update details of an existing user.
        Raises InvalidUserError if user not found.
        """
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            raise InvalidUserError("User not found.")
        user = user.update(**kwargs)
        return user

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.
        Raises InvalidUserError if not found.
        """
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            raise InvalidUserError("User not found.")
        return user

    def list_users(self):
        """Return a list of all users in the library."""
        return self.users

    def set_user_status(self, user_id, status):
        """
        Change a user's status (activate, deactivate, ban).
        Raises ValidationError if status is invalid.
        """
        user = self.get_user(user_id)
        if status == "activate":
            user.activate()
        elif status == "deactivate":
            user.deactivate()
        elif status == "ban":
            user.ban()
        else:
            raise ValidationError("Invalid status operation.")
        return user

    # ---------------- BORROW ----------------
    def borrow_book(self, user_id, book_id):
        """
        Borrow a book for a user.
        Validates:
          - User exists and is active
          - Book exists and is available
          - User has not exceeded max loans
        Creates a new transaction and decreases available copies.
        """
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if not book.is_available():
            raise BookNotAvailableError("Book not available.")
        active_loans = sum(1 for tx in self.transactions if tx.user_id == user_id and tx.status == "borrowed")
        user.can_borrow(active_loans)  # raises UserNotAllowedError if invalid

        # Generate transaction ID (simple incremental scheme)
        tx_id = f"T{len(self.transactions)+1}"
        borrow_date = today_str()
        due_date = due_date_str(14)
        tx = Transaction(tx_id, book_id, user_id, borrow_date, due_date, None, "borrowed")
        self.transactions.append(tx)
        book.decrease_copies(1)
        return tx

    # ---------------- RETURN ----------------
    def return_book(self, tx_id):
        """
        Return a borrowed book.
        Validates transaction exists and is borrowed.
        Marks transaction as returned and increases available copies.
        """
        tx = next((t for t in self.transactions if t.tx_id == tx_id), None)
        if not tx:
            raise TransactionError("Transaction not found.")
        tx.mark_returned(today_str())
        book = self.get_book(tx.book_id)
        book.increase_copies(1)
        return tx

    # ---------------- REPORTS ----------------
    def report_summary(self):
        """
        Generate a summary report:
          - Total books
          - Total users
          - Active loans
          - Overdue loans
        """
        return {
            "Total books": len(self.books),
            "Total users": len(self.users),
            "Active loans": sum(1 for tx in self.transactions if tx.status == "borrowed"),
            "Overdue loans": sum(1 for tx in self.transactions if tx.is_overdue(today_str()))
        }

    def report_user(self, user_id):
        """
        Generate a report of all transactions for a given user.
        Raises InvalidUserError if user not found.
        """
        user = self.get_user(user_id)
        txs = [tx for tx in self.transactions if tx.user_id == user_id]
        return txs

    # ---------------- SAVE ----------------
    def save_all(self):
        """
        Save all books, users, and transactions back to CSV files.
        Ensures persistence across program runs.
        """
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)
