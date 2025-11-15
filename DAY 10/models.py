class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies, available_copies):
        self.book_id = book_id
        self.title = title
        self.authors = authors  # list
        self.isbn = isbn
        self.tags = tags  # list
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
        for key, value in kwargs.items():
            setattr(self, key, value)

    def is_available(self):
        return self.available_copies > 0

    def increase_copies(self, n):
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n):
        if n > self.available_copies:
            raise ValueError("Cannot reduce more copies than available.")
        self.total_copies -= n
        self.available_copies -= n


class User:
    def __init__(self, user_id, name, email="", status="active", max_loans=5):
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

    def activate(self):
        self.status = "active"

    def deactivate(self):
        self.status = "inactive"

    def ban(self):
        self.status = "banned"

    def can_borrow(self, active_loans):
        return self.status == "active" and active_loans < self.max_loans


class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date, status):
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
            "return_date": self.return_date,
            "status": self.status
        }

    def mark_returned(self, return_date):
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date):
        from datetime import datetime
        today = datetime.strptime(today_date, "%d-%m-%Y")
        due = datetime.strptime(self.due_date, "%d-%m-%Y")
        return today > due
