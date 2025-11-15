# library.py
from models import *
from storage import CSVStorage
from utils import today_str, add_days, parse_date

class Library:
    def __init__(self, storage: CSVStorage):
        self.storage = storage
        self.books = storage.load_books()
        self.users = storage.load_users()
        self.transactions = storage.load_transactions()

    # --- Book methods ---
    def add_book(self, book: Book):
        if not book.book_id.strip():
            raise ValidationError("book_id cannot be empty.")
        if self.get_book(book.book_id):
            raise InvalidBookError("Book ID already exists.")
        if book.isbn and any(b.isbn == book.isbn for b in self.books):
            raise ValidationError("ISBN must be unique.")
        if book.available_copies > book.total_copies:
            raise ValidationError("available_copies cannot exceed total_copies.")
        self.books.append(book)

    def update_book(self, book_id: str, **kwargs):
        book = self.get_book(book_id)
        if not book:
            raise InvalidBookError("Book not found.")
        book.update(**kwargs)

    def remove_book(self, book_id: str):
        book = self.get_book(book_id)
        if not book:
            raise InvalidBookError("Book not found.")
        if any(tx.book_id == book_id and tx.status == "borrowed" for tx in self.transactions):
            raise InvalidBookError("Cannot remove book with active loans.")
        self.books = [b for b in self.books if b.book_id != book_id]

    def get_book(self, book_id: str):
        return next((b for b in self.books if b.book_id == book_id), None)

    def list_books(self):
        return list(self.books)

    def search_books(self, title_substr=None, author=None, tag=None):
        results = self.books
        if title_substr:
            results = [b for b in results if title_substr.lower() in b.title.lower()]
        if author:
            results = [b for b in results if any(author.lower() in a.lower() for a in b.authors)]
        if tag:
            results = [b for b in results if any(tag.lower() in t.lower() for t in b.tags)]
        return results

    # --- User methods ---
    def add_user(self, user: User):
        if not user.user_id.strip():
            raise ValidationError("user_id cannot be empty.")
        if self.get_user(user.user_id):
            raise InvalidUserError("User ID already exists.")
        if user.status not in ("active","inactive","banned"):
            raise ValidationError("Invalid status for user.")
        self.users.append(user)

    def update_user(self, user_id: str, **kwargs):
        user = self.get_user(user_id)
        if not user:
            raise InvalidUserError("User not found.")
        for k, v in kwargs.items():
            if hasattr(user, k) and v is not None:
                setattr(user, k, v)

    def get_user(self, user_id: str):
        return next((u for u in self.users if u.user_id == user_id), None)

    def list_users(self):
        return list(self.users)

    def deactivate_user(self, user_id: str):
        user = self.get_user(user_id)
        if not user: raise InvalidUserError("User not found.")
        user.deactivate()

    def activate_user(self, user_id: str):
        user = self.get_user(user_id)
        if not user: raise InvalidUserError("User not found.")
        user.activate()

    def ban_user(self, user_id: str):
        user = self.get_user(user_id)
        if not user: raise InvalidUserError("User not found.")
        user.ban()

    # --- Borrow / Return ---
    def borrow(self, user_id: str, book_id: str):
        book = self.get_book(book_id)
        user = self.get_user(user_id)
        if not book: raise InvalidBookError("Book not found.")
        if not user: raise InvalidUserError("User not found.")
        if not book.is_available(): raise BookNotAvailableError("No copies available.")
        active_loans = sum(1 for t in self.transactions if t.user_id==user_id and t.status=="borrowed")
        if not user.can_borrow(active_loans):
            raise UserNotAllowedError("User cannot borrow more books.")
        tx_id = f"T{len(self.transactions)+1}"
        tx = Transaction(tx_id, book_id, user_id, today_str(), add_days(today_str(),14))
        self.transactions.append(tx)
        book.available_copies -= 1
        return tx

    def return_book(self, tx_id: str):
        tx = next((t for t in self.transactions if t.tx_id==tx_id), None)
        if not tx: raise TransactionError("Transaction not found.")
        tx.mark_returned(today_str())
        book = self.get_book(tx.book_id)
        if book: book.available_copies += 1
        return tx

    # --- Reports ---
    def loans_active(self):
        return [t for t in self.transactions if t.status=="borrowed"]

    def loans_overdue(self):
        today = parse_date(today_str())
        return [t for t in self.transactions if t.status=="borrowed" and parse_date(t.due_date) < today]

    def loans_user(self, user_id):
        return [t for t in self.transactions if t.user_id == user_id]

    def report_summary(self):
        return {
            "total_books": len(self.books),
            "total_users": len(self.users),
            "active_loans": len(self.loans_active()),
            "overdue_loans": len(self.loans_overdue()),
        }

    def report_user(self, user_id):
        return self.loans_user(user_id)

    # --- Persistence ---
    def save_all(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)
