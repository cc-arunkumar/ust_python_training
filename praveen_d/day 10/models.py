from datetime import datetime

# ---------------- Custom Exceptions ----------------
# These are specific error types used throughout the system
# to make error handling more meaningful and user-friendly.
class InvalidBookError(Exception): pass          # Raised when a book is not found or invalid
class InvalidUserError(Exception): pass          # Raised when a user is not found or invalid
class BookNotAvailableError(Exception): pass     # Raised when a book cannot be borrowed/removed
class UserNotAllowedError(Exception): pass       # Raised when a user is not allowed to borrow
class TransactionError(Exception): pass          # Raised when a transaction is invalid
class ValidationError(Exception): pass           # Raised for general validation issues

# Date format used consistently across the system
DATE_FMT = "%d-%m-%Y"

# ---------------- Book ----------------
class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies, available_copies):
        if not book_id:
            raise ValidationError("Book ID cannot be empty.")
        if not title:
            raise ValidationError("Book title cannot be empty.")
        if available_copies > total_copies:
            raise ValidationError("Available copies cannot exceed total copies.")

        # Assign attributes
        self.book_id = book_id.strip()
        self.title = title.strip()
        self.authors = [a.strip() for a in authors] if authors else []
        self.isbn = isbn.strip() if isbn else ""
        self.tags = [t.strip() for t in tags] if tags else []
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies)

    def to_dict(self):
        """Convert book object into a dictionary for saving to CSV."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }

    def update(self, **kwargs):
        """Update book attributes safely, validating copy counts."""
        if "available_copies" in kwargs and kwargs["available_copies"] > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies.")
        for key, value in kwargs.items():
            setattr(self, key, value)

    def is_available(self):
        """Check if at least one copy is available to borrow."""
        return self.available_copies > 0

    def increase_copies(self, n=1):
        """Increase available copies, ensuring it does not exceed total copies."""
        self.available_copies += n
        if self.available_copies > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies.")

    def decrease_copies(self, n=1):
        """Decrease available copies, ensuring it does not go below zero."""
        if self.available_copies < n:
            raise BookNotAvailableError("Not enough copies available to decrease.")
        self.available_copies -= n


# ---------------- User ----------------
class User:
    def __init__(self, user_id, name, email="", status="active", max_loans=5):
        """
        Represents a library user.
        Validates ID, name, and status when creating a new user.
        """
        if not user_id:
            raise ValidationError("User ID cannot be empty.")
        if not name:
            raise ValidationError("User name cannot be empty.")
        if status not in {"active", "inactive", "banned"}:
            raise ValidationError("Invalid user status.")

        # Assign attributes
        self.user_id = user_id.strip()
        self.name = name.strip()
        self.email = email.strip()
        self.status = status
        self.max_loans = int(max_loans)

    def to_dict(self):
        """Convert user object into a dictionary for saving to CSV."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans
        }

    def activate(self):
        """Set user status to active."""
        self.status = "active"

    def deactivate(self):
        """Set user status to inactive."""
        self.status = "inactive"

    def ban(self):
        """Set user status to banned."""
        self.status = "banned"

    def can_borrow(self, active_loans):
        """
        Check if user can borrow a book.
        Raises UserNotAllowedError if status is not active or loan limit reached.
        """
        if self.status != "active":
            raise UserNotAllowedError("Inactive or banned users cannot borrow.")
        if active_loans >= self.max_loans:
            raise UserNotAllowedError("User has reached maximum loan limit.")
        return True


# ---------------- Transaction ----------------
class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
        if not tx_id:
            raise ValidationError("Transaction ID cannot be empty.")
        if not book_id or not user_id:
            raise ValidationError("Transaction must have valid book_id and user_id.")
        if status not in {"borrowed", "returned", "overdue"}:
            raise ValidationError("Invalid transaction status.")

        # Assign attributes
        self.tx_id = tx_id.strip()
        self.book_id = book_id.strip()
        self.user_id = user_id.strip()
        self.borrow_date = borrow_date.strip()
        self.due_date = due_date.strip()
        self.return_date = return_date.strip() if return_date else None
        self.status = status

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date or "",
            "status": self.status
        }

    def mark_returned(self, return_date):
        if self.status != "borrowed":
            raise TransactionError("Transaction is not in borrowed state.")
        self.return_date = return_date.strip()
        self.status = "returned"

    def is_overdue(self, today_date):
        """
        Check if transaction is overdue.
        Returns True if today > due_date and status is still borrowed.
        """
        if self.status != "borrowed":
            return False
        try:
            today = datetime.strptime(today_date, DATE_FMT)
            due = datetime.strptime(self.due_date, DATE_FMT)
            return today > due
        except Exception:
            raise ValidationError("Invalid date format for overdue check.")
