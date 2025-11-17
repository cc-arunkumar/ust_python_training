# Library Management System (LMS) - Main Application
# This is the main file that runs the library management system
# It provides a menu-driven interface for users to manage books, users, and transactions

import sys
from storage import CSVStorage
from models import Book, User, Transaction
from datetime import datetime, timedelta

# Initialize the storage system that handles CSV files
storage = CSVStorage()

# ================== BOOK SERVICES ==================
# These functions handle all book-related operations

def add_book():
    """Add a new book to the library."""
    print("\n--- Add a New Book ---")
    books = storage.load_books()
    
    # Get Book ID from user
    book_id = input("Enter Book ID: ").strip()
    
    # Check if book ID already exists
    existing = next((b for b in books if b.book_id == book_id), None)
    if existing:
        print("Book ID already exists. Please use a different ID.\n")
        return
    
    # Get Title
    title = input("Enter Title: ").strip()
    if not title:
        print("Title cannot be empty.\n")
        return
    
    # Get Authors (can be multiple, separated by comma)
    authors = input("Enter Authors (comma separated): ")
    
    # Get ISBN
    isbn = input("Enter ISBN: ")
    
    # Get Tags (can be multiple, separated by comma)
    tags = input("Enter Tags (comma separated): ")
    
    # Get Total Copies (must be a positive number)
    try:
        total_copies = int(input("Enter Total Copies: "))
        if total_copies <= 0:
            print("Total copies must be a positive number.\n")
            return
    except ValueError:
        print("Total copies must be a positive integer.\n")
        return
    
    # Create new book object and save it
    book = Book(book_id, title, authors, isbn, tags, total_copies)
    books.append(book)
    storage.save_books(books)
    print("✓ Book added successfully.\n")

def list_books():
    """Display all books in the library."""
    print("\n--- Book List ---")
    books = storage.load_books()
    if not books:
        print("No books found.\n")
    else:
        # Print each book with nice formatting
        for book in books:
            print(book)
        print()

def update_book(book_id=None):
    """Update an existing book's information."""
    print("\n--- Update a Book ---")
    books = storage.load_books()
    
    # Get the book ID if not provided
    if book_id is None:
        book_id = input("Enter Book ID to update: ").strip()
    
    # Find the book
    book = next((b for b in books if b.book_id == book_id), None)
    if not book:
        print("Book not found.\n")
        return
    
    # Show message that empty fields will keep current value
    print("Leave field empty to keep current value.")
    
    # Update Title
    title = input(f"Enter Title [{book.title}]: ").strip() or book.title
    if not title:
        print("Title cannot be empty.\n")
        return
    
    # Update Authors
    authors = input(f"Enter Authors (comma separated) [{book.authors}]: ") or book.authors
    
    # Update ISBN
    isbn = input(f"Enter ISBN [{book.isbn}]: ") or book.isbn
    
    # Update Tags
    tags = input(f"Enter Tags (comma separated) [{book.tags}]: ") or book.tags
    
    # Update Total Copies
    total_copies_input = input(f"Enter Total Copies [{getattr(book, 'total_copies', '')}]: ")
    if total_copies_input.strip():
        try:
            total_copies = int(total_copies_input)
            if total_copies <= 0:
                print("Total copies must be a positive number.\n")
                return
            book.total_copies = total_copies
        except ValueError:
            print("Invalid number for total copies. Keeping existing value.")
    
    # Apply changes
    book.title = title
    book.authors = authors
    book.isbn = isbn
    book.tags = tags
    
    storage.save_books(books)
    print("✓ Book updated successfully.\n")

def remove_book():
    """Remove a book from the library."""
    print("\n--- Remove a Book ---")
    book_id = input("Enter Book ID to remove: ")
    books = storage.load_books()
    
    # Find the book
    book = next((b for b in books if b.book_id == book_id), None)
    if not book:
        print("Book not found.\n")
        return
    
    # Ask for confirmation before deleting
    confirm = input(f"Are you sure you want to remove '{book.title}'? (y/n): ").strip().lower()
    if confirm == 'y':
        books = [b for b in books if b.book_id != book_id]
        storage.save_books(books)
        print("✓ Book removed successfully.\n")
    else:
        print("Operation cancelled.\n")

