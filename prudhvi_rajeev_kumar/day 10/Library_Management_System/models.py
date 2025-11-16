from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime

DATE_FMT = "%d-%m-%Y"

# Custom exceptions (business validations)
class InvalidBookError(Exception): pass
class InvalidUserError(Exception): pass
class BookNotAvailableError(Exception): pass
class UserNotAllowedError(Exception): pass
class TransactionError(Exception): pass
class ValidationError(Exception): pass


def parse_list_field(value: str) -> List[str]:
    if not value:
        return []
    return [p.strip() for p in value.split("|") if p.strip()]


def join_list_field(items: List[str]) -> str:
    return "|".join([i.strip() for i in items if i and i.strip()])


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
        for key, val in kwargs.items():
            if key in {"authors", "tags"} and isinstance(val, str):
                # Allow CLI to pass comma-separated strings; convert to list
                setattr(self, key, [v.strip() for v in val.split(",") if v.strip()])
            elif hasattr(self, key):
                setattr(self, key, val)
        if self.available_copies > self.total_copies:
            raise ValidationError("available_copies cannot exceed total_copies")

    def is_available(self) -> bool:
        return self.available_copies > 0


@dataclass
class User:
    user_id: str
    name: str
    email: Optional[str]
    status: str = "active"
    max_loans: int = 5

    def to_dict(self) -> Dict[str, str]:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email or "",
            "status": self.status,
            "max_loans": str(self.max_loans),
        }

    def activate(self): self.status = "active"
    def deactivate(self): self.status = "inactive"
    def ban(self): self.status = "banned"

    def can_borrow(self, active_loans: int) -> bool:
        return self.status == "active" and active_loans < self.max_loans


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
        # Allow returning even if overdue
        if self.status not in {"borrowed", "overdue"}:
            raise TransactionError("Transaction is not in a returnable state")
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date: str) -> bool:
        if self.status == "returned":
            return False
        try:
            due = datetime.strptime(self.due_date, DATE_FMT).date()
            today = datetime.strptime(today_date, DATE_FMT).date()
            return today > due
        except Exception:
            return False
