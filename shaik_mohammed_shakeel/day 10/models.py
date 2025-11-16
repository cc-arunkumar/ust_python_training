# models.py

from datetime import datetime
from typing import List

# Standard date format used throughout the system
DATE_FMT = "%d-%m-%Y"

# --- Custom Exceptions ---
# These exceptions provide more descriptive error handling in the library system
class InvalidBookError(Exception): pass         # Raised when a book's details are invalid
class InvalidUserError(Exception): pass         # Raised when a user’s details are invalid
class BookNotAvailableError(Exception): pass    # Raised when a book cannot be borrowed
class UserNotAllowedError(Exception): pass      # Raised when a user is not allowed to borrow
class TransactionError(Exception): pass         # Raised for transaction-related issues
class ValidationError(Exception): pass          # Raised for general validation errors


# --- Book Class ---
class Book:
    
    def __init__(
        self,
        book_id: str,
        title: str,
        authors: List[str],
        isbn: str,
        tags: List[str],
        total_copies: int,
        available_copies: int
    ):
        
        # Validation checks
        if not book_id:
            raise ValidationError("Book ID cannot be empty")
        if available_copies > total_copies:
            raise ValidationError("Available copies cannot exceed total copies")
        if len(str(isbn)) > 14:
            raise InvalidBookError("ISBN cannot exceed 14 characters")

        # Assigning attributes
        self.book_id = str(book_id)
        self.title = title
        self.authors = authors or []
        self.isbn = str(isbn)
        self.tags = tags or []
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies)

    # Return a dictionary representation of the book, suitable for storage or JSON.
    def to_dict(self):
        
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),  
            "isbn": self.isbn,
            "tags": "|".join(self.tags),        
            "total_copies": str(self.total_copies),
            "available_copies": str(self.available_copies)
        }

    # Update book details.
    #     Validates changes to ensure data integrity.
    def update(self, **kwargs):
        
        if "title" in kwargs and kwargs["title"] is not None:
            self.title = kwargs["title"]
            
        if "authors" in kwargs and kwargs["authors"] is not None:
            self.authors = kwargs["authors"]

        if "isbn" in kwargs and kwargs["isbn"] is not None:
            if len(str(kwargs["isbn"])) > 14:
                raise InvalidBookError("ISBN cannot exceed 14 characters")
            self.isbn = str(kwargs["isbn"])

        if "tags" in kwargs and kwargs["tags"] is not None:
            self.tags = kwargs["tags"]

        if "total_copies" in kwargs and kwargs["total_copies"] is not None:
            val = int(kwargs["total_copies"])
            if val < self.available_copies:
                raise ValidationError("Total copies cannot be less than available copies")
            self.total_copies = val

        if "available_copies" in kwargs and kwargs["available_copies"] is not None:
            val = int(kwargs["available_copies"])
            if val > self.total_copies:
                raise ValidationError("Available copies cannot exceed total copies")
            self.available_copies = val

    # Check if at least one copy of the book is available to borrow.
    def is_available(self):
        
        return self.available_copies > 0

    # Increase total and available copies by n (default 1).
    def increase_copies(self, n=1):
        
        n = int(n)
        if n <= 0: return
        self.total_copies += n
        self.available_copies += n

    # Decrease total and available copies by n. Raises error if trying to remove more than available.
    def decrease_copies(self, n=1):
        
        n = int(n)
        if n <= 0: return
        if n > self.available_copies:
            raise ValidationError("Cannot decrease more than available copies")
        self.total_copies -= n
        self.available_copies -= n


# --- User Class ---
class User:
    
    def __init__(self, user_id: str, name: str, email: str = "", status: str = "active", max_loans: int = 5):
        if not user_id:
            raise ValidationError("User ID cannot be empty")
        if status not in ["active", "inactive", "banned"]:
            raise ValidationError("Invalid user status")

        self.user_id = str(user_id)
        self.name = name
        self.email = email
        self.status = status
        self.max_loans = int(max_loans)

    # Return a dictionary representation of the user.
    def to_dict(self):
        
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": str(self.max_loans)
        }

    # Status management methods
    def activate(self): self.status = "active"
    def deactivate(self): self.status = "inactive"
    def ban(self): self.status = "banned"

    def can_borrow(self, active_loans_count):
        """Check if user can borrow more books based on status and current active loans."""
        return self.status == "active" and active_loans_count < self.max_loans


# --- Transaction Class ---
class Transaction:

    def __init__(self, tx_id: str, book_id: str, user_id: str, borrow_date: str, due_date: str, return_date: str = None, status: str = "borrowed"):
        self.tx_id = str(tx_id)
        self.book_id = str(book_id)
        self.user_id = str(user_id)
        self.borrow_date = borrow_date  
        self.due_date = due_date        
        self.return_date = return_date
        self.status = status

    # Return a dictionary representation of the transaction.
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

    # Mark the transaction as returned and set the return date.
    def mark_returned(self, return_date: str):
        
        if self.status != "borrowed":
            raise ValidationError("Transaction already returned")
        self.return_date = return_date
        self.status = "returned"

    # Check if the transaction is overdue.
    def is_overdue(self, today_date: str):
    
        try:
            t = datetime.strptime(today_date, DATE_FMT)
            d = datetime.strptime(self.due_date, DATE_FMT)
            return t.date() > d.date()
        except Exception:
            return False
