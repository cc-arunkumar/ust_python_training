import sys
import os
from library import Library
from utils import safe_input, get_today_str
from models import (
    ValidationError, InvalidBookError, InvalidUserError,
    BookNotAvailableError, UserNotAllowedError, TransactionError
)
def print_help():
    """Display all available CLI commands."""
    help_text = """
Library Management System - Available Commands

BOOK COMMANDS:
  book add                    Add a new book (interactive)
  book update <book_id>       Update book details (interactive)
  book remove <book_id>       Remove a book
  book get <book_id>          View book details
  book list                   List all books
  book search [title|author|tag] <value>   Search books

USER COMMANDS:
  user add                    Add a new user (interactive)
  user update <user_id>       Update user (name/email/max_loans)
  user get <user_id>          View user details
  user list                   List all users
  user activate <user_id>     Activate user
  user deactivate <user_id>   Deactivate user
  user ban <user_id>          Ban user

TRANSACTION COMMANDS:
  borrow <user_id> <book_id>  Borrow a book
  return <tx_id>              Return a book

LOAN QUERIES:
  loans active                Show all active loans
  loans overdue               Show overdue loans
  loans user <user_id>        Show user's loan history

REPORTS:
  report summary              Show system summary
  report user <user_id>       Show user transaction report

SYSTEM:
  save                        Save all data to CSV files
  help                        Show this help
  exit                        Exit the program
    """
    print(help_text)


