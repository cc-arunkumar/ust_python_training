import sys
from storage import CSVStorage
from models import Book, User, Transaction
from datetime import datetime, timedelta
import uuid

# Initialize the storage
storage = CSVStorage()

# Function to add a book
def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors = input("Authors (comma separated): ")
    isbn = input("ISBN: ")
    tags = input("Tags (comma separated): ")
    total_copies = int(input("Total Copies: "))

    book = Book(book_id, title, authors.split(','), isbn, tags.split(','), total_copies, total_copies)
    books = storage.load_books()
    books.append(book)
    storage.save_books(books)
    print("Book added successfully.")

# Function to update a book
def update_book():
    book_id = input("Book ID: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)

    if not book:
        print("Book not found!")
        return

    new_details = {}
    new_details['title'] = input(f"New title (current: {book.title}): ")
    new_details['authors'] = input(f"New authors (current: {', '.join(book.authors)}): ").split(',')
    new_details['isbn'] = input(f"New ISBN (current: {book.isbn}): ")
    new_details['tags'] = input(f"New tags (current: {', '.join(book.tags)}): ").split(',')
    new_details['total_copies'] = int(input(f"New total copies (current: {book.total_copies}): "))
    new_details['available_copies'] = int(input(f"New available copies (current: {book.available_copies}): "))

    book.update(new_details)
    storage.save_books(books)
    print(f"Book {book_id} updated successfully.")

# Function to remove a book
def remove_book():
    book_id = input("Book ID to remove: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)

    if not book:
        print("Book not found!")
        return

    books.remove(book)
    storage.save_books(books)
    print(f"Book {book_id} removed successfully.")

# Function to get details of a specific book
def get_book():
    book_id = input("Book ID: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)

    if not book:
        print("Book not found!")
        return

    print(f"Book ID: {book.book_id}")
    print(f"Title: {book.title}")
    print(f"Authors: {', '.join(book.authors)}")
    print(f"ISBN: {book.isbn}")
    print(f"Tags: {', '.join(book.tags)}")
    print(f"Total Copies: {book.total_copies}")
    print(f"Available Copies: {book.available_copies}")

# Function to search books by title, author, or tag
def search_books():
    search_type = input("Search by (title/author/tag): ").strip().lower()
    search_value = input(f"Enter {search_type}: ").strip().lower()
    
    books = storage.load_books()

    if search_type == "title":
        result = [book for book in books if search_value in book.title.lower()]
    elif search_type == "author":
        result = [book for book in books if any(search_value in author.lower() for author in book.authors)]
    elif search_type == "tag":
        result = [book for book in books if search_value in book.tags]
    else:
        print("Invalid search type!")
        return

    if not result:
        print("No books found.")
    else:
        for book in result:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Available Copies: {book.available_copies}")

# Function to add a user
def add_user():
    user_id = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    status = input("Status (active/inactive/banned): ")
    max_loans = int(input("Max Loans: "))

    user = User(user_id, name, email, status, max_loans)
    users = storage.load_users()
    users.append(user)
    storage.save_users(users)
    print("User added successfully.")

# Function to update a user
def update_user():
    user_id = input("User ID: ")
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)

    if not user:
        print("User not found!")
        return

    user.name = input(f"New name (current: {user.name}): ")
    user.email = input(f"New email (current: {user.email}): ")
    user.status = input(f"New status (current: {user.status}): ")
    user.max_loans = int(input(f"New max loans (current: {user.max_loans}): "))

    storage.save_users(users)
    print(f"User {user_id} updated successfully.")

# Function to list all users
def list_users():
    users = storage.load_users()
    for user in users:
        print(f"User ID: {user.user_id}, Name: {user.name}, Status: {user.status}")

# Function to deactivate, activate, or ban a user
def manage_user_status(command):
    user_id = command.split()[2]
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)

    if not user:
        print("User not found!")
        return

    if "deactivate" in command:
        user.deactivate()
    elif "activate" in command:
        user.activate()
    elif "ban" in command:
        user.ban()

    storage.save_users(users)
    print(f"User {user_id} status updated to {user.status}.")

# Function to borrow a book
def borrow_book():
    user_id = input("User ID: ")
    book_id = input("Book ID: ")

    users = storage.load_users()
    books = storage.load_books()

    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)

    if not user:
        print("User not found!")
        return
    if not book:
        print("Book not found!")
        return
    if not user.can_borrow():
        print(f"User {user.name} cannot borrow more books.")
        return
    if not book.is_available():
        print(f"Book {book.title} is not available.")
        return
    
    borrow_date = datetime.today().strftime('%d-%m-%Y')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
    tx_id = f"T{len(storage.load_transactions()) + 1}"
    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    
    book.decrease_copies(1)
    books = storage.load_books()
    storage.save_books(books)
    
    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)

    print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")

# Main function to handle all commands
def main():
    while True:
        command = input("lms> ").strip()

        if command == "book add":
            add_book()
        elif command == "book update":
            update_book()
        elif command == "book remove":
            remove_book()
        elif command == "book get":
            get_book()
        elif command.startswith("book search"):
            search_books()
        elif command == "user add":
            add_user()
        elif command == "user update":
            update_user()
        elif command == "user list":
            list_users()
        elif command.startswith("user deactivate") or command.startswith("user activate") or command.startswith("user ban"):
            manage_user_status(command)
        elif command.startswith("borrow"):
            borrow_book()
        elif command == "exit":
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()





# sample output
# lms> book add
# Book ID: B1041
# Title: Python Basics
# Authors (comma separated): Mark Lutz
# ISBN: 1234567890
# Tags (comma separated): programming, python
# Total Copies: 10
# Book added successfully.
# lms> user add
# User ID: U2026
# Name: sanjay
# Email: sanjay@ust.com
# Status (active/inactive/banned): active
# Max Loans: 7
# User added successfully.
# lms> borrow
# User ID: U2026
# Book ID: B1041
# Borrow successful. Transaction ID: T21. Due Date: 29-11-2025.
# lms> loans active
# Unknown command. Type 'help' for a list of commands.
# lms>