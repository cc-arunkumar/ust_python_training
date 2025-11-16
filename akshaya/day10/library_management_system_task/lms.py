# lms.py
import sys
from akshaya.day10.library_management_system_task.models import Book, User, Transaction, InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError
from akshaya.day10.library_management_system_task.library import Library
from akshaya.day10.library_management_system_task.utils import parse_comma_list, input_nonempty

def print_book(book):
    print(f"[{book.book_id}] {book.title}")
    print(f"  Authors: {', '.join(book.authors) if book.authors else '-'}")
    print(f"  ISBN: {book.isbn or '-'}")
    print(f"  Tags: {', '.join(book.tags) if book.tags else '-'}")
    print(f"  Copies: {book.available_copies}/{book.total_copies}")

def print_user(user):
    print(f"[{user.user_id}] {user.name}")
    print(f"  Email: {user.email or '-'}")
    print(f"  Status: {user.status}")
    print(f"  Max Loans: {user.max_loans}")

def print_tx(tx):
    print(f"[{tx.tx_id}] User={tx.user_id}, Book={tx.book_id}")
    print(f"  Borrow: {tx.borrow_date}  Due: {tx.due_date}")
    print(f"  Return: {tx.return_date or '-'}")
    print(f"  Status: {tx.status}")

def main():
    lib = Library()
    ADMIN_PWD = "user123"  # password used in prompts

    while True:
        try:
            print("\n" + "="*48)
            print("        LIBRARY MANAGEMENT SYSTEM")
            print("="*48)
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Borrow / Return Books")
            print("4. View Loans")
            print("5. View Reports")
            print("6. Save Changes")
            print("7. Exit")
            print("="*48)

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "7":
                # Ensure data is saved before exit
                lib.save_all()
                print("Goodbye!")
                sys.exit(0)

            # ---------------- Manage Books ----------------
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
                    try:
                        book_id = input_nonempty("Book ID: ")
                        title = input_nonempty("Title: ")
                        authors = parse_comma_list(input("Authors (comma): "))
                        isbn = input("ISBN: ").strip()
                        tags = parse_comma_list(input("Tags (comma): "))
                        total = int(input_nonempty("Total Copies: "))
                        available = total
                        lib.add_book(Book(book_id, title, authors, isbn, tags, total, available))
                        lib.save_all()  # Save after adding book
                        print("Book added successfully.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "2":  # Update Book
                    try:
                        bid = input_nonempty("Book ID: ")
                        book = lib.get_book(bid)
                        print("\nCurrent details:")
                        print_book(book)
                        print("\nEnter new values (leave empty to skip):")
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
                        lib.save_all()  # Save after updating book
                        print("Book updated successfully.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "3":  # Remove Book (soft delete)
                    try:
                        bid = input_nonempty("Book ID: ")
                        book = lib.get_book(bid)
                        print("\nAbout to remove (soft-delete) this book:")
                        print_book(book)
                        confirm = input("Type YES to confirm removal: ").strip()
                        if confirm == "YES":
                            lib.remove_book(bid)
                            lib.save_all()  # Save after removing book
                            print("Book soft-deleted successfully.")
                        else:
                            print("Removal cancelled.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "4":  # Get Book
                    try:
                        bid = input_nonempty("Book ID: ")
                        b = lib.get_book(bid)
                        print_book(b)
                    except Exception as e:
                        print(f"Error: {e}")

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

            # ---------------- Manage Users ----------------
            elif choice == "2":
                pwd = input("Enter password to access Users section: ").strip()
                if pwd != ADMIN_PWD:
                    print("Invalid credentials. Returning to main menu...")
                    continue
                print("Authentication successful.")

                print("\n--- Manage Users ---")
                print("1. Add User")
                print("2. Update User")
                print("3. Get User")
                print("4. List Users")
                print("5. Change User Status")
                print("6. Report User Transactions")
                sub = input("Choose an option (1-6): ").strip()

                if sub == "1": # Add User
                    try:
                        uid = input_nonempty("User ID: ")
                        name = input_nonempty("Name: ")
                        email = input("Email: ").strip()
                        if email and not email.endswith("@ust.com"):
                            print("Warning: email not ending with @ust.com — still accepted.")
                        ml = input("Max Loans (default 0): ").strip()
                        ml_val = int(ml) if ml else 0  # Default to 0 if left empty
                        lib.add_user(User(uid, name, email, "active", ml_val))
                        lib.save_all()  # Save after adding user
                        print("User added.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "2":  # Update User
                    try:
                        uid = input_nonempty("User ID: ")
                        user = lib.get_user(uid)
                        print("\nCurrent details:")
                        print_user(user)
                        print("\nEnter new values (leave empty to skip):")
                        name = input("Name: ").strip()
                        email = input("Email: ").strip()
                        ml = input("Max Loans: ").strip()

                        updates = {}
                        if name: updates["name"] = name
                        if email: updates["email"] = email
                        if ml: updates["max_loans"] = int(ml)

                        lib.update_user(uid, **updates)
                        lib.save_all()  # Save after updating user
                        print("User updated successfully.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "3":  # Get User
                    try:
                        uid = input_nonempty("User ID: ")
                        print_user(lib.get_user(uid))
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "4":  # List Users
                    users = lib.list_users()
                    if not users:
                        print("No users found.")
                    else:
                        for u in users:
                            print_user(u)

                elif sub == "5":  # Change Status
                    try:
                        uid = input_nonempty("User ID: ")
                        print("1=activate, 2=deactivate, 3=ban")
                        opt = input("Status option: ").strip()
                        status = {"1": "activate", "2": "deactivate", "3": "ban"}.get(opt)
                        if not status:
                            print("Invalid option.")
                        else:
                            lib.set_user_status(uid, status)
                            lib.save_all()  # Save after updating status
                            print("Status updated.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "6":  # Report User
                    try:
                        uid = input_nonempty("User ID: ")
                        items = lib.report_user(uid)
                        if not items:
                            print("No transactions.")
                        else:
                            for tx in items:
                                print_tx(tx)
                    except Exception as e:
                        print(f"Error: {e}")

                else:
                    print("Invalid option.")

            # ---------------- Borrow / Return ----------------
            elif choice == "3":
                print("\n1. Borrow Book\n2. Return Book")
                sub = input("Choose: ").strip()
                if sub == "1":
                    try:
                        uid = input_nonempty("User ID: ")
                        print("\nAvailable books (not borrowed / not deleted):")
                        avail = [b for b in lib.list_books() if b.is_available()]
                        if not avail:
                            print("No books available for borrowing.")
                            continue
                        for b in avail:
                            print_book(b)
                        bid = input_nonempty("Book ID to borrow: ")
                        print("\nAbout to borrow:")
                        print_book(lib.get_book(bid))
                        confirm = input("Type YES to confirm borrow: ").strip()
                        if confirm == "YES":
                            tx = lib.borrow_book(uid, bid)
                            print(f"Borrow successful. Transaction ID: {tx.tx_id}  Due: {tx.due_date}")
                        else:
                            print("Borrow cancelled.")
                    except Exception as e:
                        print(f"Error: {e}")

                elif sub == "2":
                    try:
                        txid = input_nonempty("Transaction ID: ")
                        # show tx details first
                        tx = next((t for t in lib.transactions if t.tx_id == txid), None)
                        if not tx:
                            print("Transaction not found.")
                            continue
                        print("Transaction details:")
                        print_tx(tx)
                        if tx.status != "borrowed":
                            print("This transaction is not borrowed; cannot return.")
                            continue
                        confirm = input("Type YES to confirm return: ").strip()
                        if confirm == "YES":
                            lib.return_book(txid)
                            print("Book returned successfully.")
                        else:
                            print("Return cancelled.")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid option.")

            # ---------------- View Loans ----------------
            elif choice == "4":
                print("\n1. Active Loans\n2. Overdue Loans\n3. Loans by User")
                sub = input("Choose: ").strip()
                if sub == "1":
                    loans = lib.loans_active()
                elif sub == "2":
                    loans = lib.loans_overdue()
                elif sub == "3":
                    try:
                        uid = input_nonempty("User ID: ")
                        loans = lib.loans_user(uid)
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                else:
                    print("Invalid option.")
                    continue

                if not loans:
                    print("No loans found.")
                else:
                    for tx in loans:
                        print_tx(tx)

            # ---------------- View Reports ----------------
            elif choice == "5":
                print("\n1. Summary Report\n2. User Report")
                sub = input("Choose: ").strip()
                if sub == "1":
                    r = lib.report_summary()
                    for k, v in r.items():
                        print(f"{k}: {v}")
                elif sub == "2":
                    try:
                        uid = input_nonempty("User ID: ")
                        items = lib.report_user(uid)
                        if not items:
                            print("No transactions.")
                        else:
                            for tx in items:
                                print_tx(tx)
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid option.")

            # ---------------- Save Changes ----------------
            elif choice == "6":
                try:
                    lib.save_all()
                    print("Data saved successfully.")
                except Exception as e:
                    print(f"Error saving data: {e}")

            else:
                print("Invalid choice.")

        except (InvalidBookError, InvalidUserError, BookNotAvailableError,
                UserNotAllowedError, TransactionError, ValidationError, ValueError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            try:
                lib.save_all()
                print("Data saved before exit.")
            except Exception:
                pass
            sys.exit(0)

if __name__ == "__main__":
    main()
