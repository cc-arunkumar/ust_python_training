# storage.py
import os
from models import Book, User, Transaction
from utils import ensure_data_dir, read_csv, write_csv, split_pipe

BOOKS_FILE = "data/books.csv"
USERS_FILE = "data/users.csv"
TX_FILE = "data/transactions.csv"

class CSVStorage:
    def __init__(self):
        ensure_data_dir()
        self._init_files()

    def _init_files(self):
        if not os.path.exists(BOOKS_FILE):
            write_csv(BOOKS_FILE, ["book_id","title","authors","isbn","tags","total_copies","available_copies"], [])
        if not os.path.exists(USERS_FILE):
            write_csv(USERS_FILE, ["user_id","name","email","status","max_loans"], [])
        if not os.path.exists(TX_FILE):
            write_csv(TX_FILE, ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"], [])

    def load_books(self):
        return [Book(
            book_id=r["book_id"],
            title=r["title"],
            authors=split_pipe(r["authors"]),
            isbn=r["isbn"],
            tags=split_pipe(r["tags"]),
            total_copies=int(r["total_copies"]),
            available_copies=int(r["available_copies"])
        ) for r in read_csv(BOOKS_FILE)]

    def save_books(self, books):
        write_csv(BOOKS_FILE,
                  ["book_id","title","authors","isbn","tags","total_copies","available_copies"],
                  [b.to_dict() for b in books])

    def load_users(self):
        return [User(
            user_id=r["user_id"],
            name=r["name"],
            email=r["email"],
            status=r["status"],
            max_loans=int(r["max_loans"])
        ) for r in read_csv(USERS_FILE)]

    def save_users(self, users):
        write_csv(USERS_FILE,
                  ["user_id","name","email","status","max_loans"],
                  [u.to_dict() for u in users])

    def load_transactions(self):
        return [Transaction(
            tx_id=r["tx_id"],
            book_id=r["book_id"],
            user_id=r["user_id"],
            borrow_date=r["borrow_date"],
            due_date=r["due_date"],
            return_date=r["return_date"] or None,
            status=r["status"]
        ) for r in read_csv(TX_FILE)]

    def save_transactions(self, txs):
        write_csv(TX_FILE,
                  ["tx_id","book_id","user_id","borrow_date","due_date","return_date","status"],
                  [t.to_dict() for t in txs])
