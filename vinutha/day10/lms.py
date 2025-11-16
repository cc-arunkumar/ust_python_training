import sys
from storage import CSVStorage
from models import Book, User, Transaction
from datetime import datetime, timedelta

# Initialize the storage
storage = CSVStorage()

def display_menu():
    """Display the main menu with options."""
    print("\n=== Library Management System ===")
    print("\n******** BOOK ******")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Get Book Details")
    print("5. List Books")
    print("6. Search Books")
    print("\n******** USER ******")
    print("7. Add User")
    print("8. Update User")
    print("9. Get User Details")
    print("10. List Users")
    print("11. Deactivate/Activate/Ban User")
    print("\n******** TRANSACTIONS ******")
    print("12. Borrow Book")
    print("13. Return Book")
    print("14. View Active Loans")
    print("15. View Overdue Loans")
    print("16. View User Loan History")
    print("17. Save Data to CSV")
    print("18. Exit")
    print("19. Help")
    print("===================================")

def handle_choice(choice):
    """Map user choice to appropriate function."""
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        get_book_details()
    elif choice == "5":
        list_books()
    elif choice == "6":
        search_books()
    elif choice == "7":
        add_user()
    elif choice == "8":
        update_user()
    elif choice == "9":
        get_user_details()
    elif choice == "10":
        list_users()
    elif choice == "11":
        user_deactivate_activate_ban()
    elif choice == "12":
        borrow_book()
    elif choice == "13":
        return_book()
    elif choice == "14":
        view_active_loans()
    elif choice == "15":
        view_overdue_loans()
    elif choice == "16":
        user_loan_history()
    elif choice == "17":
        save_data()
    elif choice == "18":
        exit_program()
    elif choice == "19":
        display_help()
    else:
        print("Invalid choice. Please try again.")

def display_help():
    """Display help instructions for the user."""
    print("""
    === Library Management System Help ===
    book add              - Add a new book to the library
    book update <book_id>  - Update book details
    book remove <book_id>  - Remove a book from the library
    book get <book_id>     - Get details of a specific book
    book list              - List all books in the library
    book search <query>    - Search books by title, author, or tag
    
    user add              - Add a new user
    user update <user_id> - Update user details
    user get <user_id>    - Get details of a specific user
    user list             - List all users
    user deactivate <user_id> - Deactivate a user
    user activate <user_id>   - Activate a user
    user ban <user_id>    - Ban a user
    
    borrow <user_id> <book_id> - Borrow a book
    return <transaction_id>    - Return a borrowed book
    
    loans active           - View all active loans
    loans overdue          - View overdue loans
    loans user <user_id>   - View loan history for a specific user
    
    save                   - Save all data to CSV
    exit                   - Exit the program
    help                   - Display this help message
    """)

# Book Management Commands
def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors = input("Authors (comma separated): ").split(',')
    isbn = input("ISBN: ")
    tags = input("Tags (comma separated): ").split(',')
    total_copies = int(input("Total Copies: "))

    book = Book(book_id, title, authors, isbn, tags, total_copies)
    books = storage.load_books()
    books.append(book)
    storage.save_books(books)
    print("Book added successfully.")

