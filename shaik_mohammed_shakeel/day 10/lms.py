# Assessment: Library Management System

# Detailed Technical Requirements
# 1. Overview & Scope
# You will build a Command-Line Library Management System (LMS) using:
# Object-Oriented Programming
# Exception Handling (already covered in training)
# CSV-based storage
# Clean and simple CLI interface
# Modular design


# System must support:
# Managing Books
# Managing Users
# Borrow/Return functionality
# Searching & basic reporting
# Persistent storage using CSV file


# Importing models and utilities
from models import Book, User
from library import Library
from utils import print_book, print_user, print_tx

# ------------------- AUTHENTICATION -------------------
# Function to authenticate a user before allowing certain actions
def authenticate_user(library, user_id):
    user = library.get_user(user_id)  # Retrieve user object by ID
    if not user:
        print("User not found.")
        return False

    # Simple password check (password = user_id)
    password_user = input("Enter Password (same as User ID): ")
    if password_user != user_id:
        print("Incorrect password.")
        return False

    return True


# ------------------- EMAIL VALIDATION -------------------
import re

# Function to validate email format using regex
def get_valid_email(prompt=" Email:"):
    # Regex pattern for common valid email formats
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email = input(prompt).strip()
        if re.match(pattern, email):
            return email
        print("Invalid email. Please enter a valid email address (e.g., user@example.com).")


