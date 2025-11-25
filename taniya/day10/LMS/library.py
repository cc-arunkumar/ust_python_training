from typing import List, Dict, Optional
from models import (
    Book, User, Transaction,
    InvalidBookError, InvalidUserError, BookNotAvailableError,
    UserNotAllowedError, TransactionError, ValidationError
)
from utils import today_str, add_days_str


# Define Library class to manage books, users, and transactions
class Library:
    # Constructor initializes storage and loads data
    def __init__(self, storage):
        self.storage = storage
        self.books: List[Book] = self.storage.load_books()              # Load all books from storage
        self.users: List[User] = self.storage.load_users()              # Load all users from storage
        self.transactions: List[Transaction] = self.storage.load_transactions()  # Load all transactions
        self._reindex()  # Build internal indexes for fast lookup

    # Internal method to rebuild indexes for quick access
    def _reindex(self):
        self._books_by_id: Dict[str, Book] = {b.book_id: b for b in self.books}   # Map book_id → Book
        self._isbn_set = set([b.isbn for b in self.books if b.isbn])              # Set of all ISBNs
        self._users_by_id: Dict[str, User] = {u.user_id: u for u in self.users}   # Map user_id → User
        self._tx_by_id: Dict[str, Transaction] = {t.tx_id: t for t in self.transactions}  # Map tx_id → Transaction

    # Save all data back to storage
    def save_all(self):
        self.storage.save_books(self.books)          # Save books list
        self.storage.save_users(self.users)          # Save users list
        self.storage.save_transactions(self.transactions)  # Save transactions list

    # Utility to generate next transaction ID
    def _next_tx_id(self) -> str:
        max_num = 0
        for tx in self.transactions:
            if tx.tx_id.startswith("T"):             # Transaction IDs start with 'T'
                try:
                    n = int(tx.tx_id[1:])            # Extract numeric part
                    max_num = max(max_num, n)        # Track maximum transaction number
                except ValueError:
                    continue
        return f"T{max_num + 1}"                     # Generate next transaction ID

    # -------------------------------
    # Book operations
    # -------------------------------

    # Add a new book to the library
    def add_book(self, book: Book):
        if not book.book_id.strip():                 # Validate book_id is not empty
            raise ValidationError("book_id cannot be empty")
        if book.book_id in self._books_by_id:        # Ensure book_id is unique
            raise InvalidBookError("Book ID must be unique")
        if book.isbn and book.isbn in self._isbn_set: # Ensure ISBN is unique
            raise ValidationError("ISBN must be unique")
        if book.available_copies > book.total_copies: # Validate available copies
            raise ValidationError("available_copies cannot exceed total_copies")
        self.books.append(book)                      # Add book to list
        self._reindex()                              # Rebuild indexes
        self.storage.save_books(self.books)          # Save updated books list

    # Update book details
    def update_book(self, book_id: str, **kwargs):
        b = self._books_by_id.get(book_id)           # Find book by ID
        if not b:
            raise InvalidBookError("Book not found")
        old_isbn = b.isbn
        new_isbn = kwargs.get("isbn", old_isbn)      # Get new ISBN if provided
        # Check uniqueness of new ISBN
        if new_isbn != old_isbn:
            if new_isbn and new_isbn in self._isbn_set:
                raise ValidationError("ISBN must be unique")
        b.update(**kwargs)                           # Update book attributes
        self._reindex()                              # Rebuild indexes
        self.storage.save_books(self.books)          # Save updated books list

    # Remove a book from the library
    def remove_book(self, book_id: str):
        b = self._books_by_id.get(book_id)           # Find book by ID
        if not b:
            raise InvalidBookError("Book not found")
        # Cannot remove if currently borrowed or overdue
        active_for_book = any(
            t.book_id == book_id and t.status in {"borrowed", "overdue"}
            for t in self.transactions
        )
        if active_for_book:
            raise InvalidBookError("Cannot remove a book with active loans")
        # Remove book from list
        self.books = [bk for bk in self.books if bk.book_id != book_id]
        self._reindex()                              # Rebuild indexes
        self.storage.save_books(self.books)          # Save updated books list

    # Get a book by its ID
    def get_book(self, book_id: str) -> Optional[Book]:
        return self._books_by_id.get(book_id)

    # List all books in the library
    def list_books(self) -> List[Book]:
        return list(self.books)

    # Search books by title substring
    def search_books_title(self, substring: str) -> List[Book]:
        s = substring.lower()
        return [b for b in self.books if s in b.title.lower()]

    # Search books by author name
    def search_books_author(self, author: str) -> List[Book]:
        a = author.lower()
        return [b for b in self.books if any(a in x.lower() for x in b.authors)]

    # Search books by tag
    def search_books_tag(self, tag: str) -> List[Book]:
        t = tag.lower()
        return [b for b in self.books if any(t == x.lower() for x in b.tags)]

   # -------------------------------