def update_book():
    book_id = input("Enter the Book ID to update: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    
    if not book:
        print("Book not found.")
        return
    
    title = input(f"New Title (Current: {book.title}): ") or book.title
    authors = input(f"New Authors (comma separated, Current: {', '.join(book.authors)}): ") or ','.join(book.authors)
    isbn = input(f"New ISBN (Current: {book.isbn}): ") or book.isbn
    tags = input(f"New Tags (comma separated, Current: {', '.join(book.tags)}): ") or ','.join(book.tags)
    total_copies = int(input(f"New Total Copies (Current: {book.total_copies}): ") or book.total_copies)

    book.update(title=title, authors=authors.split(','), isbn=isbn, tags=tags.split(','), total_copies=total_copies)
    storage.save_books(books)
    print("Book updated successfully.")

def remove_book():
    book_id = input("Enter the Book ID to remove: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    
    if not book:
        print("Book not found.")
        return
    
    if book.available_copies < book.total_copies:
        print("Cannot remove a book that is currently borrowed.")
        return
    
    books.remove(book)
    storage.save_books(books)
    print("Book removed successfully.")

def get_book_details():
    book_id = input("Enter the Book ID: ")
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    
    if not book:
        print("Book not found.")
        return
    
    print(f"Book ID: {book.book_id}")
    print(f"Title: {book.title}")
    print(f"Authors: {', '.join(book.authors)}")
    print(f"ISBN: {book.isbn}")
    print(f"Tags: {', '.join(book.tags)}")
    print(f"Total Copies: {book.total_copies}")
    print(f"Available Copies: {book.available_copies}")

def list_books():
    books = storage.load_books()
    if not books:
        print("No books found.")
        return
    print(f"{'Book ID':<15}{'Title':<30}{'Available Copies'}")
    print("="*60)
    for book in books:
        print(f"{book.book_id:<15}{book.title:<30}{book.available_copies}")

def search_books():
    query = input("Enter title, author, or tag to search: ").lower()
    books = storage.load_books()
    results = [book for book in books if (query in book.title.lower() or
                                           query in ','.join(book.authors).lower() or
                                           query in ','.join(book.tags).lower())]
    
    if not results:
        print("No books found matching the query.")
        return

    print(f"{'Book ID':<15}{'Title':<30}{'Available Copies'}")
    print("="*60)
    for book in results:
        print(f"{book.book_id:<15}{book.title:<30}{book.available_copies}")

# User Management Commands
def add_user():
    user_id = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    status = input("Status (active/inactive/banned): ")
    max_loans = input("Max Loans: ")
    password = input("Password: ")  # Get the password from the user

    # Check if user already exists
    users = storage.load_users()
    if any(user.user_id == user_id for user in users):
        print(f"Error: User with ID {user_id} already exists.")
        return
    
    user = User(user_id, name, email, status, max_loans, password)  # Pass password to User constructor
    users.append(user)
    storage.save_users(users)
    print("User added successfully.")


def update_user():
    user_id = input("Enter User ID to update: ")
    users = storage.load_users()

    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        print(f"User with ID {user_id} not found!")
        return
    
    print(f"Updating details for user: {user.name}")
    print("1. Update Name")
    print("2. Update Email")
    print("3. Update Status")
    print("4. Update Max Loans")
    print("5. Update Password")
    choice = input("Choose option (1-5): ")

    if choice == "1":
        user.name = input("Enter new Name: ")
    elif choice == "2":
        user.email = input("Enter new Email: ")
    elif choice == "3":
        user.status = input("Enter new Status (active/inactive/banned): ")
    elif choice == "4":
        user.max_loans = int(input("Enter new Max Loans: "))
    elif choice == "5":
        old_password = input("Enter current password: ")
        new_password = input("Enter new password: ")
        user.update_password(old_password, new_password)
    else:
        print("Invalid choice.")
        return

    storage.save_users(users)
    print("User updated successfully.")

def get_user_details():
    user_id = input("Enter the User ID: ")
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)
    
    if not user:
        print("User not found.")
        return
    
    print(f"User ID: {user.user_id}")
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Status: {user.status}")
    print(f"Max Loans: {user.max_loans}")

def list_users():
    users = storage.load_users()
    if not users:
        print("No users found.")
        return
    print(f"{'User ID':<15}{'Name':<30}{'Status':<15}")
    print("="*60)
    for user in users:
        print(f"{user.user_id:<15}{user.name:<30}{user.status:<15}")

def user_deactivate_activate_ban():
    user_id = input("Enter the User ID to deactivate/activate/ban: ")
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)
    
    if not user:
        print("User not found.")
        return
    
    action = input("Enter action (deactivate/activate/ban): ").lower()
    if action == "deactivate":
        user.deactivate()
    elif action == "activate":
        user.activate()
    elif action == "ban":
        user.ban()
    else:
        print("Invalid action.")
        return

    storage.save_users(users)
    print(f"User {action}d successfully.")

