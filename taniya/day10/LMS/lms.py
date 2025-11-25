
from storage import CSVStorage
from library import Library
from models import Book, User, InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError, AuthFailed
from utils import csv_authors_from_input, csv_tags_from_input

# -------------------------------
# Helper functions to print objects in a readable format
# -------------------------------

def print_book(b: Book):
    # Print book details in a formatted line
    print(f"{b.book_id} | {b.title} | Authors: {', '.join(b.authors)} | ISBN: {b.isbn or '-'} | Tags: {', '.join(b.tags)} | Total: {b.total_copies} | Available: {b.available_copies}")

def print_user(u: User):
    # Print user details in a formatted line
    print(f"{u.user_id} | {u.name} | Email: {u.email or '-'} | Status: {u.status} | Max Loans: {u.max_loans}")

def print_tx(t):
    # Print transaction details in a formatted line
    print(f"{t.tx_id} | Book: {t.book_id} | User: {t.user_id} | Borrow: {t.borrow_date} | Due: {t.due_date} | Return: {t.return_date or '-'} | Status: {t.status}")

# -------------------------------
# Menu display functions
# -------------------------------

def show_main_menu():
    # Print main menu options
    print("""
UST Library Management System - Main Menu
Please choose an option by number:
  1) Books
  2) Users
  3) Borrow / Return
  4) Loans
  5) Reports
  6) Save Data
  7) Help
  0) Exit
""")

def show_books_menu():
    # Print books menu options
    print("""
Books - Options:
  1) Add Book
  2) Update Book
  3) Remove Book
  4) Get Book by ID
  5) List All Books
  6) Search Books
  0) Back to Main Menu
""")

def show_users_menu():
    # Print users menu options
    print("""
Users - Options:
  1) Add User
  2) Update User
  3) Get User by ID
  4) List All Users
  5) Deactivate User
  6) Activate User
  7) Ban User
  0) Back to Main Menu
""")

def show_borrow_menu():
    # Print borrow/return menu options
    print("""
Borrow / Return:
  1) Borrow Book
  2) Return Book
  0) Back to Main Menu
""")

def show_loans_menu():
    # Print loans menu options
    print("""
Loans:
  1) Active Loans
  2) Overdue Loans
  3) Loans for a User
  0) Back to Main Menu
""")

def show_reports_menu():
    # Print reports menu options
    print("""
Reports:
  1) Summary
  2) User History
  0) Back to Main Menu
""")

# -------------------------------
# Authentication
# -------------------------------

def authenticate_user(lib: Library, user_id: str) -> bool:
    # Authenticate user by checking password with 3 attempts
    u = lib.get_user(user_id)
    if not u:
        raise AuthFailed("User not found.")
    attempts = 3
    for i in range(attempts):
        pw = input(f"Enter password for {user_id} (attempt {i+1}/{attempts}): ")
        if pw == getattr(u, "password", None):
            return True
        else:
            print("Incorrect password.")
    raise AuthFailed("Authentication failed.")

# -------------------------------
# Listing helpers
# -------------------------------

def list_user_ids(lib: Library):
    # Print all registered user IDs
    users = lib.list_users()
    if not users:
        print("No users registered.")
        return
    print("Registered User IDs:")
    for u in users:
        print(f"  - {u.user_id} ({u.name})")

def list_book_ids(lib: Library):
    # Print all available book IDs
    books = lib.list_books()
    if not books:
        print("No books available.")
        return
    print("Available Book IDs:")
    for b in books:
        print(f"  - {b.book_id}")

def list_book_titles(lib: Library):
    # Print all book titles
    books = lib.list_books()
    if not books:
        print("No books available.")
        return
    print("Available Book Titles:")
    for b in books:
        print(f"  - {b.title} ")

def list_book_authors(lib: Library):
    # Print all book authors
    books = lib.list_books()
    if not books:
        print("No books available.")
        return
    print("Available Book Authors:")
    for b in books:
        print(f"  - {b.authors} ")

def list_book_tags(lib: Library): 
    # Print all book tags
    books = lib.list_books()
    if not books:
        print("No books available.")
        return
    print("Available Book Tags:")
    for b in books:
        print(f"  - {b.tags} ")

# -------------------------------
# Book flows (search, add, update, remove, get, list)
# -------------------------------

def books_search_flow(lib: Library):
    # Search books by title, author, or tag
    print("Search by: 1) Title  2) Author  3) Tag")
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        list_book_titles(lib)
        q = input("Enter title substring: ")
        res = lib.search_books_title(q)
    elif choice == "2":
        list_book_authors(lib)
        q = input("Enter author name: ")
        res = lib.search_books_author(q)
    elif choice == "3":
        list_book_tags(lib)
        q = input("Enter tag: ")
        res = lib.search_books_tag(q)
    else:
        print("Invalid search choice.")
        return

    if not res:
        print("No matching books found.")
    else:
        print(f"Found {len(res)} book(s):")
        for b in res:
            print_book(b)