# ------------------- MAIN LMS PROGRAM -------------------
def main():
    library = Library()  

    print("\n Welcome to Library Management System (CLI)\n")

    # ------------------- MAIN MENU LOOP -------------------
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Books")
        print("2. Users")
        print("3. Borrow / Return")
        print("4. Loans")
        print("5. Reports")
        print("6. Save Data")
        print("7. Exit")
        print("===============================")

        choice = input("Enter choice (1-7): ")

        # ------------------- BOOKS MENU -------------------
        match choice:
            case "1":
                while True:
                    print("\n------ BOOKS MENU ------")
                    print("A. Add Book")
                    print("B. Update Book")
                    print("C. Remove Book")
                    print("D. Get Book")
                    print("E. List Books")
                    print("F. Search Books")
                    print("G. Back to main menu")
                    print("------------------------")

                    book_choice = input("Choice: ").lower()

                    match book_choice:

                        # ------------ Add Book ------------
                        case "a":
                            try:
                                book_id = input("Book ID: ")
                                title = input("Title of the Book: ")
                                authors = input("Author of the Book: ")
                                isbn = input("ISBN (International Standard Book Number): ")
                                tags = input("Tags: ")
                                total = int(input("Total Copies: "))

                                # Book model requires available copies as well
                                available = total

                                book = Book(
                                    book_id, title, authors,
                                    isbn, tags, total, available
                                )

                                # Add book to library
                                library.add_book(book) 
                                print("Book added successfully.")

                            except Exception as e:
                                print("Please enter a value to add.", e)

                        # ------------ Update Book ------------
                        case "b":
                            book_id = input("Book ID to update: ")
                            book = library.get_book(book_id)

                            if not book:
                                print(" Book not found.")
                                continue

                            # Get updated values or use existing ones
                            title = input(f"Title of the Book [{book.title}]: ") or book.title
                            authors_raw = input(f"Authors [{', '.join(book.authors)}]: ")
                            authors = authors_raw if authors_raw else book.authors
                            isbn = input(f"ISBN [{book.isbn}]: ") or book.isbn
                            tags_raw = input(f"Tags [{', '.join(book.tags)}]: ")
                            tags = tags_raw if tags_raw else book.tags
                            total_raw = input(f"Total Copies [{book.total_copies}]: ")
                            total = int(total_raw) if total_raw else book.total_copies

                            try:
                                book.update(
                                    title=title,
                                    authors=authors,
                                    isbn=isbn,
                                    tags=tags,
                                    total_copies=total,
                                )
                                print(" Book updated Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Remove Book ------------
                        case "c":
                            try:
                                book_id = input("Book ID to remove: ")
                                library.remove_book(book_id)
                                print(" Book removed Successfully.")
                            except Exception as e:
                                print(" Error:", e)

                        # ------------ Get Book ------------
                        case "d":
                            book_id = input("Book ID: ")
                            book_get = library.get_book(book_id)
                            if book_get:
                                print_book(book_get)
                            else:
                                print(" Book not found.")

                        # ------------ List Books ------------
                        case "e":
                            for book_get in library.list_books():
                                print_book(book_get)

                        # ------------ Search Books ------------
                        case "f":
                            print("Search By:")
                            print("1. Title of the book")
                            print("2. Author of the book")
                            print("3. Tag of the book")
                            search_choice = input("Enter your Choice: ")

                            match search_choice:
                                case "1":
                                    text = input("Enter the title of the book: ")
                                    results = library.search_books_by_title(text)
                                case "2":
                                    text = input("Enter the author's name: ")
                                    results = library.search_books_by_author(text)
                                case "3":
                                    text = input("Enter the tag of the book: ")
                                    results = library.search_books_by_tag(text)
                                case _:
                                    print("Invalid selection.")
                                    continue

                            # Display search results
                            for book_choice in results:
                                print_book(book_choice)

                        # Back to main menu
                        case "g":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- USERS MENU -------------------
            case "2":
                while True:
                    print("\n------ USERS MENU ------")
                    print("A. Add User")
                    print("B. Update User")
                    print("C. Get User")
                    print("D. List Users")
                    print("E. Activate user")
                    print("F. Deactivate user")
                    print("G. Ban user")
                    print("H. Back to main menu")
                    print("------------------------")

                    user_choice = input("Choice: ").lower()

                    match user_choice:
                        # ------------ Add User ------------
                        case "a":
                            try:
                                user_id = input("User ID: ")
                                name = input("User Name: ")
                                # Validate email
                                email = get_valid_email()  
                                user = User(user_id, name, email)
                                library.add_user(user)
                                print(" User added Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Update User ------------
                        case "b":
                            user_id = input("User ID: ")

                            if not authenticate_user(library, user_id):
                                continue

                            user = library.get_user(user_id)
                            if not user:
                                print(" User not found.")
                                continue

                            name = input(f"Name [{user.name}]: ") or user.name
                            email = input(f"Email [{user.email}]: ") or user.email  

                            try:
                                library.update_user(user_id, name=name, email=email)
                                print("User updated Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Get User ------------
                        case "c":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                user = library.get_user(user_id)
                                if user:
                                    print_user(user)
                                else:
                                    print("User not found.")

                        # ------------ List Users ------------
                        case "d":
                            for u1 in library.list_users():
                                print_user(u1)

                        # ------------ Activate User ------------
                        case "e":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.activate_user(user_id)
                                print("User Activated Successfully.")

                        # ------------ Deactivate User ------------
                        case "f":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.deactivate_user(user_id)
                                print("User Deactivated Successfully.")

                        # ------------ Ban User ------------
                        case "g":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.ban_user(user_id)
                                print("User Banned.")

                        # Back to main menu
                        case "h":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- BORROW / RETURN MENU -------------------
            case "3":
                while True:
                    print("\n------ BORROW / RETURN ------")
                    print("A. Borrow Book")
                    print("B. Return Book")
                    print("C. Back")
                    print("-----------------------------")

                    borrow_choice = input("Choice: ").lower()

                    match borrow_choice:
                        # ------------ Borrow Book ------------
                        case "a":
                            user_id = input("User ID: ")
                            if not authenticate_user(library, user_id):
                                continue
                            book_id = input("Book ID: ")

                            try:
                                tx, due = library.borrow_book(user_id, book_id)
                                print("Borrow successful.")
                                print_tx(tx)
                            except Exception as e:
                                print(" Error:", e)

                        # ------------ Return Book ------------
                        case "b":
                            tx_id = input("Transaction ID: ")

                            try:
                                tx = library.return_book(tx_id)
                                print("Return successful.")
                                print_tx(tx)
                            except Exception as e:
                                print(" Error:", e)

                        # Back to previous menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- LOANS MENU -------------------
            case "4":
                while True:
                    print("\n------ LOANS MENU ------")
                    print("A. Active Loans")
                    print("B. Overdue Loans")
                    print("C. Back to main menu")
                    print("------------------------")

                    loan_choice = input("Choice: ").lower()

                    match loan_choice:
                        # Show all active loans
                        case "a":
                            loans = library.get_active_loans()
                            for tx in loans:
                                print_tx(tx)

                        # Show overdue loans
                        case "b":
                            overdue = library.get_overdue_loans()
                            if overdue:
                                for tx in overdue:
                                    print_tx(tx)
                            else:
                                print("No overdue loans at the moment.")

                        # Back to main menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- REPORTS MENU -------------------
            case "5":
                while True:
                    print("\n------ REPORTS MENU ------")
                    print("A. Summary Report")
                    print("B. User Loan History")
                    print("C. Back to main menu")
                    print("--------------------------")

                    report_choice = input("Choice: ").lower()

                    match report_choice:
                        # Summary report of library stats
                        case "a":
                            book_choice, u, a, o = library.summary_report()
                            print(f"""
------- SUMMARY REPORT -------
Total Books     : {book_choice}
Total Users     : {u}
Active Loans    : {a}
Overdue Loans   : {o}
------------------------------
""")

                        # Show specific user's loan history
                        case "b":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                for tx in library.get_user_loans(user_id):
                                    print_tx(tx)

                        # Back to main menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- SAVE DATA -------------------
            case "6":
                library.save_all()
                print("Data saved successfully.")

            # ------------------- EXIT PROGRAM -------------------
            case "7":
                print("Exiting LMS. Thank You!")
                break

            case _:
                print("Invalid choice! Enter 1-7.")


# ------------------- RUN PROGRAM -------------------
if __name__ == "__main__":
    main()