def book_services():
    """Show book services menu and handle user choices."""
    while True:
        print("\n=== Book Services ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Remove Book")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.\n")

# ================== USER SERVICES ==================
# These functions handle all user-related operations

def add_user():
    """Add a new user to the library system."""
    print("\n--- Add a New User ---")
    users = storage.load_users()
    
    # Get User ID
    user_id = input("Enter User ID: ").strip()
    
    # Check if user ID already exists
    existing = next((u for u in users if u.user_id == user_id), None)
    if existing:
        print("User ID already exists. Please use a different ID.\n")
        return
    
    # Get Name
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.\n")
        return
    
    # Get Email
    email = input("Enter Email: ").strip()
    # Email must end with @ust.com for company library
    if not email.endswith("@ust.com"):
        print("❌ Email must end with @ust.com.\n")
        return
    
    # Get Status
    status = input("Enter Status (active/inactive/banned): ").strip().lower()
    if status not in ["active", "inactive", "banned"]:
        print("❌ Status must be one of: active, inactive, banned.\n")
        return
    
    # Get Max Loans (must be a positive number)
    try:
        max_loans = int(input("Enter Max Loans (books they can borrow at once): "))
        if max_loans <= 0:
            print("Max loans must be a positive number.\n")
            return
    except ValueError:
        print("Max loans must be a positive integer.\n")
        return
    
    # Create new user and save
    user = User(user_id, name, email, status, max_loans)
    users.append(user)
    storage.save_users(users)
    print("✓ User added successfully.\n")

def list_users():
    print("\n--- User List ---")
    users = storage.load_users()
    if not users:
        print("No users found.\n")
    else:
        for user in users:
            print(user)
        print()

def update_user(user_id=None):
    """Update an existing user's information."""
    print("\n--- Update a User ---")
    users = storage.load_users()
    
    # Get the user ID if not provided
    if user_id is None:
        user_id = input("Enter User ID to update: ").strip()
    
    # Find the user
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        print("User not found.\n")
        return
    
    # Show message that empty fields will keep current value
    print("Leave field empty to keep current value.")
    
    # Update Name
    name = input(f"Enter Name [{user.name}]: ").strip() or user.name
    if not name:
        print("Name cannot be empty.\n")
        return
    
    # Update Email
    email = input(f"Enter Email [{user.email}]: ").strip() or user.email
    if not email.endswith("@ust.com"):
        print("❌ Email must end with @ust.com.\n")
        return
    
    # Update Status
    status = input(f"Enter Status (active/inactive/banned) [{user.status}]: ").strip().lower() or user.status
    if status not in ["active", "inactive", "banned"]:
        print("❌ Status must be one of: active, inactive, banned.\n")
        return
    
    # Update Max Loans
    max_loans_input = input(f"Enter Max Loans [{getattr(user, 'max_loans', '')}]: ")
    if max_loans_input.strip():
        try:
            max_loans = int(max_loans_input)
            if max_loans <= 0:
                print("Max loans must be a positive number.\n")
                return
            user.max_loans = max_loans
        except ValueError:
            print("Invalid number for max loans. Keeping existing value.")
    
    # Apply changes
    user.name = name
    user.email = email
    user.status = status
    
    storage.save_users(users)
    print("✓ User updated successfully.\n")