def book_add_flow(lib: Library):
    # Add a new book interactively
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors_in = input("Authors (comma separated): ")
    isbn = input("ISBN: ")
    tags_in = input("Tags (comma separated): ")
    try:
        total_copies = int(input("Total Copies: ") or "0")
    except ValueError:
        print("Total copies must be a number. Aborting add.")
        return
    available_copies_in = input("Available Copies (leave empty to default to Total): ")
    try:
        available_copies = int(available_copies_in) if available_copies_in else total_copies
    except ValueError:
        print("Available copies must be a number. Aborting add.")
        return

    b = Book(
        book_id=book_id,
        title=title,
        authors=csv_authors_from_input(authors_in),
        isbn=isbn or None,
        tags=csv_tags_from_input(tags_in),
        total_copies=total_copies,
        available_copies=available_copies
    )
    lib.add_book(b)
    print("Book added successfully.")

def book_update_flow(lib: Library):
    # Update book details interactively
    list_book_ids(lib)
    book_id = input("Book ID to update: ")
    print("Leave field empty to skip updating.")
    new_title = input("Title: ")
    new_authors = input("Authors (comma separated): ")
    new_isbn = input("ISBN: ")
    new_tags = input("Tags (comma separated): ")
    new_total = input("Total Copies: ")
    new_available = input("Available Copies: ")
    kwargs = {}
    if new_title: kwargs["title"] = new_title
    if new_authors: kwargs["authors"] = csv_authors_from_input(new_authors)
    if new_isbn: kwargs["isbn"] = new_isbn
    if new_tags: kwargs["tags"] = csv_tags_from_input(new_tags)
    if new_total: kwargs["total_copies"] = int(new_total)
    if new_available: kwargs["available_copies"] = int(new_available)
    lib.update_book(book_id, **kwargs)
    print("Book updated.")

def book_remove_flow(lib: Library):
    # Remove a book interactively
    list_book_ids(lib)
    bid = input("Book ID to remove: ")
    lib.remove_book(bid)
    print("Book removed if it existed.")

def book_get_flow(lib: Library):
    # Get book details by ID
    list_book_ids(lib)
    bid = input("Book ID: ")
    b = lib.get_book(bid)
    if b:
        print_book(b)
    else:
        print("Book not found.")

def book_list_flow(lib: Library):
    # List all books
    items = lib.list_books()
    if not items:
        print("No books available.")
    else:
        for b in items:
            print_book(b)

# -------------------------------
# User flows (add, update,

# -------------------------------
# Return flow: handles returning a borrowed book
# -------------------------------
def return_flow(lib: Library):
    print("Active Loans:")
    lib.loans_active()                        # Show active loans
    tx_id(lib)                                # Show available transaction IDs (helper function)
    tx_id = input("Transaction ID to return: ")  # Ask user for transaction ID
    lib.return_book(tx_id)                    # Call library method to return book
    print("Return successful.")

# -------------------------------
# Loans flows: active, overdue, user-specific
# -------------------------------
def loans_active_flow(lib: Library):
    res = lib.loans_active()                  # Get active loans
    if not res:
        print("No active loans.")
    else:
        for t in res: print_tx(t)             # Print each transaction

def loans_overdue_flow(lib: Library):
    res = lib.loans_overdue()                 # Get overdue loans
    if not res:
        print("No overdue loans.")
    else:
        for t in res: print_tx(t)

def loans_user_flow(lib: Library):
    print("Available users:")
    list_user_ids(lib)                        # Show all users
    uid = input("Enter User ID to list loans: ")
    if not uid:
        print("No user selected.")
        return
    res = lib.loans_user(uid)                 # Get loans for specific user
    if not res:
        print("No loans for user.")
    else:
        for t in res: print_tx(t)

# -------------------------------
# Reports flows: summary and user history
# -------------------------------
def report_summary_flow(lib: Library):
    r = lib.report_summary()                  # Get summary report
    print("Summary Report:")
    print(f"  Total books: {r.get('total_books', 0)}")
    print(f"  Total users: {r.get('total_users', 0)}")
    print(f"  Active loans: {r.get('active_loans', 0)}")
    print(f"  Overdue loans: {r.get('overdue_loans', 0)}")