def main():
    print("Library Management System (LMS)")
    print("Type 'help' for command list, 'exit' to quit.\n")
    
    lib = Library()

    while True:
        try:
            command = input("lms> ").strip()
            if not command:
                continue

            parts = command.split()
            action = parts[0].lower()

          
            if action == "book":
                if len(parts) < 2:
                    print("Usage: book <add|update|remove|get|list|search>")
                    continue
                sub = parts[1].lower()

                # Add Book
                if sub == "add":
                    print("=== Add New Book ===")
                    book_id = safe_input("Book ID: ")
                    title = safe_input("Title: ")
                    authors_input = safe_input("Authors (comma-separated): ")
                    authors = [a.strip() for a in authors_input.split(",") if a.strip()]
                    isbn = safe_input("ISBN (optional): ", allow_empty=True)
                    tags_input = safe_input("Tags (comma-separated, optional): ", allow_empty=True)
                    tags = [t.strip() for t in tags_input.split(",") if t.strip()]
                    total_copies = safe_input("Total Copies: ", type_cast=int)

                    lib.add_book(book_id, title, authors, isbn, tags, total_copies)
                    print(f"Book '{title}' added successfully with ID: {book_id}")

                # Update Book
                elif sub == "update" and len(parts) >= 3:
                    book_id = parts[2]
                    book = lib.get_book(book_id)
                    print(f"=== Updating Book: {book.title} ===")
                    print("Leave blank to keep current value.")

                    new_title = input(f"Title [{book.title}]: ").strip()
                    new_authors = input(f"Authors [{', '.join(book.authors)}]: ").strip()    
                    new_isbn = input(f"ISBN [{book.isbn}]: ").strip()
                    new_tags = input(f"Tags [{', '.join(book.tags)}]: ").strip()
                    new_copies = input(f"Total Copies [{book.total_copies}]: ").strip()

                    updates = {}
                    if new_title:
                        updates["title"] = new_title
                    if new_authors:
                        updates["author"] = [a.strip() for a in new_authors.split(",")]
                    if new_isbn:
                        updates["isbn"] = new_isbn
                    if new_tags:
                        updates["tags"] = [t.strip() for t in new_tags.split(",")]
                    if new_copies:
                        updates["total_copies"] = int(new_copies)

                    lib.update_book(book_id, **updates)
                    print("Book updated successfully.")

                # Remove Book
                elif sub == "remove" and len(parts) >= 3:
                    book_id = parts[2]
                    book = lib.get_book(book_id)
                    confirm = input(f"Remove book '{book.title}' (ID: {book_id})? [y/N]: ").strip().lower()
                    if confirm == 'y':
                        lib.remove_book(book_id)
                        print("Book removed.")
                    else:
                        print("Removal cancelled.")

                # Get Book Details
                elif sub == "get" and len(parts) >= 3:
                    book = lib.get_book(parts[2])
                    print(f"\n--- Book Details ---")
                    print(f"ID: {book.book_id}")
                    print(f"Title: {book.title}")
                    print(f"Authors: {', '.join(book.authors)}") 
                    print(f"Tags: {', '.join(book.tags)}")
                    print(f"Available: {book.available_copies} / {book.total_copies}")
                    print(f"Status: {'Available' if book.is_available() else 'Not Available'}")

                # List Books
                elif sub == "list":
                    books = lib.list_books()
                    if not books:
                        print("No books in library.")
                    else:
                        print(f"\n=== All Books ({len(books)}) ===")
                        for b in books:
                            status = "Available" if b.is_available() else "Not Available"
                            print(f"{b.book_id}: {b.title} [{b.available_copies}/{b.total_copies}] [{status}]")

                # Search Books
                elif sub == "search" and len(parts) >= 4:
                    field = parts[2].lower()
                    value = " ".join(parts[3:]).lower()
                    results = []
                    if field == "title":
                        results = lib.search_books(title=value)
                    elif field == "author":
                        results = lib.search_books(author=value)
                    elif field == "tag":
                        results = lib.search_books(tag=value)
                    else:
                        print("Search field must be: title, author, or tag")
                        continue

                    if not results:
                        print("No matching books found.")
                    else:
                        print(f"\n=== Search Results ({len(results)}) ===")
                        for b in results:
                            print(f"{b.book_id}: {b.title}")

                else:
                    print("Usage: book add | update <id> | remove <id> | get <id> | list | search [title|author|tag] <value>")

       
            elif action == "user":
                if len(parts) < 2:
                    print("Usage: user <add|update|get|list|activate|deactivate|ban>")
                    continue
                sub = parts[1].lower()

                # Add User
                if sub == "add":
                    print("=== Add New User ===")
                    user_id = safe_input("User ID: ")
                    name = safe_input("Name: ")
                    email = safe_input("Email (optional): ", allow_empty=True)
                    lib.add_user(user_id, name, email or None)
                    print(f"User '{name}' added with ID: {user_id}")

                # Update User
                elif sub == "update" and len(parts) >= 3:
                    user_id = parts[2]
                    user = lib.get_user(user_id)
                    print(f"=== Updating User: {user.name} ===")
                    print("Leave blank to keep current value.")

                    new_name = input(f"Name [{user.name}]: ").strip()
                    new_email = input(f"Email [{user.email or 'None'}]: ").strip()
                    new_max = input(f"Max Loans [{user.max_loans}]: ").strip()

                    updates = {}
                    if new_name:
                        updates["name"] = new_name
                    if new_email:
                        updates["email"] = new_email
                    if new_max:
                        updates["max_loans"] = int(new_max)

                    lib.update_user(user_id, **updates)
                    print("User updated.")

                # Get User
                elif sub == "get" and len(parts) >= 3:
                    user = lib.get_user(parts[2])
                    active = sum(1 for t in lib.transactions if t.user_id == user.user_id and t.status == "borrowed")
                    print(f"\n--- User Details ---")
                    print(f"ID: {user.user_id}")
                    print(f"Name: {user.name}")
                    print(f"Email: {user.email or 'None'}")
                    print(f"Status: {user.status.upper()}")
                    print(f"Max Loans: {user.max_loans}")
                    print(f"Active Loans: {active}")

                # List Users
                elif sub == "list":
                    users = lib.list_users()
                    if not users:
                        print("No users registered.")
                    else:
                        print(f"\n=== All Users ({len(users)}) ===")
                        for u in users:
                            active = sum(1 for t in lib.transactions if t.user_id == u.user_id and t.status == "borrowed")
                            print(f"{u.user_id}: {u.name} [{u.status.upper()}] (Loans: {active}/{u.max_loans})")

                # Status Change
                elif sub in ("activate", "deactivate", "ban") and len(parts) >= 3:
                    user_id = parts[2]
                    user = lib.get_user(user_id)
                    if sub == "activate":
                        user.activate()
                    elif sub == "deactivate":
                        user.deactivate()
                    elif sub == "ban":
                        user.ban()
                    print(f"User {user_id} is now {user.status.upper()}.")

                else:
                    print("Usage: user add | update <id> | get <id> | list | activate|deactivate|ban <id>")

           
            elif action == "borrow" and len(parts) >= 3:
                user_id, book_id = parts[1], parts[2]
                tx = lib.borrow_book(user_id, book_id)
                print(f"Borrow successful!")
                print(f"Transaction ID: {tx.tx_id}")
                print(f"Due Date: {tx.due_date}")

            elif action == "return" and len(parts) >= 2:
                tx_id = parts[1]
                lib.return_book(tx_id)
                print("Book returned successfully.")

            
            elif action == "loans":
                if len(parts) < 2:
                    print("Usage: loans active | overdue | user <id>")
                    continue
                sub = parts[1].lower()

                if sub == "active":
                    active = lib.active_loans()
                    if not active:
                        print("No active loans.")
                    else:
                        print(f"\n=== Active Loans ({len(active)}) ===")
                        for t in active:
                            print(f"{t.tx_id}: {t.book_id} → {t.user_id} | Due: {t.due_date}")

                elif sub == "overdue":
                    overdue = lib.overdue_loans()
                    if not overdue:
                        print("No overdue loans.")
                    else:
                        print(f"\n=== OVERDUE LOANS ({len(overdue)}) ===")
                        for t in overdue:
                            print(f"{t.tx_id}: {t.book_id} → {t.user_id} | Due: {t.due_date}")

                elif sub == "user" and len(parts) >= 3:
                    user_id = parts[2]
                    history = lib.user_loan_history(user_id)
                    user = lib.get_user(user_id)
                    if not history:
                        print(f"No loan history for user {user_id}.")
                    else:
                        print(f"\n=== Loan History: {user.name} ({user_id}) ===")
                        today = get_today_str()
                        for t in history:
                            status = t.status.upper()
                            if t.status == "borrowed" and t.is_overdue(today):
                                status = "OVERDUE"
                            print(f"{t.tx_id} | {t.book_id} | {t.borrow_date.strftime('%d-%m-%Y')} → {t.due_date} | {status}")

            elif action == "report":
                if len(parts) < 2:
                    print("Usage: report summary | user <id>")
                    continue
                sub = parts[1].lower()

                if sub == "summary":
                    r = lib.summary_report()
                    print(f"\n=== Library Summary ===")
                    print(f"Total Books: {r['total_books']}")
                    print(f"Total Users: {r['total_users']}")
                    print(f"Active Loans: {r['active_loans']}")
                    print(f"Overdue Loans: {r['overdue_loans']}")

                elif sub == "user" and len(parts) >= 3:
                    user_id = parts[2]
                    rep = lib.user_history_report(user_id)
                    user = rep["user"]
                    print(f"\n=== Transaction Report: {user.name} ({user_id}) ===")
                    for t in rep["transactions"]:
                        status = t.status.upper()
                        if t.status == "borrowed" and t.is_overdue(get_today_str()):
                            status = "OVERDUE"
                        print(f"{t.tx_id} | {t.book_id} | {t.borrow_date.strftime('%d-%m-%Y')} → {t.due_date} | {status}")
                    if rep["overdue"]:
                        print(f"\nOverdue: {len(rep['overdue'])} item(s)")

            
            elif action == "save":
                lib.save_all()
                print("All data saved to CSV files successfully.")

            elif action == "help":
                print_help()

            elif action == "exit":
                confirm = input("Save before exit? [Y/n]: ").strip().lower()
                if confirm != 'n':
                    lib.save_all()
                    print("Data saved.")
                print("Goodbye!")
                sys.exit(0)

            else:
                print("Unknown command. Type 'help' for list.")

        except (InvalidBookError, InvalidUserError, BookNotAvailableError,
                UserNotAllowedError, TransactionError, ValidationError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            
if __name__ == "__main__":
    main()