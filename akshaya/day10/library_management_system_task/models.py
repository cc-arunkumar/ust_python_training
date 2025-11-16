# models.py
from datetime import datetime

DATE_FMT = "%d-%m-%Y"

# ---------------- Custom Exceptions ----------------
class InvalidBookError(Exception): pass
class InvalidUserError(Exception): pass
class BookNotAvailableError(Exception): pass
class UserNotAllowedError(Exception): pass
class TransactionError(Exception): pass
class ValidationError(Exception): pass

# ---------------- BOOK ----------------
class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies, available_copies):
        # authors and tags may arrive as list or pipe/string; normalize
        if not book_id:
            raise ValidationError("Book ID cannot be empty.")
        if not title:
            raise ValidationError("Book title cannot be empty.")
        try:
            total_copies = int(total_copies)
            available_copies = int(available_copies)
        except Exception:
            raise ValidationError("Copies must be integers.")
        if available_copies > total_copies:
            raise ValidationError("Available copies cannot exceed total copies.")

        self.book_id = str(book_id).strip()
        self.title = str(title).strip()
        if isinstance(authors, list):
            self.authors = authors
        else:
            self.authors = [a.strip() for a in str(authors).split("|") if a.strip()]
        self.isbn = str(isbn).strip() if isbn else ""
        if isinstance(tags, list):
            self.tags = tags
        else:
            self.tags = [t.strip() for t in str(tags).split("|") if t.strip()]
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.is_removed = False  # New attribute to track if the book is soft-deleted

    def to_dict(self):
        # Exclude 'is_removed' from being saved to CSV
        data = {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": str(self.total_copies),
            "available_copies": str(self.available_copies),
        }
        return data

    def update(self, **kwargs):
        if "title" in kwargs:
            self.title = kwargs["title"]
        if "authors" in kwargs:
            self.authors = kwargs["authors"]
        if "isbn" in kwargs:
            self.isbn = kwargs["isbn"]
        if "tags" in kwargs:
            self.tags = kwargs["tags"]
        if "total_copies" in kwargs:
            tc = int(kwargs["total_copies"])
            if tc < self.available_copies:
                raise ValidationError("Total copies cannot be less than available copies.")
            self.total_copies = tc
        if "available_copies" in kwargs:
            ac = int(kwargs["available_copies"])
            if ac > self.total_copies:
                raise ValidationError("Available copies cannot exceed total copies.")
            self.available_copies = ac
        return self

    def is_available(self):
        return self.title != "DELETED" and self.available_copies > 0

    def decrease_copies(self, n=1):
        if self.available_copies < n:
            raise BookNotAvailableError("No available copies.")
        self.available_copies -= n

    def increase_copies(self, n=1):
        if self.available_copies + n > self.total_copies:
            self.available_copies = self.total_copies
        else:
            self.available_copies += n

    def soft_delete(self):
        self.is_removed = True
        self.title = "DELETED"
        self.available_copies = 0
        self.authors = []
        self.tags = []
        self.isbn = ""

# ---------------- USER ----------------
class User:
    def __init__(self, user_id, name, email="", status="active", max_loans=5):
        if not user_id:
            raise ValidationError("User ID cannot be empty.")
        if status not in {"active", "inactive", "banned"}:
            raise ValidationError("Invalid user status.")
        self.user_id = str(user_id).strip()
        self.name = str(name).strip()
        self.email = str(email).strip()
        self.status = status
        self.max_loans = int(max_loans)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": str(self.max_loans)
        }

    def update(self, **kwargs):
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "email" in kwargs:
            self.email = kwargs["email"]
        if "status" in kwargs:
            if kwargs["status"] not in {"active","inactive","banned"}:
                raise ValidationError("Invalid status value.")
            self.status = kwargs["status"]
        if "max_loans" in kwargs:
            self.max_loans = int(kwargs["max_loans"])
        return self

    def activate(self):
        self.status = "active"

    def deactivate(self):
        self.status = "inactive"

    def ban(self):
        self.status = "banned"

    def can_borrow(self, active_loans):
        if self.status != "active":
            raise UserNotAllowedError("User is not active.")
        if active_loans >= self.max_loans:
            raise UserNotAllowedError("User has reached max loans.")
        return True

# ---------------- TRANSACTION ----------------
class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
        if not tx_id:
            raise ValidationError("Transaction ID cannot be empty.")
        self.tx_id = str(tx_id)
        self.book_id = str(book_id)
        self.user_id = str(user_id)
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date or ""
        self.status = status

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "status": self.status
        }

    def mark_returned(self, return_date):
        if self.status != "borrowed":
            raise TransactionError("Transaction is not in 'borrowed' state; can't return again.")
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date):
        if self.status != "borrowed":
            return False
        try:
            today = datetime.strptime(today_date, DATE_FMT)
            due = datetime.strptime(self.due_date, DATE_FMT)
            return today > due
        except Exception:
            return False
