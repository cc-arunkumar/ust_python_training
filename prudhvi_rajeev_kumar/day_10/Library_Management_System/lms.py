from storage import CSVStorage
from library import Library
from models import Book, User
from utils import csv_authors_from_input, csv_tags_from_input

def prompt(text):
    return input(text).strip()

# ------------------- Printing Helpers -------------------
def print_book(b: Book):
    print(f"{b.book_id} | {b.title} | Authors: {', '.join(b.authors)} | ISBN: {b.isbn} | Tags: {', '.join(b.tags)} | Total: {b.total_copies} | Available: {b.available_copies}")

def print_user(u: User):
    print(f"{u.user_id} | {u.name} | Email: {u.email or '-'} | Status: {u.status} | Max Loans: {u.max_loans}")

def print_tx(t):
    print(f"{t.tx_id} | Book: {t.book_id} | User: {t.user_id} | Borrow: {t.borrow_date} | Due: {t.due_date} | Return: {t.return_date or '-'} | Status: {t.status}")

# One-line summaries
def print_book_summary(b: Book):
    print(f"- {b.book_id} : {b.title} (Available: {b.available_copies})")

def print_user_summary(u: User):
    print(f"- {u.user_id} : {u.name} [{u.status}]")

def print_tx_summary(t):
    print(f"- {t.tx_id} : Book {t.book_id} borrowed by {t.user_id} (Due: {t.due_date}, Status: {t.status})")

def print_report_summary(r):
    print("\n Library Summary")
    print(f"- Total Books : {r['total_books']}")
    print(f"- Total Users : {r['total_users']}")
    print(f"- Active Loans : {r['active_loans']}")
    print(f"- Overdue Loans : {r['overdue_loans']}")

# ------------------- Authentication -------------------
def authenticate_user(section_name: str) -> bool:
    """
    Ask for password (same for all users: '123').
    Allow 3 attempts. Return True if authenticated, else False.
    """
    attempts = 3
    while attempts > 0:
        password = prompt(f"Enter password to access {section_name}: ")
        if password == "123":
            print(" Authentication successful.")
            return True
        else:
            attempts -= 1
            print(f" Incorrect password. Attempts left: {attempts}")
    print("Returning to Main Menu...")
    return False

# ------------------- Books Menu -------------------
def books_menu(lib: Library):
    while True:
        print("\n--- Books Menu ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Get Book")
        print("5. List Books")
        print("6. Search by Title")
        print("7. Search by Author")
        print("8. Search by Tag")
        print("0. Back to Main Menu")
        choice = prompt("Choose option: ")

        try:
            if choice == "1":
                book_id = prompt("Book ID: ")
                title = prompt("Title: ")
                authors_in = prompt("Authors (comma separated): ")
                isbn = prompt("ISBN: ")
                tags_in = prompt("Tags (comma separated): ")
                total_copies = int(prompt("Total Copies: ") or "0")
                available_copies_in = prompt("Available Copies (leave empty to default to Total): ")
                available_copies = int(available_copies_in) if available_copies_in else total_copies
                b = Book(book_id, title, csv_authors_from_input(authors_in), isbn, csv_tags_from_input(tags_in), total_copies, available_copies)
                lib.add_book(b)
                print(" Book added successfully.")
            elif choice == "2":
                book_id = prompt("Book ID to update: ")
                new_title = prompt("Title (leave blank to skip): ")
                new_authors = prompt("Authors (comma separated, leave blank to skip): ")
                new_isbn = prompt("ISBN (leave blank to skip): ")
                new_tags = prompt("Tags (comma separated, leave blank to skip): ")
                new_total = prompt("Total Copies (leave blank to skip): ")
                new_available = prompt("Available Copies (leave blank to skip): ")
                kwargs = {}
                if new_title: kwargs["title"] = new_title
                if new_authors: kwargs["authors"] = new_authors
                if new_isbn: kwargs["isbn"] = new_isbn
                if new_tags: kwargs["tags"] = new_tags
                if new_total: kwargs["total_copies"] = int(new_total)
                if new_available: kwargs["available_copies"] = int(new_available)
                lib.update_book(book_id, **kwargs)
                print("Book updated.")
            elif choice == "3":
                lib.remove_book(prompt("Book ID to remove: "))
                print(" Book removed.")
            elif choice == "4":
                b = lib.get_book(prompt("Book ID: "))
                if b: print_book(b)
                else: print("Book not found.")
            elif choice == "5":
                print("\n Available Books")
                for b in lib.list_books(): print_book_summary(b)
            elif choice == "6":
                for b in lib.search_books_title(prompt("Title substring: ")): print_book_summary(b)
            elif choice == "7":
                for b in lib.search_books_author(prompt("Author name: ")): print_book_summary(b)
            elif choice == "8":
                for b in lib.search_books_tag(prompt("Tag: ")): print_book_summary(b)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

