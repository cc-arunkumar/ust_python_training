# storage.py
import os
import csv
from models import Book, User, Transaction

# Simple CSV-based storage system for books, users, and transactions.
#     Provides methods to load and save objects as CSV rows.
class CSVStorage:
    

    def __init__(self, books_path="data/books.csv", users_path="data/users.csv", transactions_path="data/transactions.csv"):
        # Determine the base directory of the current file
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(BASE_DIR, "data")
        os.makedirs(data_dir, exist_ok=True)  # Ensure 'data' directory exists

        # Allow relative paths or absolute paths for CSV files
        self.books_path = os.path.join(BASE_DIR, books_path) if not os.path.isabs(books_path) else books_path
        self.users_path = os.path.join(BASE_DIR, users_path) if not os.path.isabs(users_path) else users_path
        self.transactions_path = os.path.join(BASE_DIR, transactions_path) if not os.path.isabs(transactions_path) else transactions_path

        # Ensure CSV files exist with proper headers
        self._ensure_file(self.books_path, ["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
        self._ensure_file(self.users_path, ["user_id", "name", "email", "status", "max_loans"])
        self._ensure_file(self.transactions_path, ["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])

    # Ensure that the CSV file exists. If not, create it and write headers.
    def _ensure_file(self, path, headers):
        
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(headers)

    def _load_generic(self, path, cls, int_fields=None, list_fields=None, optional_fields=None):
        int_fields = int_fields or []
        list_fields = list_fields or []
        optional_fields = optional_fields or []

        items = []
        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        # Convert field types
                        for fld in int_fields:
                            row[fld] = int(row[fld]) if row[fld] != "" else 0
                        for fld in list_fields:
                            row[fld] = row[fld].split("|") if row[fld] else []
                        for fld in optional_fields:
                            row[fld] = row[fld] if row.get(fld) else None

                        items.append(cls(**row)) 
                    except Exception as e:

                        # Skip invalid rows but continue
                        print(f"[storage] Skipping invalid row in {path}: {row} ({e})")

        # If file doesn't exist, return empty list
        except FileNotFoundError:
            pass  
        return items

    # Public loading methods for each entity
    def load_books(self):
        
        return self._load_generic(
            self.books_path,
            Book,
            int_fields=["total_copies", "available_copies"],
            list_fields=["authors", "tags"]
        )
    
    #Load all users from CSV and return as a list of User instances.
    def load_users(self):
        
        return self._load_generic(
            self.users_path,
            User,
            int_fields=["max_loans"]
        )

    # Load all transactions from CSV and return as a list of Transaction instances.
    def load_transactions(self):
        
        return self._load_generic(
            self.transactions_path,
            Transaction,
            optional_fields=["return_date"]
        )

    # Generic method to save a list of objects to a CSV file.
    def _save_generic(self, path, items, fieldnames, list_fields=None):
        
        list_fields = list_fields or []
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for it in items:
                data = it.to_dict()
                for fld in list_fields:
                    if isinstance(data.get(fld), list):
                        data[fld] = "|".join(data[fld])
                writer.writerow(data)

    # Public saving methods for each entity
    def save_books(self, books):
        
        self._save_generic(
            self.books_path,
            books,
            ["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"],
            list_fields=["authors", "tags"]
        )

    # Save a list of User instances to CSV.
    def save_users(self, users):
        
        self._save_generic(
            self.users_path,
            users,
            ["user_id", "name", "email", "status", "max_loans"]
        )

    # Save a list of Transaction instances to CSV.
    def save_transactions(self, transactions):
        
        self._save_generic(
            self.transactions_path,
            transactions,
            ["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"]
        )