def remove_user():
    """Remove a user from the system."""
    print("\n--- Remove a User ---")
    user_id = input("Enter User ID to remove: ")
    users = storage.load_users()
    
    # Find the user
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        print("User not found.\n")
        return
    
    # Ask for confirmation before deleting
    confirm = input(f"Are you sure you want to remove '{user.name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        users = [u for u in users if u.user_id != user_id]
        storage.save_users(users)
        print("✓ User removed successfully.\n")
    else:
        print("Operation cancelled.\n")

def user_services():
    """Show user services menu and handle user choices."""
    while True:
        print("\n=== User Services ===")
        print("1. Add User")
        print("2. View All Users")
        print("3. Update User")
        print("4. Remove User")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            remove_user()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.\n")

# ================== TRANSACTION SERVICES ==================
# These functions handle borrowing and returning books

def borrow_book():
    """Allow a user to borrow a book from the library."""
    print("\n--- Borrow a Book ---")
    user_id = input("Enter User ID: ")
    book_id = input("Enter Book ID: ")

    # Load all data
    users = storage.load_users()
    books = storage.load_books()

    # Find the user and book
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)

    # Validate user and book exist
    if not user:
        print("❌ User not found.\n")
        return
    if not book:
        print("❌ Book not found.\n")
        return
    
    # Check if user can borrow (must be active and under their loan limit)
    if not user.can_borrow():
        print(f"❌ User '{user.name}' cannot borrow more books (reached limit or inactive).\n")
        return
    
    # Check if book is available
    if not book.is_available():
        print(f"❌ Book '{book.title}' is not available.\n")
        return

    # Create transaction
    borrow_date = datetime.today().strftime('%d-%m-%Y')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
    tx_id = f"T{len(storage.load_transactions()) + 1}"

    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    # Explicitly set transaction fields for clarity and persistence
    # status should be 'borrowed' when creating a new borrow transaction
    transaction.status = "borrowed"
    # return_date must be None while the book is out
    transaction.return_date = None

    # Update book and user
    book.decrease_copies(1)
    user.increase_active_loans()

    # Save all changes
    storage.save_books(books)
    storage.save_users(users)

    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)

    print(f"✓ Borrow successful!")
    print(f"  Transaction ID: {tx_id}")
    print(f"  Due Date: {due_date}\n")

def return_book():
    """Allow a user to return a borrowed book."""
    print("\n--- Return a Book ---")
    transaction_id = input("Enter Transaction ID: ")

    transactions = storage.load_transactions()
    transaction = next((t for t in transactions if t.tx_id == transaction_id), None)

    if not transaction:
        print("❌ Transaction not found.\n")
        return
    if transaction.status == "returned":
        print("❌ This book has already been returned.\n")
        return

    # Mark transaction as returned with today's date and update status
    # mark_returned sets both return_date and status to 'returned'
    transaction.mark_returned(datetime.today().strftime('%d-%m-%Y'))

    # Update book (increase copies)
    books = storage.load_books()
    book = next((b for b in books if b.book_id == transaction.book_id), None)
    if book:
        book.increase_copies(1)
        storage.save_books(books)

    # Update user (decrease active loans)
    users = storage.load_users()
    user = next((u for u in users if u.user_id == transaction.user_id), None)
    if user:
        user.decrease_active_loans()
        storage.save_users(users)

    # Save transaction
    storage.save_transactions(transactions)
    print("✓ Return successful.\n")

def transaction_services():
    """Show transaction services menu and handle user choices."""
    while True:
        print("\n=== Transaction Services ===")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Please enter 1-3.\n")

# ================== UTILITY FUNCTIONS ==================
# Helper functions and main menu

def save_data():
    """Save all data to CSV files."""
    storage.save_books(storage.load_books())
    storage.save_users(storage.load_users())
    storage.save_transactions(storage.load_transactions())
    print("✓ All data saved to CSV successfully.\n")

def show_help():
    """Display help information."""
    print("\n=== Available Services ===")
    print("1. Book Services: Add, view, update, and remove books")
    print("2. User Services: Add, view, update, and remove users")
    print("3. Transaction Services: Borrow and return books")
    print("4. Utility Commands: Save data")
    print("5. Help: Show this help message")
    print("6. Exit: Close the program\n")

def main():
    """Main function that runs the library management system."""
    print("\n" + "="*50)
    print(" LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Book Services")
        print("2. User Services")
        print("3. Transaction Services")
        print("4. Utility Commands")
        print("5. Help")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            book_services()
        elif choice == "2":
            user_services()
        elif choice == "3":
            transaction_services()
        elif choice == "4":
            save_data()
        elif choice == "5":
            show_help()
        elif choice == "6":
            print("\n✓ Thank you for using Library Management System!")
            print("Goodbye!\n")
            sys.exit()
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
    
    
