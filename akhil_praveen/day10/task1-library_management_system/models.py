# models.py
from datetime import datetime, timedelta

class InvalidBookError(Exception): pass
class InvalidUserError(Exception): pass
class BookNotAvailableError(Exception): pass
class UserNotAllowedError(Exception): pass
class TransactionError(Exception): pass
class ValidationError(Exception): pass


class Book:
    def __init__(self, book_id, title, authors, isbn, tags,
                 total_copies, available_copies):
        self.book_id = book_id
        self.title = title
        
        # Handle authors - can be string or list
        if isinstance(authors, str):
            self.authors = [a.strip() for a in authors.split("|") if a.strip()] if authors else []
        else:
            self.authors = authors if authors else []
        
        self.isbn = isbn
        
        # Handle tags - can be string or list
        if isinstance(tags, str):
            self.tags = [t.strip() for t in tags.split("|") if t.strip()] if tags else []
        else:
            self.tags = tags if tags else []
        
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies)

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == "authors" and isinstance(value, str):
                self.authors = [a.strip() for a in value.split("|") if a.strip()] if value else []
            elif key == "tags" and isinstance(value, str):
                self.tags = [t.strip() for t in value.split("|") if t.strip()] if value else []
            elif hasattr(self, key) and value is not None:
                setattr(self, key, value)

    def is_available(self):
        return self.available_copies > 0

    def increase_copies(self, n):
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n):
        if self.available_copies - n < 0:
            raise BookNotAvailableError("Not enough available copies")
        self.total_copies -= n
        self.available_copies -= n


class User:
    def __init__(self, user_id, name, email, status="active", max_loans=5):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.status = status
        self.max_loans = int(max_loans)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans
        }

    def activate(self): self.status = "active"
    def deactivate(self): self.status = "inactive"
    def ban(self): self.status = "banned"

    def can_borrow(self, active_loans):
        return self.status == "active" and active_loans < self.max_loans


class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date,
                 due_date, return_date, status):
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date if return_date else None
        self.status = status

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date if self.return_date else "",
            "status": self.status
        }

    def mark_returned(self, return_date):
        if self.status != "borrowed":
            raise TransactionError("Book already returned")
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today):
        if self.status == "returned":
            return False
        try:
            return datetime.strptime(today, "%d-%m-%Y") > \
                   datetime.strptime(self.due_date, "%d-%m-%Y")
        except:
            return False