import sys
from library import Library
from models import (
    InvalidBookError, InvalidUserError, BookNotAvailableError,
    UserNotAllowedError, TransactionError, ValidationError
)
from models import Book, User
from utils import parse_comma_list, input_nonempty


def print_book(book):
    print(f"[{book.book_id}] {book.title}")
    print(f"  Authors: {', '.join(book.authors)}")
    print(f"  ISBN: {book.isbn}")
    print(f"  Tags: {', '.join(book.tags)}")
    print(f"  Copies: {book.available_copies}/{book.total_copies}")


def print_user(user):
    print(f"[{user.user_id}] {user.name}")
    print(f"  Email: {user.email}")
    print(f"  Status: {user.status}")
    print(f"  Max Loans: {user.max_loans}")


def print_tx(tx):
    print(f"[{tx.tx_id}] User={tx.user_id}, Book={tx.book_id}")
    print(f"  Borrow: {tx.borrow_date}  Due: {tx.due_date}")
    print(f"  Return: {tx.return_date or '-'}")
    print(f"  Status: {tx.status}")


def main():
    lib = Library()

    while True:
        try:
            # ---------- Main Menu ----------
            print("\n" + "="*50)
            print("        LIBRARY MANAGEMENT SYSTEM")
            print("="*50)
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Borrow / Return Books")
            print("4. View Loans")
            print("5. View Reports")
            print("6. Save Changes")
            print("7. Exit")
            print("="*50)

            choice = input("Enter your choice (1-7): ").strip()

            # ---------- Exit ----------
            if choice == "7":
                print("Goodbye!")
                sys.exit(0)

            # ---------- Manage Books ----------
            elif choice == "1":
                print("\n--- Manage Books ---")
                print("1. Add Book")
                print("2. Update Book")
                print("3. Remove Book")
                print("4. Get Book")
                print("5. List Books")
                print("6. Search Books")
                sub = input("Choose an option (1-6): ").strip()

                if sub == "1":  # Add Book
                    book_id = input_nonempty("Book ID: ")
                    title = input_nonempty("Title: ")
                    authors = parse_comma_list(input("Authors (comma): "))
                    isbn = input("ISBN: ").strip()
                    tags = parse_comma_list(input("Tags (comma): "))
                    total = int(input_nonempty("Total Copies: "))
                    available = total
                    lib.add_book(Book(book_id, title, authors, isbn, tags, total, available))
                    print("Book added successfully.")

                elif sub == "2":  # Update Book
                    bid = input_nonempty("Book ID: ")
                    book = lib.get_book(bid)
                    print("Leave empty to skip.")
                    t = input("Title: ").strip()
                    a = input("Authors (comma): ").strip()
                    i = input("ISBN: ").strip()
                    tg = input("Tags (comma): ").strip()
                    tc = input("Total Copies: ").strip()

                    updates = {}
                    if t: updates["title"] = t
                    if a: updates["authors"] = parse_comma_list(a)
                    if i: updates["isbn"] = i
                    if tg: updates["tags"] = parse_comma_list(tg)
                    if tc: updates["total_copies"] = int(tc)

                    lib.update_book(bid, **updates)
                    print("Book updated.")

                elif sub == "3":  # Remove Book
                    bid = input_nonempty("Book ID: ")
                    lib.remove_book(bid)
                    print("Book removed.")

                elif sub == "4":  # Get Book
                    bid = input_nonempty("Book ID: ")
                    print_book(lib.get_book(bid))

                elif sub == "5":  # List Books
                    books = lib.list_books()
                    if not books:
                        print("No books available.")
                    else:
                        for b in books:
                            print_book(b)

                elif sub == "6":  # Search Books
                    t = input("Title contains: ").strip()
                    a = input("Author: ").strip()
                    tg = input("Tag: ").strip()
                    results = lib.search_books(t, a, tg)
                    if not results:
                        print("No results.")
                    else:
                        for b in results:
                            print_book(b)

                else:
                    print("Invalid option.")

            # ---------- Manage Users ----------
            elif choice == "2":
                pwd = input("Enter password to access Users section: ").strip()
                if pwd != "user123":
                    print("Invalid credentials. Returning to main menu...")
                    continue  # Go back to main menu
                else:
                     print("Authentication successfull!!")


                print("\n--- Manage Users ---")
                print("1. Add User")
                print("2. Update User")
                print("3. Get User")
                print("4. List Users")
                print("5. Change User Status")
                print("6. Report User")
                sub = input("Choose an option (1-6): ").strip()

                if sub == "1": # Add User
                    uid = input_nonempty("User ID: ")
                    name = input_nonempty("Name: ")
                    email = input("Email: ").strip()
                    if not email.endswith("@ust.com"):
                        print("Invalid email. Returning to Main menu.")
                        continue 
                    lib.add_user(User(uid, name, email,max_loans=0))
                    print("User added.")

                elif sub == "2":  # Update User
                    pwd = input("Enter password to access Users section: ").strip()
                    if pwd != "user123":
                        print("Invalid credentials. Returning to main menu...")
                        continue  # Go back to main menu
                    else:
                     print("Authentication successfull!!")
                     uid = input_nonempty("User ID: ")
                     user = lib.get_user(uid)
                     print("Leave empty to skip.")
                     name = input("Name: ").strip()
                     email = input("Email: ").strip()
                     ml = input("Max Loans: ").strip()

                     updates = {}
                     if name: updates["name"] = name
                     if email: updates["email"] = email
                     if ml: updates["max_loans"] = int(ml)

                     lib.update_user(uid, **updates)
                     print("User updated.")

                elif sub == "3":  # Get User
                    pwd = input("Enter password to access Users section: ").strip()
                    if pwd != "user123":
                        print("Invalid credentials. Returning to main menu...")
                        continue  # Go back to main menu
                    else:
                     print("Authentication successfull!!")

                     users = lib.list_users()
                     if not users:
                         print("No users found.")
                     else:
                         for u in users:
                             print_user(u)
                     uid = input_nonempty("Enter User ID to view details: ")
                     print_user(lib.get_user(uid))

                elif sub == "4":  # List Users
                    pwd = input("Enter password to access Users section: ").strip()
                    if pwd != "user123":
                        print("Invalid credentials. Returning to main menu...")
                        continue  # Go back to main menu
                    else:
                     print("Authentication successfull!!")
                     users = lib.list_users()
                     if not users:
                         print("No users found.")
                     else:
                         for u in users:
                             print_user(u)

                elif sub == "5":  # Change Status
                    pwd = input("Enter password to access Users section: ").strip()
                    if pwd != "user123":
                        print("Invalid credentials. Returning to main menu...")
                        continue  # Go back to main menu
                    else:
                     print("Authentication successfull!!")
                     uid = input_nonempty("User ID: ")
                     print("1=activate, 2=deactivate, 3=ban")
                     opt = input("Status: ").strip()
                     status = {"1": "activate", "2": "deactivate", "3": "ban"}.get(opt)
                     if not status:
                         print("Invalid status.")
                     else:
                         lib.set_user_status(uid, status)
                         print("Status updated.")

                elif sub == "6":  # Report User
                    uid = input_nonempty("User ID: ")
                    items = lib.report_user(uid)
                    if not items:
                        print("No transactions.")
                    else:
                        for tx in items:
                            print_tx(tx)

                else:
                    print("Invalid option.")

            # ---------- Borrow / Return ----------
            elif choice == "3":
                print("\n1. Borrow Book\n2. Return Book")
                sub = input("Choose: ").strip()
                if sub == "1":
                    uid = input_nonempty("User ID: ")
                    bid = input_nonempty("Book ID: ")
                    tx = lib.borrow_book(uid, bid)
                    print(f"Borrow successful. Transaction ID: {tx.tx_id}")
                elif sub == "2":
                    txid = input_nonempty("Transaction ID: ")
                    lib.return_book(txid)
                    print("Book returned.")
                else:
                    print("Invalid option.")

            # ---------- View Loans ----------
            elif choice == "4":
                print("\n1. Active Loans\n2. Overdue Loans\n3. Loans by User")
                sub = input("Choose: ").strip()
                if sub == "1":
                    loans = lib.loans_active()
                elif sub == "2":
                    loans = lib.loans_overdue()
                elif sub == "3":
                    uid = input_nonempty("User ID: ")
                    loans = lib.loans_user(uid)
                else:
                    print("Invalid option.")
                    continue

                if not loans:
                    print("No loans found.")
                else:
                    for tx in loans:
                        print_tx(tx)

            # ---------- View Reports ----------
            elif choice == "5":
                print("\n1. Summary Report\n2. User Report")
                sub = input("Choose: ").strip()
                if sub == "1":
                    r = lib.report_summary()
                    for k, v in r.items():
                        print(f"{k}: {v}")
                elif sub == "2":
                    uid = input_nonempty("User ID: ")
                    items = lib.report_user(uid)
                    if not items:
                        print("No transactions.")
                    else:
                        for tx in items:
                            print_tx(tx)
                else:
                    print("Invalid option.")

            # ---------- Save Changes ----------
            elif choice == "6":
                lib.save_all()
                print("Data saved successfully.")

            else:
                print("Invalid choice.")

        except (
            InvalidBookError, InvalidUserError,
            BookNotAvailableError, UserNotAllowedError,
            TransactionError, ValidationError, ValueError
        ) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()
