
import csv
import os
from models import Book, User, Transaction

DATA_PATH = "data/"

class CSVStorage:
    def __init__(self):
        os.makedirs(DATA_PATH, exist_ok=True)

    def _ensure_file(self, filename, fieldnames):
        path = os.path.join(DATA_PATH, filename)
        if not os.path.exists(path):
            with open(path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
        return path

    def load_books(self):
        fieldnames = ["book_id","title","authors","isbn","tags","total_copies","available_copies","is_deleted"]
        path = self._ensure_file("books.csv", fieldnames)
        books = []
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(Book(
                    row.get("book_id",""),
                    row.get("title",""),
                    row.get("authors",""),
                    row.get("isbn",""),
                    row.get("tags",""),
                    int(row.get("total_copies","0")),
                    int(row.get("available_copies","0")),
                    row.get("is_deleted","0"),
                ))
        return books

    def save_books(self, books):
        fieldnames = ["book_id","title","authors","isbn","tags","total_copies","available_copies","is_deleted"]
        path = os.path.join(DATA_PATH, "books.csv")
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for b in books:
                writer.writerow(b.to_dict())

    def load_users(self):
        fieldnames = ["user_id","name","email","status","max_loans","active_loans","password"]
        path = self._ensure_file("users.csv", fieldnames)
        users = []
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(User(
                    row.get("user_id",""),
                    row.get("name",""),
                    row.get("email",""),
                    row.get("status","active"),
                    int(row.get("max_loans","5")),
                    int(row.get("active_loans","0")),
                    row.get("password",""),
                ))
        return users

    def save_users(self, users):
        fieldnames = ["user_id","name","email","status","max_loans","active_loans","password"]
        path = os.path.join(DATA_PATH, "users.csv")
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for u in users:
                writer.writerow(u.to_dict())
    def load_transactions(self):
        fieldnames = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status","overdue"]
        path = self._ensure_file("transactions.csv", fieldnames)
        txs = []
        with open(path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                txs.append(Transaction(
                    row.get("tx_id",""),
                    row.get("book_id",""),
                    row.get("user_id",""),
                    row.get("borrow_date",""),
                    row.get("due_date",""),
                    row.get("return_date") or None,
                    row.get("status","borrowed"),
                    row.get("overdue","0")   # <-- NEW
                ))
        return txs

    def save_transactions(self, txs):
        fieldnames = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status","overdue"]
        path = os.path.join(DATA_PATH, "transactions.csv")
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for t in txs:
                writer.writerow(t.to_dict())


    # def load_transactions(self):
    #     fieldnames = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"]
    #     path = self._ensure_file("transactions.csv", fieldnames)
    #     txs = []
    #     with open(path, "r", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             txs.append(Transaction(
    #                 row.get("tx_id",""),
    #                 row.get("book_id",""),
    #                 row.get("user_id",""),
    #                 row.get("borrow_date",""),
    #                 row.get("due_date",""),
    #                 row.get("return_date") or None,
    #                 row.get("status","borrowed"),
    #             ))
    #     return txs

    # def save_transactions(self, txs):
    #     fieldnames = ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"]
    #     path = os.path.join(DATA_PATH, "transactions.csv")
    #     with open(path, "w", newline="") as f:
    #         writer = csv.DictWriter(f, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for t in txs:
    #             writer.writerow(t.to_dict())

