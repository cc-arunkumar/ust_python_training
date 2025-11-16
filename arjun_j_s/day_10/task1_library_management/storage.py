import csv
import os
from models import Book, User, Transaction

class CSVStorage:
    def __init__(self, data_dir="data"):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(BASE_DIR, data_dir)

        self.books_file = os.path.join(self.data_dir, "books.csv")
        self.users_file = os.path.join(self.data_dir, "users.csv")
        self.transactions_file = os.path.join(self.data_dir, "transactions.csv")

    # ---------- BOOKS ----------
    def load_books(self):
        books = {}
        if not os.path.exists(self.books_file):
            return books

        with open(self.books_file, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("book_id"): 
                    continue
                books[row["book_id"]] = Book(
                    row["book_id"],
                    row["title"],
                    row["authors"],
                    row["isbn"],
                    row["tags"],
                    int(row["total_copies"]),
                    int(row["available_copies"])
                )
        return books

    def save_books(self, books):
        with open(self.books_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["book_id","title","authors","isbn","tags","total_copies","available_copies"])
            for b in books.values():
                writer.writerow([
                    b.book_id,
                    b.title,
                    b.authors,
                    b.isbn,
                    "|".join(b.tags),
                    b.total_copies,
                    b.available_copies
                ])

    # ---------- USERS ----------
    def load_users(self):
        users = {}
        if not os.path.exists(self.users_file):
            return users

        with open(self.users_file, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("user_id"): 
                    continue
                users[row["user_id"]] = User(
                    row["user_id"],
                    row["name"],
                    row["email"],
                    row["status"],
                    int(row["max_loans"])
                )
        return users

    def save_users(self, users):
        with open(self.users_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["user_id","name","email","status","max_loans"])
            for u in users.values():
                writer.writerow([
                    u.user_id,
                    u.name,
                    u.email,
                    u.status,
                    u.max_loans
                ])

    # ---------- TRANSACTIONS ----------
    def load_transactions(self):
        txs = {}
        if not os.path.exists(self.transactions_file):
            return txs

        with open(self.transactions_file, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("tx_id"):
                    continue
                txs[row["tx_id"]] = Transaction(
                    row["tx_id"],
                    row["user_id"],
                    row["book_id"],
                    row["borrow_date"],
                    row["due_date"],
                    row["return_date"],
                    row["status"]
                )
        return txs

    def save_transactions(self, txs):
        with open(self.transactions_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["tx_id","user_id","book_id","borrow_date","due_date","return_date","status"])
            for t in txs.values():
                writer.writerow([
                    t.tx_id,
                    t.user_id,
                    t.book_id,
                    t.borrow_date,
                    t.due_date,
                    t.return_date,
                    t.status
                ])
