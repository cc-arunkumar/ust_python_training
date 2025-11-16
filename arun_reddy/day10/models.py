"""
This file contains the data models (classes) for the Library Management System.
Models are like templates that define what properties and methods each entity has.
"""

from datetime import datetime, timedelta


class Book:
    """
    Represents a book in the library.
    
    Attributes:
        book_id: Unique identifier for the book
        title: Name of the book
        authors: List of people who wrote the book
        isbn: ISBN number of the book
        tags: Tags/categories for the book
        total_copies: Total number of copies in the library
        available_copies: Number of copies available right now
    """
    
    def __init__(self, book_id, title, authors, isbn, tags, total_copies):
        """Initialize a new book with given details."""
        self.book_id = book_id
        self.title = title
        # If authors is a string, split it by comma; otherwise keep as is (already a list)
        self.authors = authors.split(",") if isinstance(authors, str) else authors
        self.isbn = isbn
        # Same as authors - convert string to list if needed
        self.tags = tags.split(",") if isinstance(tags, str) else tags
        self.total_copies = int(total_copies)
        # When a book is added, all copies are available
        self.available_copies = self.total_copies
        
    def __str__(self):
        """Return a nice text representation of the book."""
        return f"{self.book_id}: {self.title} by {', '.join(self.authors)} | Available: {self.available_copies}/{self.total_copies}"
    
    def to_dict(self):
        """Convert book object to a dictionary (useful for saving to CSV)."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "authors": "|".join(self.authors),
            "isbn": self.isbn,
            "tags": "|".join(self.tags),
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }

    def is_available(self):
        """Check if this book has at least one copy available to borrow."""
        return self.available_copies > 0

    def increase_copies(self, n):
        """Add more copies to the library (called when a book is returned)."""
        self.total_copies += n
        self.available_copies += n

    def decrease_copies(self, n):
        """Remove copies from the library (called when a book is borrowed)."""
        if self.available_copies >= n:
            self.available_copies -= n
        else:
            raise ValueError(f"Cannot decrease copies below 0. Available copies: {self.available_copies}")


class User:
    """
    Represents a library user/member.
    
    Attributes:
        user_id: Unique identifier for the user
        name: User's full name
        email: User's email address (must end with @ust.com)
        status: Current status (active, inactive, or banned)
        max_loans: Maximum number of books this user can borrow at once
        active_loans: Current number of books this user has borrowed
    """
    
    def __init__(self, user_id, name, email, status, max_loans=5):
        """Initialize a new user with given details."""
        self.user_id = user_id
        self.name = name
        self.email = email
        self.status = status
        self.max_loans = int(max_loans)  # Ensure max_loans is a whole number
        self.active_loans = 0  # Start with no borrowed books
        
    def __str__(self):
        """Return a nice text representation of the user."""
        return f"{self.user_id}: {self.name} ({self.status}) | Loans: {self.active_loans}/{self.max_loans}"
    
    def to_dict(self):
        """Convert user object to a dictionary (useful for saving to CSV)."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "max_loans": self.max_loans
        }

    def can_borrow(self):
        """Check if this user is allowed to borrow a book."""
        # User must be active AND not have reached their borrowing limit
        return self.status == "active" and self.active_loans < self.max_loans

    def activate(self):
        """Change user status to active."""
        self.status = "active"

    def deactivate(self):
        """Change user status to inactive."""
        self.status = "inactive"

    def ban(self):
        """Change user status to banned."""
        self.status = "banned"
    
    def increase_active_loans(self):
        """Add 1 to the user's current loan count (when they borrow a book)."""
        self.active_loans += 1
    
    def decrease_active_loans(self):
        """Subtract 1 from the user's current loan count (when they return a book)."""
        self.active_loans -= 1


class Transaction:
    """
    Represents a book borrowing transaction.
    
    Attributes:
        tx_id: Unique transaction identifier
        book_id: Which book was borrowed
        user_id: Which user borrowed it
        borrow_date: Date the book was borrowed
        due_date: Date the book should be returned by
        return_date: Date the book was actually returned (None if not returned yet)
        status: Current status (borrowed or returned)
    """
    
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status="borrowed"):
        """Initialize a new transaction."""
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status

    def to_dict(self):
        """Convert transaction object to a dictionary (useful for saving to CSV)."""
        return {
            "tx_id": self.tx_id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date if self.return_date else '',
            "status": self.status
        }

    def mark_returned(self, return_date):
        """Mark this book as returned with the return date."""
        self.return_date = return_date
        self.status = "returned"

    def is_overdue(self, today_date):
        """Check if this book is overdue (not returned by the due date)."""
        today = datetime.strptime(today_date, '%d-%m-%Y')
        due = datetime.strptime(self.due_date, '%d-%m-%Y')
        return today > due and self.status != "returned"
