from typing import List, Dict, Optional
from models import (
    Book, User, Transaction,
    InvalidBookError, InvalidUserError, BookNotAvailableError,
    UserNotAllowedError, TransactionError, ValidationError
)
from utils import today_str, add_days_str

class Library:
    def __init__(self, storage):
        self.storage = storage
        self.books: List[Book] = self.storage.load_books()
        self.users: List[User] = self.storage.load_users()
        self.transactions: List[Transaction] = self.storage.load_transactions()
        self._reindex()

    def _reindex(self):
        self._books_by_id: Dict[str, Book] = {b.book_id: b for b in self.books}
        self._isbn_set = set([b.isbn for b in self.books if b.isbn])
        self._users_by_id: Dict[str, User] = {u.user_id: u for u in self.users}
        self._tx_by_id: Dict[str, Transaction] = {t.tx_id: t for t in self.transactions}

    def save_all(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)

    # Utility to generate next transaction ID
    def _next_tx_id(self) -> str:
        max_num = 0
        for tx in self.transactions:
            if tx.tx_id.startswith("T"):
                try:
                    n = int(tx.tx_id[1:])
                    max_num = max(max_num, n)
                except ValueError:
                    continue
        return f"T{max_num + 1}"

    # Book operations
    def add_book(self, book: Book):
        if not book.book_id.strip():
            raise ValidationError("book_id cannot be empty")
        if book.book_id in self._books_by_id:
            raise InvalidBookError("Book ID must be unique")
        if book.isbn and book.isbn in self._isbn_set:
            raise ValidationError("ISBN must be unique")
        if book.available_copies > book.total_copies:
            raise ValidationError("available_copies cannot exceed total_copies")
        self.books.append(book)
        self._reindex()
        self.storage.save_books(self.books)

    def update_book(self, book_id: str, **kwargs):
        b = self._books_by_id.get(book_id)
        if not b:
            raise InvalidBookError("Book not found")
        old_isbn = b.isbn
        # Temporarily compute new values for uniqueness check
        new_isbn = kwargs.get("isbn", old_isbn)
        if new_isbn != old_isbn:
            if new_isbn and new_isbn in self._isbn_set:
                raise ValidationError("ISBN must be unique")
        b.update(**kwargs)
        self._reindex()
        self.storage.save_books(self.books)

    def remove_book(self, book_id: str):
        b = self._books_by_id.get(book_id)
        if not b:
            raise InvalidBookError("Book not found")
        # Cannot remove if currently borrowed or overdue
        active_for_book = any(
            t.book_id == book_id and t.status in {"borrowed", "overdue"}
            for t in self.transactions
        )
        if active_for_book:
            raise InvalidBookError("Cannot remove a book with active loans")
        self.books = [bk for bk in self.books if bk.book_id != book_id]
        self._reindex()
        self.storage.save_books(self.books)

    def get_book(self, book_id: str) -> Optional[Book]:
        return self._books_by_id.get(book_id)

    def list_books(self) -> List[Book]:
        return list(self.books)

    def search_books_title(self, substring: str) -> List[Book]:
        s = substring.lower()
        return [b for b in self.books if s in b.title.lower()]

    def search_books_author(self, author: str) -> List[Book]:
        a = author.lower()
        return [b for b in self.books if any(a in x.lower() for x in b.authors)]

    def search_books_tag(self, tag: str) -> List[Book]:
        t = tag.lower()
        return [b for b in self.books if any(t == x.lower() for x in b.tags)]

    # User operations
    def add_user(self, user: User):
        if not user.user_id.strip():
            raise ValidationError("user_id cannot be empty")
        if user.user_id in self._users_by_id:
            raise InvalidUserError("User ID must be unique")
        if user.status not in {"active", "inactive", "banned"}:
            raise ValidationError("Invalid user status")    
        self.users.append(user)
        self._reindex()
        self.storage.save_users(self.users)

    def update_user(self, user_id: str, **kwargs):
        u = self._users_by_id.get(user_id)
        if not u:
            raise InvalidUserError("User not found")
        for k, v in kwargs.items():
            if hasattr(u, k):
                setattr(u, k, v)
        if u.status not in {"active", "inactive", "banned"}:
            raise ValidationError("Invalid user status")
        self._reindex()
        self.storage.save_users(self.users)

    def get_user(self, user_id: str) -> Optional[User]:
        return self._users_by_id.get(user_id)

    def list_users(self) -> List[User]:
        return list(self.users)

    def deactivate_user(self, user_id: str):
        
        u = self._users_by_id.get(user_id)
        if not u:
            raise InvalidUserError("User not found")
        u.deactivate()
        self.storage.save_users(self.users)

    def activate_user(self, user_id: str):
        u = self._users_by_id.get(user_id)
        if not u:
            raise InvalidUserError("User not found")
        u.activate()
        self.storage.save_users(self.users)

    def ban_user(self, user_id: str):
        u = self._users_by_id.get(user_id)
        if not u:
            raise InvalidUserError("User not found")
        u.ban()
        self.storage.save_users(self.users)

    # Borrow/Return operations
    def _active_loans_for_user(self, user_id: str) -> int:
        return sum(1 for t in self.transactions if t.user_id == user_id and t.status in {"borrowed", "overdue"})

    def borrow(self, user_id: str, book_id: str) -> Transaction:
        b = self._books_by_id.get(book_id)
        if not b:
            raise InvalidBookError("Book does not exist")
        u = self._users_by_id.get(user_id)
        if not u:
            raise InvalidUserError("User does not exist")
        if u.status != "active":
            raise UserNotAllowedError("User is not allowed to borrow")
        if not b.is_available():
            raise BookNotAvailableError("Book not available")
        active_loans = self._active_loans_for_user(user_id)
        if not u.can_borrow(active_loans):
            raise UserNotAllowedError("User has reached max loans")

        borrow_date = today_str()
        due_date = add_days_str(borrow_date, 14)
        tx_id = self._next_tx_id()

        t = Transaction(
            tx_id=tx_id, book_id=book_id, user_id=user_id,
            borrow_date=borrow_date, due_date=due_date, status="borrowed"
        )
        self.transactions.append(t)
        b.available_copies -= 1
        self._reindex()
        self.storage.save_books(self.books)
        self.storage.save_transactions(self.transactions)
        return t

    
        
    def return_book(self, tx_id: str) -> Transaction:
        t = self._tx_by_id.get(tx_id)
        if not t:
            raise TransactionError("Transaction not found")
        if t.status not in {"borrowed", "overdue"}:
            raise TransactionError("Book already returned or not borrowed")
        t.mark_returned(today_str())
        # increment book availability
        b = self._books_by_id.get(t.book_id)
        if b:
            b.available_copies += 1
        self._reindex()
        self.storage.save_books(self.books)
        self.storage.save_transactions(self.transactions)
        return t

    # Transactions queries
    def loans_active(self) -> List[Transaction]:
        return [t for t in self.transactions if t.status == "borrowed"]

    def loans_overdue(self) -> List[Transaction]:
        today = today_str()
        result = []
        changed = False
        for t in self.transactions:
            if t.status == "borrowed" and t.is_overdue(today):
                t.status = "overdue"
                result.append(t)
                changed = True
        if changed:
            self._reindex()
            self.storage.save_transactions(self.transactions)
        return result

    def loans_user(self, user_id: str) -> List[Transaction]:
        return [t for t in self.transactions if t.user_id == user_id]

    # Reports
    def report_summary(self) -> Dict[str, int]:
        total_books = len(self.books)
        total_users = len(self.users)
        active_loans = sum(1 for t in self.transactions if t.status == "borrowed")
        overdue_loans = sum(1 for t in self.transactions if t.status == "overdue")
        return {
            "total_books": total_books,
            "total_users": total_users,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
        }

    def report_user_history(self, user_id: str) -> List[Transaction]:
        return self.loans_user(user_id)
