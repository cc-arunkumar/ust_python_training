# library.py
import storage  # Import storage module to handle reading and saving data from/to CSV files
from models import Book, User, Transaction  # Import the necessary classes for Book, User, and Transaction
from datetime import datetime, timedelta  # Import datetime and timedelta for handling dates

# Function to add a new book to the system
def add_book():
    # Prompt user to input book details
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors = input("Authors (comma separated): ")
    isbn = input("ISBN: ")
    tags = input("Tags (comma separated): ")
    total_copies = int(input("Total Copies: "))
    
    # Create a new Book object with the provided details
    book = Book(book_id, title, authors, isbn, tags, total_copies, total_copies)
    
    # Load existing books from storage and add the new book
    books = storage.load_books()
    books.append(book)
    
    # Save the updated book list back to storage (CSV)
    storage.save_books(books)
    
    # Print confirmation message
    print(f"Book {book.title} added successfully.")

# Function to borrow a book for a user
def borrow_book():
    # Prompt user to input user and book IDs for borrowing
    user_id = input("User ID: ")
    book_id = input("Book ID: ")
    
    # Load the lists of users and books from storage
    users = storage.load_users()
    books = storage.load_books()
    
    # Find the user and book based on the IDs provided
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)

    # If the user is not found, print an error and exit
    if not user:
        print("User not found!")
        return
    
    # If the book is not found, print an error and exit
    if not book:
        print("Book not found!")
        return
    
    # Check if the user can borrow more books (based on their limit and current borrowed books)
    if not user.can_borrow():
        print(f"User {user.name} cannot borrow more books.")
        return
    
    # Check if the book is available for borrowing
    if not book.is_available():
        print(f"Book {book.title} is not available.")
        return
    
    # Get the current borrow date and calculate the due date (14 days from today)
    borrow_date = datetime.today().strftime('%d-%m-%Y')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
    
    # Create a new transaction ID (e.g., T1, T2, T3, ...)
    tx_id = f"T{len(storage.load_transactions()) + 1}"
    
    # Create a new transaction object for borrowing the book
    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    
    # Decrease the available copies of the book (book is borrowed)
    book.decrease_copies(1)
    
    # Save the updated book list back to storage
    books = storage.load_books()
    storage.save_books(books)
    
    # Add the transaction to the list of transactions and save it
    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)

    # Print a confirmation message with the transaction ID and due date
    print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")
