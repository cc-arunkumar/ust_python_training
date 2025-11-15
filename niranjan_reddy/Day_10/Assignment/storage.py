import os
import csv
from models import Book, User, Transaction

class CSVStorage:
    def __init__(self, books_path, users_path, transactions_path):
        self.books_path = books_path
        self.users_path = users_path
        self.transactions_path = transactions_path

        self._ensure_file(self.books_path, ["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
        self._ensure_file(self.users_path, ["user_id", "name", "email", "status", "max_loans"])
        self._ensure_file(self.transactions_path, ["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])

    def _ensure_file(self, path, headers):
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(headers)


    def load_books(self):
        return self._load_generic(self.books_path, Book, ["authors", "tags"], list_fields=["authors", "tags"])

    def load_users(self):
        return self._load_generic(self.users_path, User, int_fields=["max_loans"])

    def load_transactions(self):
        return self._load_generic(self.transactions_path, Transaction, ["return_date"], optional_fields=["return_date"])

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
                        for field in int_fields:
                            row[field] = int(row[field])
                        for field in list_fields:
                            row[field] = row[field].split("|") if row[field] else []
                        for field in optional_fields:
                            row[field] = row[field] if row[field] else None
                        item = cls(**row)
                        items.append(item)
                    except Exception as e:
                        print(f"Skipping row due to error: {row} ({e})")
        except FileNotFoundError:
            pass
        return items

    def save_books(self, books):
        self._save_generic(self.books_path, books, ["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"], list_fields=["authors", "tags"])

    def save_users(self, users):
        self._save_generic(self.users_path, users, ["user_id", "name", "email", "status", "max_loans"])

    def save_transactions(self, transactions):
        self._save_generic(self.transactions_path, transactions, ["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])

    def _save_generic(self, path, items, fieldnames, list_fields=None):
        list_fields = list_fields or []
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in items:
                data = item.to_dict()
                for field in list_fields:
                    data[field] = "|".join(data[field])
                writer.writerow(data)