# User operations
# -------------------------------

    # Add a new user to the library system
    def add_user(self, user: User):
        if not user.user_id.strip():                     # Validate user_id is not empty
            raise ValidationError("user_id cannot be empty")
        if user.user_id in self._users_by_id:            # Ensure user_id is unique
            raise InvalidUserError("User ID must be unique")
        if user.status not in {"active", "inactive", "banned"}:  # Validate user status
            raise ValidationError("Invalid user status")
        self.users.append(user)                          # Add user to list
        self._reindex()                                  # Rebuild indexes
        self.storage.save_users(self.users)              # Save updated users list

    # Update user details
    def update_user(self, user_id: str, **kwargs):
        u = self._users_by_id.get(user_id)               # Find user by ID
        if not u:
            raise InvalidUserError("User not found")
        for k, v in kwargs.items():                      # Update provided attributes
            if hasattr(u, k):
                setattr(u, k, v)
        if u.status not in {"active", "inactive", "banned"}:  # Validate updated status
            raise ValidationError("Invalid user status")
        self._reindex()                                  # Rebuild indexes
        self.storage.save_users(self.users)              # Save updated users list

    # Get a user by ID
    def get_user(self, user_id: str) -> Optional[User]:
        return self._users_by_id.get(user_id)

    # List all users
    def list_users(self) -> List[User]:
        return list(self.users)

    # Deactivate a user
    def deactivate_user(self, user_id: str):
        u = self._users_by_id.get(user_id)               # Find user by ID
        if not u:
            raise InvalidUserError("User not found")
        u.deactivate()                                   # Call user's deactivate method
        self.storage.save_users(self.users)              # Save updated users list

    # Activate a user
    def activate_user(self, user_id: str):
        u = self._users_by_id.get(user_id)               # Find user by ID
        if not u:
            raise InvalidUserError("User not found")
        u.activate()                                     # Call user's activate method
        self.storage.save_users(self.users)              # Save updated users list

    # Ban a user
    def ban_user(self, user_id: str):
        u = self._users_by_id.get(user_id)               # Find user by ID
        if not u:
            raise InvalidUserError("User not found")
        u.ban()                                          # Call user's ban method
        self.storage.save_users(self.users)              # Save updated users list


# -------------------------------
# Borrow/Return operations
# -------------------------------

    # Count active loans for a user (borrowed or overdue)
    def _active_loans_for_user(self, user_id: str) -> int:
        return sum(1 for t in self.transactions if t.user_id == user_id and t.status in {"borrowed", "overdue"})

    # Borrow a book
    def borrow(self, user_id: str, book_id: str) -> Transaction:
        b = self._books_by_id.get(book_id)               # Find book by ID
        if not b:
            raise InvalidBookError("Book does not exist")
        u = self._users_by_id.get(user_id)               # Find user by ID
        if not u:
            raise InvalidUserError("User does not exist")
        if u.status != "active":                         # Only active users can borrow
            raise UserNotAllowedError("User is not allowed to borrow")
        if not b.is_available():                         # Check book availability
            raise BookNotAvailableError("Book not available")
        active_loans = self._active_loans_for_user(user_id)
        if not u.can_borrow(active_loans):               # Check user's borrowing limit
            raise UserNotAllowedError("User has reached max loans")

        borrow_date = today_str()                        # Get today's date
        due_date = add_days_str(borrow_date, 14)         # Set due date (14 days later)
        tx_id = self._next_tx_id()                       # Generate transaction ID

        # Create new transaction
        t = Transaction(
            tx_id=tx_id, book_id=book_id, user_id=user_id,
            borrow_date=borrow_date, due_date=due_date, status="borrowed"
        )
        self.transactions.append(t)                      # Add transaction to list
        b.available_copies -= 1                          # Decrease available copies
        self._reindex()                                  # Rebuild indexes
        self.storage.save_books(self.books)              # Save updated books list
        self.storage.save_transactions(self.transactions) # Save updated transactions
        return t

    # Return a borrowed book
    def return_book(self, tx_id: str) -> Transaction:
        t = self._tx_by_id.get(tx_id)                    # Find transaction by ID
        if not t:
            raise TransactionError("Transaction not found")
        if t.status not in {"borrowed", "overdue"}:      # Ensure book is borrowed/overdue
            raise TransactionError("Book already returned or not borrowed")
        t.mark_returned(today_str())                     # Mark transaction as returned
        b = self._books_by_id.get(t.book_id)             # Find book by ID
        if b:
            b.available_copies += 1                      # Increase available copies
        self._reindex()                                  # Rebuild indexes
        self.storage.save_books(self.books)              # Save updated books list
        self.storage.save_transactions(self.transactions) # Save updated transactions
        return t


# -------------------------------
# Transaction queries
# -------------------------------

    # List all active loans
    def loans_active(self) -> List[Transaction]:
        return [t for t in self.transactions if t.status == "borrowed"]

    # List overdue loans and update their status
    def loans_overdue(self) -> List[Transaction]:
        today = today_str()                              # Get today's date
        result = []                                      # Store overdue transactions
        changed = False                                  # Track if any status changed
        for t in self.transactions:
            if t.status == "borrowed" and t.is_overdue(today):  # Check overdue
                t.status = "overdue"                     # Mark as overdue
                result.append(t)                         # Add to result list
                changed = True
        if changed:                                      # If any status changed
            self._reindex()
            self.storage.save_transactions(self.transactions)
        return result

    # List all loans for a specific user
    def loans_user(self, user_id: str) -> List[Transaction]:
        return [t for t in self.transactions if t.user_id == user_id]


# -------------------------------
# Reports
# -------------------------------

    # Generate summary report of library
    def report_summary(self) -> Dict[str, int]:
        total_books = len(self.books)                    # Count total books
        total_users = len(self.users)                    # Count total users
        active_loans = sum(1 for t in self.transactions if t.status == "borrowed")
        overdue_loans = sum(1 for t in self.transactions if t.status == "overdue")
        return {
            "total_books": total_books,
            "total_users": total_users,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
        }

    # Get loan history for a specific user
    def report_user_history(self, user_id: str) -> List[Transaction]:
        return self.loans_user(user_id)