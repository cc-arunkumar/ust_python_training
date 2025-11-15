# storage.py
import os
import csv
from typing import List
from models import Book, User, Transaction
from models import ValidationError

DATA_DIR = "data"

# CRITICAL: Create directory BEFORE defining file paths
os.makedirs(DATA_DIR, exist_ok=True)

# Now safe to define paths
BOOKS_FILE = os.path.join(DATA_DIR, "books.csv")
USERS_FILE = os.path.join(DATA_DIR, "users.csv")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.csv")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)


class CSVStorage:
    """
    Handles all CSV-based persistence.
    - Creates files with headers if missing
    - Loads malformed rows gracefully
    - Overwrites entire file on save
    - Uses | as delimiter for list fields
    """

    # ================================
    # BOOKS
    # ================================
    @staticmethod
    def _ensure_books_file():
        """Create books.csv with header if not exists."""
        if not os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "book_id", "title", "authors", "isbn", "tags",
                    "total_copies", "available_copies"
                ])

    @staticmethod
    def load_books() -> List[Book]:
        """Load all books from CSV. Skip malformed rows."""
        CSVStorage._ensure_books_file()
        books = []
        with open(BOOKS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Parse pipe-separated lists
                    authors = [a.strip() for a in row["authors"].split("|") if a.strip()]
                    tags = [t.strip() for t in row["tags"].split("|") if t.strip()]

                    book = Book(
                        book_id=row["book_id"],
                        title=row["title"],
                        authors=authors,
                        isbn=row["isbn"],
                        tags=tags,
                        total_copies=int(row["total_copies"]),
                        available_copies=int(row["available_copies"])
                    )
                    books.append(book)
                except (KeyError, ValueError, ValidationError):
                    # Skip corrupted row but continue
                    continue
        return books

    @staticmethod
    def save_books(books: List[Book]):
        """Overwrite books.csv with current book list."""
        with open(BOOKS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "book_id", "title", "authors", "isbn", "tags",
                "total_copies", "available_copies"
            ])
            writer.writeheader()
            for book in books:
                data = book.to_dict()
                # Convert lists to |-separated strings
                data["authors"] = "|".join(data["authors"])
                data["tags"] = "|".join(data["tags"])
                writer.writerow(data)

    # ================================
    # USERS
    # ================================
    @staticmethod
    def _ensure_users_file():
        """Create users.csv with header if not exists."""
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["user_id", "name", "email", "status", "max_loans"])

    @staticmethod
    def load_users() -> List[User]:
        """Load all users from CSV."""
        CSVStorage._ensure_users_file()
        users = []
        with open(USERS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    email = row["email"] if row["email"] else None
                    user = User(
                        user_id=row["user_id"],
                        name=row["name"],
                        email=email,
                        status=row["status"],
                        max_loans=int(row["max_loans"])
                    )
                    users.append(user)
                except (KeyError, ValueError, ValidationError):
                    continue
        return users

    @staticmethod
    def save_users(users: List[User]):
        """Overwrite users.csv."""
        with open(USERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "user_id", "name", "email", "status", "max_loans"
            ])
            writer.writeheader()
            for user in users:
                data = user.to_dict()
                data["email"] = data["email"] or ""
                writer.writerow(data)

    # ================================
    # TRANSACTIONS
    # ================================
    @staticmethod
    def _ensure_transactions_file():
        """Create transactions.csv with header if not exists."""
        if not os.path.exists(TRANSACTIONS_FILE):
            with open(TRANSACTIONS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "tx_id", "book_id", "user_id", "borrow_date",
                    "due_date", "return_date", "status"
                ])

    @staticmethod
    def load_transactions() -> List[Transaction]:
        """Load all transactions from CSV."""
        CSVStorage._ensure_transactions_file()
        transactions = []
        with open(TRANSACTIONS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    borrow_date = row["borrow_date"]
                    return_date_str = row["return_date"] if row["return_date"] else None

                    tx = Transaction.from_dict({
                        "tx_id": row["tx_id"],
                        "book_id": row["book_id"],
                        "user_id": row["user_id"],
                        "borrow_date": borrow_date,
                        "due_date": row["due_date"],
                        "return_date": return_date_str,
                        "status": row["status"]
                    })
                    transactions.append(tx)
                except (KeyError, ValueError, ValidationError):
                    continue
        return transactions

    @staticmethod
    def save_transactions(transactions: List[Transaction]):
        """Overwrite transactions.csv."""
        with open(TRANSACTIONS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "tx_id", "book_id", "user_id", "borrow_date",
                "due_date", "return_date", "status"
            ])
            writer.writeheader()
            for tx in transactions:
                writer.writerow(tx.to_dict())