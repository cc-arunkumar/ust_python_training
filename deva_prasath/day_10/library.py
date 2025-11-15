import os
import csv
from datetime import datetime
from models import User, Book, Transaction
from storage import CSVStorage
from utils import get_today_str, add_days, generate_id
from models import (
    ValidationError, InvalidBookError, InvalidUserError,
    BookNotAvailableError, UserNotAllowedError, TransactionError
)

class Library:
    """
    Main business logic layer for the Library Management System.
    Handles all operations on books, users, and transactions.
    """

    def __init__(self):
        """Initialize library and load data from CSV files."""
        self.storage = CSVStorage()
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.transactions = self.storage.load_transactions()

        # Fast lookup sets
        self.book_ids = {b.book_id for b in self.books}
        self.isbns = {b.isbn for b in self.books if b.isbn}
        self.user_ids = {u.user_id for u in self.users}
        self.tx_ids = {t.tx_id for t in self.transactions}

    def save_all(self):
        """Save all data back to CSV files."""
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)


    def add_book(self, book_id: str, title: str, authors: list, isbn: str,
             tags: list, total_copies: int):
        
        if not book_id.strip():
            raise ValidationError("Book ID cannot be empty")
        if book_id in self.book_ids:
            raise InvalidBookError("Book ID already exists")
        if isbn and isbn in self.isbns:
            raise InvalidBookError("ISBN already exists")

        # Fixed: Use Book, not Books | authors, not author
        book = Book(
            book_id=book_id,
            title=title,
            authors=authors,
            isbn=isbn,
            tags=tags,
            total_copies=total_copies,
            available_copies=total_copies
        )
        self.books.append(book)
        self.book_ids.add(book_id)
        if isbn:
            self.isbns.add(isbn)

    def update_book(self, book_id: str, **kwargs):
        book = self.get_book(book_id)
        old_isbn = book.isbn

        if "isbn" in kwargs and kwargs["isbn"] != old_isbn:
            new_isbn = kwargs["isbn"]
            if new_isbn and new_isbn in self.isbns:
                raise InvalidBookError("ISBN already exists")

        for key, value in kwargs.items():
            if key == "total_copies":
                new_total = int(value)
                if new_total < book.available_copies:
                    raise ValidationError("Total copies cannot be less than available copies")
                book.total_copies = new_total
            elif key in ["authors", "tags"]:  # Fixed: authors
                if isinstance(value, str):
                    value = [v.strip() for v in value.split(",") if v.strip()]
                setattr(book, key, value)
            else:
                setattr(book, key, value)

        if "isbn" in kwargs:
            if old_isbn:
                self.isbns.discard(old_isbn)
            if kwargs["isbn"]:
                self.isbns.add(kwargs["isbn"])

    def remove_book(self, book_id: str):
        """Remove a book if no active loans exist."""
        book = self.get_book(book_id)
        active_loans = any(
            t.book_id == book_id and t.status == "borrowed"
            for t in self.transactions
        )
        if active_loans:
            raise InvalidBookError("Cannot remove book with active loans")

        self.books = [b for b in self.books if b.book_id != book_id]
        self.book_ids.remove(book_id)
        if book.isbn:
            self.isbns.discard(book.isbn)

    def get_book(self, book_id: str) -> Book:
        """Retrieve book by ID."""
        for b in self.books:
            if b.book_id == book_id:
                return b
        raise InvalidBookError("Book not found")

    def list_books(self):
        """Return all books."""
        return self.books

    def search_books(self, title=None, author=None, tag=None):
        """
        Search books by title substring, author name, or tag.
        Case-insensitive.
        """
        results = self.books

        if title:
            title_lower = title.lower()
            results = [b for b in results if title_lower in b.title.lower()]

        if author:
            author_lower = author.lower()
            results = [
                b for b in results
                if any(author_lower in a.lower() for a in b.author)
            ]

        if tag:
            tag_lower = tag.lower()
            results = [
                b for b in results
                if tag_lower in [t.lower() for t in b.tags]
            ]

        return results

    def add_user(self, user_id: str, name: str, email=None,
                 status="active", max_loans=5):
        """Add a new user."""
        if not user_id.strip():
            raise ValidationError("User ID cannot be empty")
        if user_id in self.user_ids:
            raise InvalidUserError("User ID already exists")

        user = User(user_id, name, email, status, max_loans)
        self.users.append(user)
        self.user_ids.add(user_id)

    def update_user(self, user_id: str, **kwargs):
        """Update user fields: name, email, max_loans."""
        user = self.get_user(user_id)
        for key, value in kwargs.items():
            if key == "max_loans":
                user.max_loans = int(value)
            elif key in ["name", "email"]:
                setattr(user, key, value)

    def get_user(self, user_id: str) -> User:
        """Retrieve user by ID."""
        for u in self.users:
            if u.user_id == user_id:
                return u
        raise InvalidUserError("User not found")

    def list_users(self):
        """Return all users."""
        return self.users

   

    def borrow_book(self, user_id: str, book_id: str) -> Transaction:
        """
        Borrow a book.
        Rules:
        - Book must exist and be available
        - User must exist, be active, and under max_loans
        - Due date = today + 14 days
        """
        user = self.get_user(user_id)
        book = self.get_book(book_id)

        if not book.is_available():
            raise BookNotAvailableError("No copies available")

        active_loans = sum(
            1 for t in self.transactions
            if t.user_id == user_id and t.status == "borrowed"
        )
        if not user.can_borrow(active_loans):
            raise UserNotAllowedError("User cannot borrow: inactive, banned, or max loans reached")

        today = get_today_str()
        due = add_days(today, 14)
        tx_id = generate_id("T", self.tx_ids)

        tx = Transaction(
            tx_id=tx_id,
            book_id=book_id,
            user_id=user_id,
            borrow_date=datetime.strptime(today, "%d-%m-%Y"),
            due_date=due
        )
        self.transactions.append(tx)
        self.tx_ids.add(tx_id)

        # Decrease available copies
        book.available_copies -= 1

        return tx

    def return_book(self, tx_id: str):
        """Return a borrowed book."""
        tx = None
        for t in self.transactions:
            if t.tx_id == tx_id:
                tx = t
                break
        if not tx:
            raise TransactionError("Transaction not found")

        if tx.status != "borrowed":
            raise TransactionError("Book already returned or overdue")

        today = get_today_str()
        tx.mark_returned(today)

        # Increase available copies
        book = self.get_book(tx.book_id)
        book.available_copies += 1


    def active_loans(self):
        """Return all borrowed (not returned) transactions."""
        return [t for t in self.transactions if t.status == "borrowed"]

    def overdue_loans(self):
        """Return borrowed transactions past due date."""
        today = get_today_str()
        return [
            t for t in self.active_loans()
            if t.is_overdue(today)
        ]

    def user_loan_history(self, user_id: str):
        """Return all transactions for a user."""
        return [t for t in self.transactions if t.user_id == user_id]

  
    def summary_report(self):
        """Generate system summary."""
        return {
            "total_books": len(self.books),
            "total_users": len(self.users),
            "active_loans": len(self.active_loans()),
            "overdue_loans": len(self.overdue_loans())
        }

    def user_history_report(self, user_id: str):
        """Generate detailed report for a user."""
        user = self.get_user(user_id)
        history = self.user_loan_history(user_id)
        today = get_today_str()
        overdue = [
            t for t in history
            if t.status == "borrowed" and t.is_overdue(today)
        ]
        return {
            "user": user,
            "transactions": history,
            "overdue": overdue
        }
        