# Borrow/Return Commands
def borrow_book():
    user_id = input("Enter User ID: ")
    book_id = input("Enter Book ID: ")

    users = storage.load_users()
    books = storage.load_books()
    
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)
    
    if not user:
        print("User not found.")
        return
    if not book:
        print("Book not found.")
        return
    if not user.can_borrow():
        print("User cannot borrow more books.")
        return
    if not book.is_available():
        print("Book is not available.")
        return
    
    borrow_date = datetime.today().strftime('%Y-%m-%d')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%Y-%m-%d')
    tx_id = f"T{len(storage.load_transactions()) + 1}"
    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    
    book.decrease_copies(1)
    books = storage.load_books()
    storage.save_books(books)
    
    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)
    
    print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")

def return_book():
    tx_id = input("Enter Transaction ID: ")
    transactions = storage.load_transactions()
    transaction = next((t for t in transactions if t.tx_id == tx_id), None)
    
    if not transaction:
        print("Transaction not found.")
        return
    if transaction.status == "returned":
        print("Book already returned.")
        return

    transaction.mark_returned(datetime.today().strftime('%Y-%m-%d'))
    storage.save_transactions(transactions)
    
    books = storage.load_books()
    book = next((b for b in books if b.book_id == transaction.book_id), None)
    if book:
        book.increase_copies(1)
        storage.save_books(books)
    
    print(f"Return successful. Book ID: {transaction.book_id} returned.")

def view_active_loans():
    transactions = storage.load_transactions()
    active_loans = [tx for tx in transactions if tx.status == "borrowed"]
    
    if not active_loans:
        print("No active loans.")
        return
    
    print(f"{'Transaction ID':<15}{'User ID':<15}{'Book ID':<15}{'Due Date'}")
    print("="*60)
    for tx in active_loans:
        print(f"{tx.tx_id:<15}{tx.user_id:<15}{tx.book_id:<15}{tx.due_date}")

def view_overdue_loans():
    today = datetime.today().strftime('%Y-%m-%d')
    transactions = storage.load_transactions()
    overdue_loans = [tx for tx in transactions if tx.status == "borrowed" and tx.is_overdue(today)]
    
    if not overdue_loans:
        print("No overdue loans.")
        return
    
    print(f"{'Transaction ID':<15}{'User ID':<15}{'Book ID':<15}{'Due Date'}")
    print("="*60)
    for tx in overdue_loans:
        print(f"{tx.tx_id:<15}{tx.user_id:<15}{tx.book_id:<15}{tx.due_date}")

def user_loan_history():
    user_id = input("Enter User ID: ")
    transactions = storage.load_transactions()
    user_loans = [tx for tx in transactions if tx.user_id == user_id]
    
    if not user_loans:
        print(f"No loans found for User ID: {user_id}.")
        return
    
    print(f"{'Transaction ID':<15}{'Book ID':<15}{'Borrow Date':<15}{'Due Date':<15}{'Return Date'}")
    print("="*80)
    for tx in user_loans:
        print(f"{tx.tx_id:<15}{tx.book_id:<15}{tx.borrow_date:<15}{tx.due_date:<15}{tx.return_date if tx.return_date else 'Not Returned'}")

def save_data():
    storage.save_books(storage.load_books())
    storage.save_users(storage.load_users())
    storage.save_transactions(storage.load_transactions())
    print("All data saved to CSV successfully.")

def exit_program():
    print("Exiting the Library Management System. Goodbye!")
    sys.exit(0)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        handle_choice(choice)

if __name__ == "__main__":
    main()