def report_user_flow(lib: Library):
    print("Available users:")
    list_user_ids(lib)                        # Show all users
    uid = input("Enter User ID for history: ")
    if not uid:
        print("No user selected.")
        return
    txs = lib.report_user_history(uid)        # Get user loan history
    if not txs:
        print("No history for user.")
    else:
        for t in txs:
            print_tx(t)

# -------------------------------
# Main program loop
# -------------------------------
def main():
    storage = CSVStorage()                    # Initialize CSV storage
    lib = Library(storage)                    # Create Library instance
    print("Welcome to the UST Library Management System")

    while True:                               # Infinite loop until exit
        try:
            show_main_menu()                  # Display main menu
            choice = input("Select an option: ")
        except (EOFError, KeyboardInterrupt): # Handle Ctrl+D or Ctrl+C
            print("\nExiting. Goodbye.")
            break

        try:
            # Help option
            if choice == "7" or choice.lower() == "help":
                print("Use the menus to perform actions. Enter numbers to navigate.")
                continue

            # Exit option
            if choice == "0":
                print("Goodbye.")
                break

            # Save data option
            if choice == "6":
                lib.save_all()
                print("All data saved to CSV successfully.")
                continue

            # -------------------------------
            # Books submenu
            # -------------------------------
            if choice == "1":
                while True:
                    show_books_menu()
                    sub = input("Books> ")
                    if sub == "0":
                        break
                    try:
                        if sub == "1":
                            book_add_flow(lib)
                        elif sub == "2":
                            book_update_flow(lib)
                        elif sub == "3":
                            book_remove_flow(lib)
                        elif sub == "4":
                            book_get_flow(lib)
                        elif sub == "5":
                            book_list_flow(lib)
                        elif sub == "6":
                            books_search_flow(lib)
                        else:
                            print("Invalid selection in Books menu.")
                    except (InvalidBookError, ValidationError, ValueError, AuthFailed) as e:
                        print(f"Error: {e}")
                continue

            # -------------------------------
            # Users submenu
            # -------------------------------
            if choice == "2":
                while True:
                    show_users_menu()
                    sub = input("Users> ")
                    if sub == "0":
                        break
                    try:
                        if sub == "1":
                            user_add_flow(lib)
                        elif sub == "2":
                            user_update_flow(lib)
                        elif sub == "3":
                            user_get_flow(lib)
                        elif sub == "4":
                            user_list_flow(lib)
                        elif sub == "5":
                            list_user_ids(lib)
                            uid = input("User ID to deactivate: ")
                            lib.deactivate_user(uid); print("User deactivated.")
                        elif sub == "6":
                            list_user_ids(lib)
                            uid = input("User ID to activate: ")
                            lib.activate_user(uid); print("User activated.")
                        elif sub == "7":
                            list_user_ids(lib)
                            uid = input("User ID to ban: ")
                            lib.ban_user(uid); print("User banned.")
                        else:
                            print("Invalid selection in Users menu.")
                    except (InvalidUserError, ValidationError, ValueError, AuthFailed) as e:
                        print(f"Error: {e}")
                continue

            # -------------------------------
            # Borrow / Return submenu
            # -------------------------------
            if choice == "3":
                while True:
                    show_borrow_menu()
                    sub = input("BorrowReturn> ")
                    if sub == "0":
                        break
                    try:
                        if sub == "1":
                            borrow_flow(lib)
                        elif sub == "2":
                            return_flow(lib)
                        else:
                            print("Invalid selection.")
                    except (BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError, AuthFailed) as e:
                        print(f"Error: {e}")
                continue

            # -------------------------------
            # Loans submenu
            # -------------------------------
            if choice == "4":
                while True:
                    show_loans_menu()
                    sub = input("Loans> ")
                    if sub == "0":
                        break
                    try:
                        if sub == "1":
                            loans_active_flow(lib)
                        elif sub == "2":
                            loans_overdue_flow(lib)
                        elif sub == "3":
                            loans_user_flow(lib)
                        else:
                            print("Invalid selection in Loans menu.")
                    except Exception as e:
                        print(f"Error: {e}")
                continue

            # -------------------------------
            # Reports submenu
            # -------------------------------
            if choice == "5":
                while True:
                    show_reports_menu()
                    sub = input("Reports> ")
                    if sub == "0":
                        break
                    if sub == "1":
                        report_summary_flow(lib)
                    elif sub == "2":
                        report_user_flow(lib)
                    else:
                        print("Invalid selection in Reports menu.")
                continue

            # If user enters an unknown option
            print("Unknown option. Please use the menu numbers or 'Help'.")

        # -------------------------------
        # Error handling
        # -------------------------------
        except (InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError, AuthFailed) as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    main()   # Run the main program loop