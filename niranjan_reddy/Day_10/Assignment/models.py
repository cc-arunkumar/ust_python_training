from datetime import timedelta
 
# --- Custom Exceptions ---
class InvalidBookError(Exception):
    pass
 
class InvalidUserError(Exception):
    pass
 
class BookNotAvailableError(Exception):
    pass
 
class UserNotAllowedError(Exception):
    pass
 
class TransactionError(Exception):
    pass
 
class ValidationError(Exception):
    pass
 
 
# --- Book Class ---
class Book:
    def __init__(self, book_id: str, title: str, authors: list, isbn: str, tags: list, total_copies: int, available_copies: int):
        if not book_id:
            raise ValidationError("Book ID cannot be empty")
        if available_copies > total_copies:
            raise ValidationError("Available copies cannot exceed total copies")
        if len(str(isbn)) > 14:
            raise InvalidBookError("ISBN cannot exceed 14 digits")
 
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.isbn = str(isbn)
        self.tags = tags
        self.total_copies = total_copies
        self.available_copies = available_copies
 
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
        for key, value in kwargs.items():
            if key == "book_id":
                self.book_id = value
            elif key == "title":
                self.title = value
            elif key == "authors":
                self.authors = value
            elif key == "isbn":
                if len(str(value)) > 14:
                    raise InvalidBookError("ISBN cannot exceed 14 digits")
                self.isbn = str(value)
            elif key == "tags":
                self.tags = value
            elif key == "total_copies":
                if value < self.available_copies:
                    raise ValidationError("Total copies cannot be less than available copies")
                self.total_copies = value
            elif key == "available_copies":
                if value > self.total_copies:
                    raise ValidationError("Available copies cannot exceed total copies")
                self.available_copies = value
 
    def is_available(self):
        return self.available_copies > 0
 
    def increase_copies(self, n):
        self.total_copies += n
        self.available_copies += n
 
    def decrease_copies(self, n):
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
 
        self.user_id = user_id
        self.name = name
        self.email = email
        self.status = status
        self.max_loans = max_loans
 
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans
        }
 
    def activate(self):
        self.status = "active"
 
    def deactivate(self):
        self.status = "inactive"
 
    def ban(self):
        self.status = "banned"
 
    def can_borrow(self, active_loans):
        return self.status == "active" and active_loans < self.max_loans
 
# --- Transaction Class ---
class Transaction:
    def __init__(self, tx_id: str, book_id: str, user_id: str, borrow_date: str, due_date: str, return_date: str = None, status: str = "borrowed"):
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date  
        self.due_date = due_date        
        self.return_date = return_date
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
            raise ValidationError("Transaction already returned")
        self.return_date = return_date
        self.status = "returned"
 
    def is_overdue(self, today_date):
        today_day, today_month, today_year = map(int, today_date.split('-'))
        due_day, due_month, due_year = map(int, self.due_date.split('-'))
 
        if today_year > due_year:
            return True
        elif today_year < due_year:
            return False
 
        if today_month > due_month:
            return True
        elif today_month < due_month:
            return False
 
        if today_day > due_day:
            return True
        return False
 
 