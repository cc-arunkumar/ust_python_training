from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime

# Date format used for borrow/due/return dates
DATE_FMT = "%d-%m-%Y"

# -------------------------------
# Custom exceptions (business validations)
# -------------------------------
class InvalidBookError(Exception): pass          # Raised when book ID or details are invalid
class InvalidUserError(Exception): pass          # Raised when user ID or details are invalid
class BookNotAvailableError(Exception): pass     # Raised when a book is not available to borrow
class UserNotAllowedError(Exception): pass       # Raised when user is not allowed to borrow
class TransactionError(Exception): pass          # Raised when transaction is invalid
class ValidationError(Exception): pass           # Raised when validation rules fail
class AuthFailed(Exception): pass                # Raised when authentication fails

# -------------------------------
# Utility functions for parsing/joining list fields
# -------------------------------
def parse_list_field(value: str) -> List[str]:
    # Convert a string with "|" separators into a list of strings
    if not value:
        return []
    return [p.strip() for p in value.split("|") if p.strip()]

def join_list_field(items: List[str]) -> str:
    # Convert a list of strings into a "|" separated string
    return "|".join([i.strip() for i in items if i and i.strip()])

# -------------------------------
# Book dataclass
# -------------------------------
@dataclass
class Book:
    book_id: str
    title: str
    authors: List[str]
    isbn: str
    tags: List[str]
    total_copies: int
    available_copies: int

    def to_dict(self) -> Dict[str, str]:
        # Convert Book object into dictionary for CSV storage
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": join_list_field(self.authors),
            "isbn": self.isbn,
            "tags": join_list_field(self.tags),
            "total_copies": str(self.total_copies),
            "available_copies": str(self.available_copies),
        }

    def update(self, **kwargs):
        # Update book attributes dynamically
        for key, val in kwargs.items():
            if key in {"authors", "tags"} and isinstance(val, str):
                # Allow CLI to pass comma-separated strings; convert to list
                setattr(self, key, [v.strip() for v in val.split(",") if v.strip()])
            elif hasattr(self, key):
                setattr(self, key, val)
        # Validation: available copies cannot exceed total copies
        if self.available_copies > self.total_copies:
            raise ValidationError("available_copies cannot exceed total_copies")

    def is_available(self) -> bool:
        # Check if book has at least one available copy
        return self.available_copies > 0

# -------------------------------
# User dataclass
# -------------------------------
@dataclass
class User:
    user_id: str
    name: str
    email: Optional[str]
    status: str = "active"       # Default status is active
    max_loans: int = 5           # Default max loans
    password: Optional[str] = None

    def to_dict(self) -> Dict[str, str]:
        # Convert User object into dictionary for CSV storage
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email or "",
            "status": self.status,
            "max_loans": str(self.max_loans),
            "password": self.password or self.user_id or "",
        }

    # Methods to change user status
    def activate(self): self.status = "active"
    def deactivate(self): self.status = "inactive"
    def ban(self): self.status = "banned"

    def can_borrow(self, active_loans: int) -> bool:
        # Check if user can borrow more books
        return self.status == "active" and active_loans < self.max_loans

# -------------------------------
# Transaction dataclass
# -------------------------------
@dataclass
class Transaction:
    tx_id: str
    book_id: str
    user_id: str
    borrow_date: str  # DD-MM-YYYY
    due_date: str     # DD-MM-YYYY
    return_date: Optional[str] = None
    status: str = "borrowed"  # borrowed, returned, overdue

    def to_dict(self) -> Dict[str, str]:
        # Convert Transaction object into dictionary for CSV storage
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date or "",
            "status": self.status,
        }

    def mark_returned(self, return_date: str):
        # Mark transaction as returned (even if overdue)
        if self.status not in {"borrowed", "overdue"}:
            raise TransactionError("Transaction is not in a returnable state")
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date: str) -> bool:
        # Check if transaction is overdue compared to today's date
        if self.status == "returned":
            return False
        try:
            due = datetime.strptime(self.due_date, DATE_FMT).date()
            today = datetime.strptime(today_date, DATE_FMT).date()
            return today > due
        except Exception:
            return False