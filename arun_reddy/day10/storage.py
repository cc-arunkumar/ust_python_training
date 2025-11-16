import csv
from models import Book, User, Transaction
import os
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent
# Create full path to data folder
DATA_PATH = SCRIPT_DIR / "data"

# Ensure data directory exists, create if it doesn't
DATA_PATH.mkdir(exist_ok=True)

class CSVStorage:
    """
    This class handles all file operations for the Library Management System.
    It saves and loads books, users, and transactions from CSV files.
    """

    def load_books(self):
        """
        Load all books from the books.csv file.
        If file doesn't exist, create it automatically.
        Returns: A list of Book objects
        """
        books = []
        try:
            # Build full path to books.csv file
            books_file = DATA_PATH / "books.csv"
            # Open CSV in UTF-8 to support special characters
            with open(books_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        book = Book(
                            row.get("book_id", ""),
                            row.get("title", ""),
                            row.get("authors", "").split("|"),
                            row.get("isbn", ""),
                            row.get("tags", "").split("|"),
                            int(row.get("total_copies", 0))
                        )
                        book.available_copies = int(row.get("available_copies", 0))
                        books.append(book)
                    except Exception as e:
                        print(f"Skipping malformed row: {row} — {e}")
        except FileNotFoundError:
            # If file doesn't exist, create it with headers
            books_file = DATA_PATH / "books.csv"
            with open(books_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
                writer.writeheader()
        return books

    def save_books(self, books):
        """
        Save all books to books.csv file.
        Each book is saved as one row in the file.
        
        Args:
            books: A list of Book objects to save
        """
        books_file = DATA_PATH / "books.csv"
        # Use UTF-8 to preserve special characters on all computers
        with open(books_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
            writer.writeheader()
            for book in books:
                # Write each book as one row in the CSV
                # Authors and tags are converted from list to string (separated by |)
                writer.writerow({
                    "book_id": book.book_id,
                    "title": book.title,
                    "authors": "|".join(book.authors),  # Convert authors list to a string
                    "isbn": book.isbn,
                    "tags": "|".join(book.tags),  # Convert tags list to a string
                    "total_copies": book.total_copies,
                    "available_copies": book.available_copies
                })

    def load_users(self):
        """
        Load all users from users.csv file.
        If file doesn't exist, create it automatically.
        Returns: A list of User objects
        """
        users = []
        try:
            users_file = DATA_PATH / "users.csv"
            # Open CSV file with UTF-8 encoding
            with open(users_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        row["user_id"],
                        row["name"],
                        row["email"],
                        row["status"],
                        int(row["max_loans"])  # Convert max_loans to integer
                    )
                    users.append(user)
        except FileNotFoundError:
            # If file does not exist, create it with headers
            users_file = DATA_PATH / "users.csv"
            with open(users_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["user_id", "name", "email", "status", "max_loans"])
                writer.writeheader()
        return users

    def save_users(self, users):
        """
        Save all users to users.csv file.
        Each user is saved as one row in the file.
        
        Args:
            users: A list of User objects to save
        """
        users_file = DATA_PATH / "users.csv"
        # Write users using UTF-8 encoding
        with open(users_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["user_id", "name", "email", "status", "max_loans"])
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "user_id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "status": user.status,
                    "max_loans": user.max_loans
                })

    def load_transactions(self):
        """
        Load all transactions from transactions.csv file.
        If file doesn't exist, create it automatically.
        Returns: A list of Transaction objects
        """
        transactions = []
        try:
            transactions_file = DATA_PATH / "transactions.csv"
            # Open CSV file with UTF-8 encoding
            with open(transactions_file, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transaction = Transaction(
                        row["tx_id"],
                        row["book_id"],
                        row["user_id"],
                        row["borrow_date"],
                        row["due_date"],
                        row["return_date"] if row["return_date"] else None,
                        row["status"]
                    )
                    transactions.append(transaction)
        except FileNotFoundError:
            # If file does not exist, create it with headers
            transactions_file = DATA_PATH / "transactions.csv"
            with open(transactions_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])
                writer.writeheader()
        return transactions

    def save_transactions(self, transactions):
        """
        Save all transactions to transactions.csv file.
        Each transaction is saved as one row in the file.
        
        Args:
            transactions: A list of Transaction objects to save
        """
        transactions_file = DATA_PATH / "transactions.csv"
        with open(transactions_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])
            writer.writeheader()
            for transaction in transactions:
                writer.writerow({
                    "tx_id": transaction.tx_id,
                    "book_id": transaction.book_id,
                    "user_id": transaction.user_id,
                    "borrow_date": transaction.borrow_date,
                    "due_date": transaction.due_date,
                    "return_date": transaction.return_date if transaction.return_date else '',
                    "status": transaction.status
                })

    # -----------------
    # Data sanitation helpers
    # -----------------
    def sanitize_books(self, keep='first'):
        """Remove duplicate or malformed book records and rewrite CSV.
        keep: 'first' (default) keeps first seen ID, 'last' keeps last.
        Returns (removed_count, total)
        """
        books = self.load_books()
        seen = {}
        cleaned = []
        removed = 0
        for b in books:
            # Skip empty titles or non-positive total_copies
            try:
                if not b.title or str(b.title).strip() == '':
                    removed += 1
                    continue
                if int(b.total_copies) <= 0:
                    removed += 1
                    continue
            except Exception:
                removed += 1
                continue
            if b.book_id in seen:
                removed += 1
                if keep == 'last':
                    # replace previous
                    idx = seen[b.book_id]
                    cleaned[idx] = b
                # else keep first -> do nothing
            else:
                seen[b.book_id] = len(cleaned)
                cleaned.append(b)
        self.save_books(cleaned)
        return removed, len(cleaned)

    def sanitize_users(self, keep='first'):
        """Remove duplicate or malformed user records and rewrite CSV.
        Enforces email ending with @ust.com and positive max_loans.
        Returns (removed_count, total)
        """
        users = self.load_users()
        seen = {}
        cleaned = []
        removed = 0
        for u in users:
            try:
                if not u.user_id or not u.name:
                    removed += 1
                    continue
                if not isinstance(u.max_loans, int) or u.max_loans <= 0:
                    removed += 1
                    continue
                if not str(u.email).endswith('@ust.com'):
                    removed += 1
                    continue
            except Exception:
                removed += 1
                continue
            if u.user_id in seen:
                removed += 1
                if keep == 'last':
                    idx = seen[u.user_id]
                    cleaned[idx] = u
            else:
                seen[u.user_id] = len(cleaned)
                cleaned.append(u)
        self.save_users(cleaned)
        return removed, len(cleaned)
