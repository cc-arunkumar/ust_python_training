# storage.py
import csv
import os
from models import Book, User, Transaction

DATA_DIR = "data"

class CSVStorage:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)

    def _file(self, name, headers):
        """Ensure file exists with headers, return path."""
        path = os.path.join(DATA_DIR, name)
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
        return path

    def _load(self, filename, headers, factory):
        """Generic loader: returns list of objects created by factory(row)."""
        path = self._file(filename, headers)
        items = []
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    obj = factory(row)
                    if obj:  # skip invalid
                        items.append(obj)
                except Exception:
                    continue
        return items

    def _save(self, filename, headers, objects):
        """Generic saver: writes list of objects with to_dict()."""
        path = os.path.join(DATA_DIR, filename)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for obj in objects:
                writer.writerow(obj.to_dict())

    # ---------------- Books ----------------
    def load_books(self):
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
        headers = ["book_id","title","authors","isbn","tags","total_copies","available_copies"]
        self._save("books(in).csv", headers, books)

    # ---------------- Users ----------------
    def load_users(self):
        headers = ["user_id","name","email","status","max_loans"]
        return self._load("users(in).csv", headers, lambda r: User(
            r.get("user_id",""),
            r.get("name",""),
            r.get("email",""),
            r.get("status","active"),
            int(r.get("max_loans","0"))
        ) if r.get("user_id") and r.get("name") else None)

    def save_users(self, users):
        headers = ["user_id","name","email","status","max_loans"]
        self._save("users(in).csv", headers, users)

    # ---------------- Transactions ----------------
    def load_transactions(self):
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
