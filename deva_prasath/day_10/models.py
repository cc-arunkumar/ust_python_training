from datetime import datetime
from typing import List, Optional


class ValidationError(Exception):
    """Raised for general input validation errors."""
    pass


class InvalidBookError(Exception):
    """Raised when book-related operation fails (not found, duplicate ID/ISBN, etc.)."""
    pass


class InvalidUserError(Exception):
    """Raised when user-related operation fails (not found, duplicate ID, etc.)."""
    pass


class BookNotAvailableError(Exception):
    """Raised when trying to borrow a book with no available copies."""
    pass


class UserNotAllowedError(Exception):
    """Raised when user is inactive, banned, or exceeded max loans."""
    pass


class TransactionError(Exception):
    """Raised for transaction-related errors (not found, already returned, etc.)."""
    pass


class Book:
    """
    Represents a book in the library.
    Supports multiple authors and tags as lists.
    """
    def __init__(
        self,
        book_id: str,
        title: str,
        authors: List[str],
        isbn: str,
        tags: List[str],
        total_copies: int,
        available_copies: Optional[int] = None
    ):
        self.book_id = book_id.strip()
        self.title = title.strip()
        self.authors = [a.strip() for a in authors if a.strip()]
        self.isbn = isbn.strip() if isbn else ""
        self.tags = [t.strip() for t in tags if t.strip()]
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies) if available_copies is not None else self.total_copies

        
        if not self.book_id:
            raise ValidationError("Book ID cannot be empty")
        if self.available_copies > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies")

    def to_dict(self) -> dict:
        """Convert book to dictionary for CSV storage."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": str(self.total_copies),
            "available_copies": str(self.available_copies)
        }

    def update(self, **kwargs):
        """Update book attributes dynamically."""
        for key, value in kwargs.items():
            if key == "authors" and isinstance(value, str):
                self.authors = [a.strip() for a in value.split(",") if a.strip()]
            elif key == "tags" and isinstance(value, str):
                self.tags = [t.strip() for t in value.split(",") if t.strip()]
            elif key == "total_copies":
                new_total = int(value)
                if new_total < self.available_copies:
                    raise ValidationError("Total copies cannot be less than available copies")
                self.total_copies = new_total
            elif key == "available_copies":
                new_avail = int(value)
                if new_avail > self.total_copies:
                    raise ValidationError("Available copies cannot exceed total copies")
                self.available_copies = new_avail
            elif hasattr(self, key):
                setattr(self, key, value)

    def is_available(self) -> bool:
        """Check if at least one copy is available."""
        return self.available_copies > 0

    def increase_copies(self, n: int):
        """Add more copies (increases both total and available)."""
        if n <= 0:
            return
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n: int = 1):
        """Reduce available copies (e.g., during borrow)."""
        if n > self.available_copies:
            raise BookNotAvailableError("Not enough copies available")
        self.available_copies -= n

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """Create Book instance from CSV row dictionary."""
        return Book(
            book_id=data["book_id"],
            title=data["title"],
            authors=data["authors"].split("|") if data["authors"] else [],
            isbn=data["isbn"],
            tags=data["tags"].split("|") if data["tags"] else [],
            total_copies=int(data["total_copies"]),
            available_copies=int(data["available_copies"])
        )


class User:
    """Represents a library user."""
    VALID_STATUSES = {"active", "inactive", "banned"}

    def __init__(
        self,
        user_id: str,
        name: str,
        email: Optional[str] = None,
        status: str = "active",
        max_loans: int = 5
    ):
        self.user_id = user_id.strip()
        self.name = name.strip()
        self.email = email.strip() if email else None
        self.status = status.strip().lower()
        self.max_loans = int(max_loans)

        # Validations
        if not self.user_id:
            raise ValidationError("User ID cannot be empty")
        if self.status not in self.VALID_STATUSES:
            raise ValidationError(f"Invalid status. Must be one of: {', '.join(self.VALID_STATUSES)}")

    def to_dict(self) -> dict:
        """Convert user to dictionary for CSV storage."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email or "",
            "status": self.status,
            "max_loans": str(self.max_loans)
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

    def can_borrow(self, active_loans: int) -> bool:
        """Check if user is allowed to borrow another book."""
        return self.status == "active" and active_loans < self.max_loans

    @staticmethod
    def from_dict(data: dict) -> 'User':
        """Create User instance from CSV row dictionary."""
        return User(
            user_id=data["user_id"],
            name=data["name"],
            email=data["email"] if data["email"] else None,
            status=data["status"],
            max_loans=int(data["max_loans"])
        )


class Transaction:
    """Represents a borrow/return transaction."""
    def __init__(
        self,
        tx_id: str,
        book_id: str,
        user_id: str,
        borrow_date: datetime,
        due_date: str,
        return_date: Optional[datetime] = None,
        status: str = "borrowed"
    ):
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date  # stored as string "DD-MM-YYYY"
        self.return_date = return_date
        self.status = status  # borrowed, returned, overdue

    def to_dict(self) -> dict:
        """Convert transaction to dictionary for CSV storage."""
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date.strftime("%d-%m-%Y"),
            "due_date": self.due_date,
            "return_date": self.return_date.strftime("%d-%m-%Y") if self.return_date else "",
            "status": self.status
        }

    def mark_returned(self, return_date_str: str):
        """Mark transaction as returned."""
        if self.status != "borrowed":
            raise TransactionError("Transaction is not in borrowed state")
        self.return_date = datetime.strptime(return_date_str, "%d-%m-%Y")
        self.status = "returned"

    def is_overdue(self, today_str: str) -> bool:
        """Check if borrowed book is overdue."""
        if self.status != "borrowed":
            return False
        try:
            today = datetime.strptime(today_str, "%d-%m-%Y")
            due = datetime.strptime(self.due_date, "%d-%m-%Y")
            return today > due
        except Exception:
            return False

    @staticmethod
    def from_dict(data: dict) -> 'Transaction':
        """Create Transaction instance from CSV row dictionary."""
        borrow_date = datetime.strptime(data["borrow_date"], "%d-%m-%Y")
        return_date = None
        if data["return_date"]:
            try:
                return_date = datetime.strptime(data["return_date"], "%d-%m-%Y")
            except Exception:
                return_date = None
        return Transaction(
            tx_id=data["tx_id"],
            book_id=data["book_id"],
            user_id=data["user_id"],
            borrow_date=borrow_date,
            due_date=data["due_date"],
            return_date=return_date,
            status=data["status"]
        )