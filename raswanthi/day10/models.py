
from datetime import datetime

DATE_FMT = "%d-%m-%Y"

class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies, available_copies=None, is_deleted=False):
        self.book_id = book_id
        self.title = title
        self.authors = authors if isinstance(authors, list) else [a.strip() for a in str(authors).split("|") if a.strip()]
        self.isbn = isbn
        self.tags = tags if isinstance(tags, list) else [t.strip() for t in str(tags).split("|") if t.strip()]
        self.total_copies = int(total_copies)
        self.available_copies = int(available_copies) if available_copies is not None else self.total_copies
        self.is_deleted = bool(int(is_deleted)) if isinstance(is_deleted, (int, str)) else bool(is_deleted)

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
            "is_deleted": int(self.is_deleted),
        }

    def is_available(self):
        return not self.is_deleted and self.available_copies > 0

    def increase_copies(self, n):
        if n < 0:
            raise ValueError("Increase must be non-negative")
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n):
        if n < 0:
            raise ValueError("Decrease must be non-negative")
        if self.available_copies >= n:
            self.available_copies -= n
        else:
            raise ValueError("Not enough copies available")


class User:
    def __init__(self, user_id, name, email, status, max_loans=5, active_loans=0, password=""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.status = status.strip().lower()
        self.max_loans = int(max_loans)
        self.active_loans = int(active_loans)
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans,
            "active_loans": self.active_loans,
            "password": self.password,
        }

    def can_borrow(self):
        return self.status == "active" and self.active_loans < self.max_loans

    def increase_active_loans(self):
        self.active_loans += 1

    def decrease_active_loans(self):
        if self.active_loans > 0:
            self.active_loans -= 1

class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed", overdue="0"):
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status
        self.overdue = overdue  

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date or "",
            "status": self.status,
            "overdue": self.overdue,   
        }

# class Transaction:
#     def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
#         self.tx_id = tx_id
#         self.book_id = book_id
#         self.user_id = user_id
#         self.borrow_date = borrow_date
#         self.due_date = due_date
#         self.return_date = return_date
#         self.status = status  # borrowed/returned
        

#     def to_dict(self):
#         return {
#             "tx_id": self.tx_id,
#             "book_id": self.book_id,
#             "user_id": self.user_id,
#             "borrow_date": self.borrow_date,
#             "due_date": self.due_date,
#             "return_date": self.return_date or "",
#             "status": self.status,
#         }

    def mark_returned(self, return_date):
        if self.status == "returned":
            raise ValueError("Already returned")
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date):
        try:
            today = datetime.strptime(today_date, DATE_FMT)
            due = datetime.strptime(self.due_date, DATE_FMT)
            return today > due and self.status != "returned"
        except Exception:
            # If date parsing fails, treat as not overdue
            return False
