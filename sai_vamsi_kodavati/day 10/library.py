# library.py
import os
from datetime import datetime, timedelta
from models import *
from storage import CSVStorage

# Standard date format used across the LMS
DATE_FMT = "%d-%m-%Y"

# Utility function to get today's date as a string
def today():
    return datetime.today().strftime(DATE_FMT)

# Utility function to add a certain number of days to a date string
def add_days(date_str, days):
    base = datetime.strptime(date_str, DATE_FMT)
    return (base + timedelta(days=days)).strftime(DATE_FMT)


class Library:
    
    # Library class manages books, users, and transactions.
    # Supports add/update/remove/list/search for books and users,
    # borrow/return operations, and reporting.
    

    def __init__(self, storage: CSVStorage = None):
        
        # Initializes the library with optional CSVStorage.
        # Loads books, users, and transactions from storage.
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if storage:
            self.storage = storage
        else:
            # Default CSV storage paths
            self.storage = CSVStorage(
                books_path="data/books.csv",
                users_path="data/users.csv",
                transactions_path="data/transactions.csv"
            )

        # Load data from storage
        self.books = self.storage.load_books()
        self.users = self.storage.load_users()
        self.transactions = self.storage.load_transactions()

    # ---------------- Book operations ----------------
    def add_book(self, book: Book):
        
        # Adds a new book to the library.
        # Raises error if book_id or ISBN already exists.
        
        if self.get_book(book.book_id):
            raise InvalidBookError("Book ID already exists.")
        for b in self.books:
            if b.isbn == book.isbn:
                raise ValidationError("ISBN already exists.")
        self.books.append(book)
        return book

    def update_book(self, book_id, **kwargs):
        
        # Updates attributes of an existing book.
        
        book = self.get_book(book_id)
        if not book:
            raise InvalidBookError("Book not found.")
        book.update(**kwargs)
        return book

    def remove_book(self, book_id):
        
        # Removes a book from library if it's not currently borrowed.
        
        book = self.get_book(book_id)
        if not book:
            raise InvalidBookError("Book not found.")
        for tx in self.transactions:
            if tx.book_id == book_id and tx.status == "borrowed":
                raise InvalidBookError("Book is currently borrowed.")
        self.books.remove(book)
        return True

    def get_book(self, book_id):
        
        # Returns a book object by its ID, or None if not found.
        
        for b in self.books:
            if b.book_id == str(book_id):
                return b
        return None
    
    # Returns a list of all books.
    def list_books(self):
        
        

        return self.books

    # Returns books where the title contains the search text.Case-insensitive.
    def search_books_by_title(self, text):
        
        s = text.lower()
        return [b for b in self.books if s in (b.title or "").lower()]

    def search_books_by_author(self, text):
        
        # Returns books where any author's name contains the search text.
        # Case-insensitive.
      
        s = text.lower()
        return [b for b in self.books if any(s in a.lower() for a in b.authors)]

    def search_books_by_tag(self, text):
        
        # Returns books where any tag contains the search text.
        # Case-insensitive.
        
        s = text.lower()
        return [b for b in self.books if any(s in t.lower() for t in b.tags)]

    # ---------------- User operations ----------------
    def add_user(self, user: User):
        
        # Adds a new user to the library.
        # Raises error if user_id already exists.
        
        if self.get_user(user.user_id):
            raise InvalidUserError("User ID already exists.")
        self.users.append(user)
        return user

    def update_user(self, user_id, **kwargs):
        
        # Updates attributes of an existing user.
        # Directly sets allowed attributes (name, email, status, max_loans).
        
        user = self.get_user(user_id)
        if not user:
            raise InvalidUserError("User not found.")
        # Placeholder to bypass model update method
        user.update = lambda **k: None
        if "name" in kwargs and kwargs["name"] is not None:
            user.name = kwargs["name"]
        if "email" in kwargs and kwargs["email"] is not None:
            user.email = kwargs["email"]
        if "status" in kwargs and kwargs["status"] is not None:
            user.status = kwargs["status"]
        if "max_loans" in kwargs and kwargs["max_loans"] is not None:
            user.max_loans = int(kwargs["max_loans"])
        return user

    # Returns a user object by user_id, or None if not found.
    def get_user(self, user_id):
        
        
        
        for u in self.users:
            if u.user_id == str(user_id):
                return u
        return None

    # Returns a list of all users.
    def list_users(self):
        return self.users

    # Sets a user's status to active.
    def activate_user(self, user_id):
        u = self.get_user(user_id)
        if not u: raise InvalidUserError("User not found.")
        u.activate()
    
    # Sets a user's status to inactive.
    def deactivate_user(self, user_id):
        
        u = self.get_user(user_id)
        if not u: raise InvalidUserError("User not found.")
        u.deactivate()

    # Bans a user from borrowing books.
    def ban_user(self, user_id):
        u = self.get_user(user_id)
        if not u: raise InvalidUserError("User not found.")
        u.ban()

    # ---------------- Borrow / Return ----------------
    def borrow_book(self, user_id, book_id, days=14):
        user = self.get_user(user_id)
        if not user:
            raise InvalidUserError("User does not exist.")
        book = self.get_book(book_id)
        if not book:
            raise InvalidBookError("Book does not exist.")
        if user.status != "active":
            raise UserNotAllowedError("User is not allowed to borrow.")
        if not book.is_available():
            raise BookNotAvailableError("Book is not available.")

        active_loans = [tx for tx in self.transactions if tx.user_id == user.user_id and tx.status == "borrowed"]
        if len(active_loans) >= user.max_loans:
            raise UserNotAllowedError("User reached maximum loan limit.")

        tx_id = f"T{len(self.transactions) + 1}"
        borrow_date = today()
        due_date = add_days(borrow_date, days)
        tx = Transaction(tx_id, book.book_id, user.user_id, borrow_date, due_date, None, "borrowed")

        # Decrease available copies of the book
        book.decrease_copies(1)
        self.transactions.append(tx)
        return tx, due_date


    # Processes returning a borrowed book by transaction ID.
    #     Updates book copies and transaction status.
    def return_book(self, transaction_id):
        tx = next((t for t in self.transactions if t.tx_id == str(transaction_id)), None)
        if not tx:
            raise TransactionError("Transaction not found.")
        if tx.status != "borrowed":
            raise TransactionError("Book already returned.")
        book = self.get_book(tx.book_id)
        if not book:
            raise InvalidBookError("Book not found.")
        book.increase_copies(1)
        tx.mark_returned(today())
        return tx

    # ---------------- Reports ----------------
    def get_active_loans(self):
    
        return [tx for tx in self.transactions if tx.status == "borrowed"]

    # Returns a list of all overdue loans based on today's date.
    def get_overdue_loans(self, today_date=None):
        td = today_date or today()
        return [tx for tx in self.transactions if tx.is_overdue(td)]

    # Returns all transactions for a specific user.
    def get_user_loans(self, user_id):
        return [tx for tx in self.transactions if tx.user_id == str(user_id)]

    # Returns summary statistics: total books, users, active loans, overdue loans.
    def summary_report(self):
        return len(self.books), len(self.users), len(self.get_active_loans()), len(self.get_overdue_loans())

    # ---------------- Persistence ----------------
    def save_all(self):
        self.storage.save_books(self.books)
        self.storage.save_users(self.users)
        self.storage.save_transactions(self.transactions)
