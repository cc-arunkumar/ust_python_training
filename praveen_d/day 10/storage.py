import csv
import os
from models import Book, User, Transaction

# Folder where all CSV files will be stored
DATA_DIR = "C:\\UST python\\Praveen D\\day10\\library_management_assessment\\data"

class CSVStorage:
    def __init__(self):
        # Ensure the data directory exists; create it if missing
        os.makedirs(DATA_DIR, exist_ok=True)

    def _file(self, name, headers):
        """
        Ensure a CSV file exists with the given headers.
        If the file does not exist, create it and write the header row.
        Returns the full path to the file.
        """
        path = os.path.join(DATA_DIR, name)
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
        return path

    def _load(self, filename, headers, factory):
        """
        Generic loader function.
        - Ensures the file exists (with headers).
        - Reads rows from the CSV.
        - Uses the provided 'factory' function to convert each row into an object (Book/User/Transaction).
        - Skips malformed rows gracefully.
        Returns a list of objects.
        """
        path = self._file(filename, headers)
        items = []
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    obj = factory(row)
                    if obj:  # skip invalid rows
                        items.append(obj)
                except Exception:
                    # If any error occurs while parsing a row, skip it
                    continue
        return items

    def _save(self, filename, headers, objects):
        """
        Generic saver function.
        - Overwrites the CSV file with the provided list of objects.
        - Each object must implement a to_dict() method.
        """
        path = os.path.join(DATA_DIR, filename)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for obj in objects:
                writer.writerow(obj.to_dict())

    # ---------------- Books ----------------
    def load_books(self):
        """
        Load all books from books(in).csv.
        Each row is converted into a Book object.
        Returns a list of Book objects.
        """
        headers = ["book_id","title","authors","isbn","tags","total_copies","available_copies"]
        return self._load("books(in).csv", headers, lambda r: Book(
            r.get("book_id",""),
            r.get("title",""),
            r.get("authors","").split("|") if r.get("authors") else [],
            r.get("isbn",""),
            r.get("tags","").split("|") if r.get("tags") else [],
            int(r.get("total_copies","0")),
            int(r.get("available_copies","0"))
        ) if r.get("book_id") and r.get("title") else None)

    def save_books(self, books):
        """
        Save all Book objects to books.csv.
        Overwrites the file with the current list of books.
        """
        headers = ["book_id","title","authors","isbn","tags","total_copies","available_copies"]
        self._save("books(in).csv", headers, books)

    # ---------------- Users ----------------
    def load_users(self):
        """
        Load all users from users(in).csv.
        Each row is converted into a User object.
        Returns a list of User objects.
        """
        headers = ["user_id","name","email","status","max_loans"]
        return self._load("users(in).csv", headers, lambda r: User(
            r.get("user_id",""),
            r.get("name",""),
            r.get("email",""),
            r.get("status","active"),
            int(r.get("max_loans","5"))
        ) if r.get("user_id") and r.get("name") else None)

    def save_users(self, users):
        """
        Save all User objects to users.csv.
        Overwrites the file with the current list of users.
        """
        headers = ["user_id","name","email","status","max_loans"]
        self._save("users(in).csv", headers, users)

    # ---------------- Transactions ----------------
    def load_transactions(self):
        """
        Load all transactions from transactions(in).csv.
        Each row is converted into a Transaction object.
        Returns a list of Transaction objects.
        """
        headers = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"]
        return self._load("transactions(in).csv", headers, lambda r: Transaction(
            r.get("tx_id",""),
            r.get("book_id",""),
            r.get("user_id",""),
            r.get("borrow_date",""),
            r.get("due_date",""),
            r.get("return_date") or None,
            r.get("status","borrowed")
        ) if r.get("tx_id") and r.get("book_id") and r.get("user_id") else None)

    def save_transactions(self, txs):
        headers = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"]
        self._save("transactions(in).csv", headers, txs)