# ------------------- Users Menu -------------------
def users_menu(lib: Library):
    while True:
        print("\n--- Users Menu ---")
        print("1. Add User")
        print("2. Update User")
        print("3. Get User")
        print("4. List Users")
        print("5. Deactivate User")
        print("6. Activate User")
        print("7. Ban User")
        print("0. Back to Main Menu")
        choice = prompt("Choose option: ")

        try:
            if choice == "1":
                user_id = prompt("User ID: ")
                name = prompt("Name: ")
                email_input = prompt("Email (username only, will append @ust.com): ")
                email = f"{email_input}@ust.com" if email_input else None
                max_loans = int(prompt("Max Loans (default 0): ") or "0")
                u = User(user_id, name, email, "active", max_loans)
                lib.add_user(u)
                print(" User added.")

            elif choice == "2":
                user_id = prompt("User ID to update: ")
                name = prompt("Name (leave blank to skip): ")
                email_input = prompt("Email (username only, leave blank to skip): ")
                status = prompt("Status (active/inactive/banned, leave blank to skip): ")
                max_loans = prompt("Max Loans (leave blank to skip): ")
                kwargs = {}
                if name: kwargs["name"] = name
                if email_input: kwargs["email"] = f"{email_input}@ust.com"
                if status: kwargs["status"] = status
                if max_loans: kwargs["max_loans"] = int(max_loans)
                lib.update_user(user_id, **kwargs)
                print(" User updated.")

            elif choice == "3":
                u = lib.get_user(prompt("User ID: "))
                if u: print_user(u)
                else: print("User not found.")
            elif choice == "4":
                if authenticate_user("All User Details"):
                    print("\n Registered Users")
                    for u in lib.list_users(): print_user_summary(u)
            elif choice == "5":
                lib.deactivate_user(prompt("User ID: "))
                print(" User deactivated.")
            elif choice == "6":
                lib.activate_user(prompt("User ID: "))
                print(" User activated.")
            elif choice == "7":
                lib.ban_user(prompt("User ID: "))
                print(" User banned.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

# ------------------- Borrow/Return Menu -------------------
def borrow_return_menu(lib: Library):
    while True:
        print("\n--- Borrow/Return Menu ---")
        print("1. Borrow Book")
        print("2. Return Book")
        print("0. Back to Main Menu")
        choice = prompt("Choose option: ")
        try:
            if choice == "1":
                user_id = prompt("User ID: ")
                book_id = prompt("Book ID: ")
                t = lib.borrow(user_id, book_id)
                print(f" Borrow successful. Transaction ID: {t.tx_id}. Due Date: {t.due_date}.")
            elif choice == "2":
                tx_id = prompt("Transaction ID: ")
                lib.return_book(tx_id)
                print(" Return successful.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")


# ------------------- Loans Menu -------------------
def loans_menu(lib: Library):
    while True:
        print("\n--- Loans Menu ---")
        print("1. Active Loans ")
        print("2. Overdue Loans ")
        print("3. User Loan History ")
        print("0. Back to Main Menu")
        choice = prompt("Choose option: ")
        try:
            if choice == "1":
                if authenticate_user("Active Loans"):
                    print("\n Active Loans")
                    for t in lib.loans_active():
                        print_tx_summary(t)
            elif choice == "2":
                if authenticate_user("Overdue Loans"):
                    print("\n Overdue Loans")
                    for t in lib.loans_overdue():
                        print_tx_summary(t)
            elif choice == "3":
                if authenticate_user("User Loan History"):
                    user_id = prompt("User ID: ")
                    print(f"\n Loan History for {user_id}")
                    for t in lib.loans_user(user_id):
                        print_tx_summary(t)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

# ------------------- Reports Menu -------------------
def report_menu(lib: Library):
    while True:
        print("\n--- Report Menu ---")
        print("1. Summary Report")
        print("2. User History Report")
        print("0. Back to Main Menu")
        choice = prompt("Choose option: ")
        try:
            if choice == "1":
                r = lib.report_summary()
                print_report_summary(r)
            elif choice == "2":
                if authenticate_user("User History Report"):
                    user_id = prompt("User ID: ")
                    print(f"\n User Report for {user_id}")
                    for t in lib.report_user_history(user_id):
                        print_tx_summary(t)
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

# ------------------- Main Menu -------------------
def main():
    storage = CSVStorage()
    lib = Library(storage)

    while True:
        print("\n===  Library Management System ===")
        print("1.  Manage Books")
        print("2.  Manage Users ")
        print("3.  Borrow & Return")
        print("4.  Loan Tracker ")
        print("5.  Reports & Insights")
        print("6.  Save Changes")
        print("7.  Help & Guide")
        print("8.  Exit System")

        choice = prompt(" Please enter your choice: ")

        if choice == "1":
            books_menu(lib)
        elif choice == "2":
            if authenticate_user("Users Section"):
                users_menu(lib)
        elif choice == "3":
            borrow_return_menu(lib)
        elif choice == "4":
            if authenticate_user("Loans Section"):
                loans_menu(lib)
        elif choice == "5":
            report_menu(lib)
        elif choice == "6":
            lib.save_all()
            print(" All data saved to CSV successfully.")
        elif choice == "7":
            print("\n Help & Guide")
            print("Navigate using numbers. Each section has its own submenu.")
            print("Books → manage books")
            print("Users → manage users (password protected)")
            print("Borrow/Return → borrow or return books")
            print("Loans → view active/overdue loans or user history (password protected)")
            print("Reports → summary or user history reports")
            print("Save → persist all changes to CSV")
            print("Exit → quit the program")
        elif choice == "8":
            print(" Goodbye.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
