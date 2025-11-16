from datetime import datetime

# ---------------- Custom Exceptions ----------------
class InvalidBookError(Exception): pass
class InvalidUserError(Exception): pass
class BookNotAvailableError(Exception): pass
class UserNotAllowedError(Exception): pass
class TransactionError(Exception): pass
class ValidationError(Exception): pass

DATE_FMT = "%d-%m-%Y"

# ---------------- BOOK ----------------
class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies, available_copies):
        if not book_id:
            raise ValidationError("Book ID cannot be empty.")
        if not title:
            raise ValidationError("Book title cannot be empty.")
        if int(available_copies) > int(total_copies):
            raise ValidationError("Available copies cannot exceed total copies.")

        self.book_id = book_id.strip()
        self.title = title.strip()
        self.authors = authors or []
        self.isbn = isbn.strip() if isbn else ""
        self.tags = tags or []
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
            "available_copies": self.available_copies
        }

    def update(self, **kwargs):
        if "available_copies" in kwargs and kwargs["available_copies"] > self.total_copies:
            raise ValidationError("Available copies cannot exceed total copies.")
        if "total_copies" in kwargs and kwargs["total_copies"] < self.available_copies:
            raise ValidationError("Total copies cannot be less than available copies.")

        for k, v in kwargs.items():
            setattr(self, k, v)

        return self

    def is_available(self):
        return self.available_copies > 0

    def increase_copies(self, n=1):
        if self.available_copies + n > self.total_copies:
            raise ValidationError("Available copies exceed total.")
        self.available_copies += n

    def decrease_copies(self, n=1):
        if self.available_copies < n:
            raise BookNotAvailableError("No available copies.")
        self.available_copies -= n


# ---------------- USER ----------------
class User:
    def __init__(self, user_id, name, email="", status="active", max_loans=5):
        if not user_id:
            raise ValidationError("User ID cannot be empty.")
        if status not in {"active", "inactive", "banned"}:
            raise ValidationError("Invalid user status.")

        self.user_id = user_id.strip()
        self.name = name.strip()
        self.email = email.strip()
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

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return self

    def activate(self):
        self.status = "active"

    def deactivate(self):
        self.status = "inactive"

    def ban(self):
        self.status = "banned"

    def can_borrow(self, active_loans):
        if self.status != "active":
            raise UserNotAllowedError("User not active.")
        if active_loans >= self.max_loans:
            raise UserNotAllowedError("Loan limit reached.")
        return True


# ---------------- TRANSACTION ----------------
class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
        if not tx_id:
            raise ValidationError("Transaction ID empty.")
        if status not in {"borrowed", "returned", "overdue"}:
            status = "borrowed"

        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
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
            raise TransactionError("Transaction is not borrowed.")
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
