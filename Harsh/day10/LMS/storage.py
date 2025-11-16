import csv
import os
from typing import List
from models import Book, User, Transaction, parse_list_field

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
BOOKS_CSV = os.path.join(DATA_DIR, "books.csv")
USERS_CSV = os.path.join(DATA_DIR, "users.csv")
TX_CSV = os.path.join(DATA_DIR, "transactions.csv")

BOOK_HEADERS = ["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"]
USER_HEADERS = ["user_id", "name", "email", "status", "max_loans","password"]
TX_HEADERS = ["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"]


class CSVStorage:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self._ensure_file(BOOKS_CSV, BOOK_HEADERS)
        self._ensure_file(USERS_CSV, USER_HEADERS)
        self._ensure_file(TX_CSV, TX_HEADERS)

    def _ensure_file(self, path: str, headers: List[str]):
        if not os.path.exists(path):
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=headers)
                w.writeheader()

    # Books
    def load_books(self) -> List[Book]:
        books = []
        try:
            with open(BOOKS_CSV, "r", newline="", encoding="utf-8") as f:
                r = csv.DictReader(f)
                for row in r:
                    try:
                        b = Book(
                            book_id=row.get("book_id", "").strip(),
                            title=row.get("title", "").strip(),
                            authors=parse_list_field(row.get("authors", "")),
                            isbn=row.get("isbn", "").strip(),
                            tags=parse_list_field(row.get("tags", "")),
                            total_copies=int(row.get("total_copies", "0")),
                            available_copies=int(row.get("available_copies", "0")),
                        )
                        if not b.book_id:
                            continue
                        books.append(b)
                    except Exception:
                        # Skip malformed rows gracefully
                        continue
        except FileNotFoundError:
            # Ensure file exists with headers
            self._ensure_file(BOOKS_CSV, BOOK_HEADERS)
        return books

    def save_books(self, list_of_books: List[Book]):
        with open(BOOKS_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=BOOK_HEADERS)
            w.writeheader()
            for b in list_of_books:
                w.writerow(b.to_dict())
        with open(BOOKS_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=BOOK_HEADERS)
            w.writeheader()
            for b in list_of_books:
                w.writerow(b.to_dict())

    # Users
    def load_users(self) -> List[User]:
        users = []
        try:
            with open(USERS_CSV, "r", newline="", encoding="utf-8") as f:
                r = csv.DictReader(f)
                for row in r:
                    try:
                        u = User(
                            user_id=row.get("user_id", "").strip(),
                            name=row.get("name", "").strip(),
                            email=row.get("email", "").strip() or None,
                            status=row.get("status", "active").strip(),
                            max_loans=int(row.get("max_loans", "5")),
                            password=row.get('password') or None,
                        )
                        if not u.user_id:
                            continue
                        users.append(u)
                    except Exception:
                        continue
        except FileNotFoundError:
            self._ensure_file(USERS_CSV, USER_HEADERS)
        return users

    def save_users(self, list_of_users: List[User]):
        with open(USERS_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=USER_HEADERS)
            w.writeheader()
            for u in list_of_users:
                row = u.to_dict()
                w.writerow(row)
        with open(USERS_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=USER_HEADERS)
            w.writeheader()
            for u in list_of_users:
                row = u.to_dict()
                # ensure all header fields are present in correct order
                w.writerow({k: row.get(k, "") for k in USER_HEADERS})

    # Transactions
    def load_transactions(self) -> List[Transaction]:
        txs = []
        try:
            with open(TX_CSV, "r", newline="", encoding="utf-8") as f:
                r = csv.DictReader(f)
                # If headers are wrong (like books headers), DictReader will still provide keys;
                # we skip rows missing required transaction fields
                for row in r:
                    try:
                        tx_id = row.get("tx_id", "").strip()
                        book_id = row.get("book_id", "").strip()
                        user_id = row.get("user_id", "").strip()
                        borrow_date = row.get("borrow_date", "").strip()
                        due_date = row.get("due_date", "").strip()
                        return_date = row.get("return_date", "").strip() or None
                        status = row.get("status", "").strip() or "borrowed"

                        # Basic validation: require tx_id, book_id, user_id, borrow_date, due_date
                        required_present = all([tx_id, book_id, user_id, borrow_date, due_date])
                        if not required_present:
                            # Skip malformed rows gracefully
                            continue

                        t = Transaction(
                            tx_id=tx_id,
                            book_id=book_id,
                            user_id=user_id,
                            borrow_date=borrow_date,
                            due_date=due_date,
                            return_date=return_date,
                            status=status,
                        )
                        txs.append(t)
                    except Exception:
                        continue
        except FileNotFoundError:
            self._ensure_file(TX_CSV, TX_HEADERS)
        return txs

    def save_transactions(self, list_of_transactions: List[Transaction]):
        with open(TX_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=TX_HEADERS)
            w.writeheader()
            for t in list_of_transactions:
                w.writerow(t.to_dict())
