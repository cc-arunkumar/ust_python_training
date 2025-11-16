from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, authors, isbn, tags, total_copies):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.tags = tags
        self.total_copies = total_copies
        self.available_copies = total_copies

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

    def update(self, title=None, authors=None, isbn=None, tags=None, total_copies=None):
        if title:
            self.title = title
        if authors:
            self.authors = authors
        if isbn:
            self.isbn = isbn
        if tags:
            self.tags = tags
        if total_copies is not None:  # total_copies can be 0 or a positive number
            self.total_copies = total_copies
            self.available_copies = total_copies  # Reset available copies to the total number of copies

    def is_available(self):
        return self.available_copies > 0

    def increase_copies(self, n):
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n):
        if self.available_copies - n < 0:
            raise ValueError("Cannot decrease copies below 0.")
        self.available_copies -= n


class User:
    def __init__(self, user_id, name, email, status, max_loans=5, password=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.status = status
        self.max_loans = int(max_loans)  # Ensure max_loans is an integer
        self.active_loans = 0  # Initialize active_loans to 0
        self.password = password  # Store password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans,
            "password": self.password  # Add password field to dictionary
        }

    def can_borrow(self):
        return self.status == "active" and self.active_loans < self.max_loans

    def activate(self):
        self.status = "active"

    def deactivate(self):
        self.status = "inactive"

    def ban(self):
        self.status = "banned"
    
    def increase_active_loans(self):
        self.active_loans += 1
    
    def decrease_active_loans(self):
        self.active_loans -= 1

    # Update password
    def update_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password. Password update failed.")

class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
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
            "return_date": self.return_date or "",  
            "status": self.status
        }

    def mark_returned(self, return_date):
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date):
        """
        Check if the transaction is overdue.
        - today_date: today's date in string format ('YYYY-MM-DD' or 'DD-MM-YYYY')
        """
        # Try parsing the today_date string
        try:
            today = datetime.strptime(today_date, '%d-%m-%Y')  # Try with day-first format
        except ValueError:
            today = datetime.strptime(today_date, '%Y-%m-%d')  # Try with year-first format
            
        try:
            due = datetime.strptime(self.due_date, '%d-%m-%Y')  # Try with day-first format
        except ValueError:
            due = datetime.strptime(self.due_date, '%Y-%m-%d')  # Try with year-first format
        
        return today > due and self.status != "returned"