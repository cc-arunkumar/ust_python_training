# storage.py
import csv
import os
from models import Book, User, Transaction


class CSVStorage:
    def __init__(self, folder="data"):
        self.folder = folder
        self.books_file = f"{folder}/books.csv"
        self.users_file = f"{folder}/users.csv"
        self.tx_file = f"{folder}/transactions.csv"

        self._init_files()

    def _init_files(self):
        if not os.path.exists(self.books_file):
            with open(self.books_file, "w", newline="") as f:
                csv.writer(f).writerow([
                    "book_id", "title", "authors", "isbn",
                    "tags", "total_copies", "available_copies"
                ])

        if not os.path.exists(self.users_file):
            with open(self.users_file, "w", newline="") as f:
                csv.writer(f).writerow([
                    "user_id", "name", "email", "status", "max_loans"
                ])

        if not os.path.exists(self.tx_file):
            with open(self.tx_file, "w", newline="") as f:
                csv.writer(f).writerow([
                    "tx_id", "book_id", "user_id",
                    "borrow_date", "due_date", "return_date", "status"
                ])

    # ============================================================
    # BOOKS
    # ============================================================

    def load_books(self):
        books = []
        with open(self.books_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                books.append(Book(
                    row["book_id"],
                    row["title"],
                    row["authors"].split("|") if row["authors"] else [],
                    row["isbn"],
                    row["tags"].split("|") if row["tags"] else [],
                    int(row["total_copies"]),
                    int(row["available_copies"])
                ))
        return books

    # append one book (add)
    def append_book(self, book):
        with open(self.books_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "book_id", "title", "authors", "isbn",
                "tags", "total_copies", "available_copies"
            ])
            writer.writerow(book.to_dict())

    # overwrite full csv (update)
    def save_books(self, books):
        with open(self.books_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "book_id", "title", "authors", "isbn",
                "tags", "total_copies", "available_copies"
            ])
            writer.writeheader()
            for b in books:
                writer.writerow(b.to_dict())

    # ============================================================
    # USERS
    # ============================================================

    def load_users(self):
        users = []
        with open(self.users_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(User(
                    row["user_id"],
                    row["name"],
                    row["email"],
                    row["status"],
                    int(row["max_loans"])
                ))
        return users

    # append one user (add)
    def append_user(self, user):
        with open(self.users_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "user_id", "name", "email", "status", "max_loans"
            ])
            writer.writerow(user.to_dict())

    # overwrite full csv (update)
    def save_users(self, users):
        with open(self.users_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "user_id", "name", "email", "status", "max_loans"
            ])
            writer.writeheader()
            for u in users:
                writer.writerow(u.to_dict())

    # ============================================================
    # TRANSACTIONS
    # ============================================================

    def load_transactions(self):
        tx_list = []
        with open(self.tx_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tx_list.append(Transaction(
                    row["tx_id"],
                    row["book_id"],
                    row["user_id"],
                    row["borrow_date"],
                    row["due_date"],
                    row["return_date"],
                    row["status"]
                ))
        return tx_list

    # append one transaction (borrow)
    def append_transaction(self, tx):
        with open(self.tx_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "tx_id", "book_id", "user_id",
                "borrow_date", "due_date",
                "return_date", "status"
            ])
            writer.writerow(tx.to_dict())

    # overwrite full csv (return / update)
    def save_transactions(self, tx_list):
        with open(self.tx_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "tx_id", "book_id", "user_id",
                "borrow_date", "due_date",
                "return_date", "status"
            ])
            writer.writeheader()
            for t in tx_list:
                writer.writerow(t.to_dict())