# lms.py
import sys
from models import Book, User, InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError
from library import Library
from storage import CSVStorage
from utils import split_comma

HELP_TEXT = """
Commands:
  book add
  book update <book_id>
  book remove <book_id>
  book get <book_id>
  book list
  book search title <substr>
  book search author <name>
  book search tag <tag>

  user add
  user update <user_id>
  user get <user_id>
  user list
  user deactivate <user_id>
  user activate <user_id>
  user ban <user_id>

  borrow <user_id> <book_id>
  return <transaction_id>

  loans active
  loans overdue
  loans user <user_id>

  report summary
  report user <user_id>

  save
  help
  exit
"""

def prompt(msg):
    return input(f"{msg}: ").strip()

def print_book(b: Book):
    print(f"- ID: {b.book_id} | Title: {b.title} | Authors: {', '.join(b.authors)} | ISBN: {b.isbn} | Tags: {', '.join(b.tags)} | Total: {b.total_copies} | Available: {b.available_copies}")

def print_user(u: User):
    print(f"- ID: {u.user_id} | Name: {u.name} | Email: {u.email or ''} | Status: {u.status} | Max Loans: {u.max_loans}")

def print_tx(t):
    print(f"- TX: {t.tx_id} | User: {t.user_id} | Book: {t.book_id} | Borrow: {t.borrow_date} | Due: {t.due_date} | Return: {t.return_date or ''} | Status: {t.status}")

def main():
    lib = Library(CSVStorage())
    print("lms> type 'help' for commands.")
    while True:
        try:
            cmd = input("lms> ").strip()
            if not cmd:
                continue
            parts = cmd.split()
            if parts[0] == "help":
                print(HELP_TEXT)

            elif parts[0] == "exit":
                print("Goodbye.")
                break

            elif parts[0] == "save":
                lib.save_all()
                print("All data saved to CSV successfully.")

            # --- Book commands ---
            elif parts[0] == "book" and len(parts) >= 2:
                sub = parts[1]

                if sub == "add":
                    book_id = prompt("Book ID")
                    title = prompt("Title")
                    authors_in = prompt("Authors (comma separated)")
                    isbn = prompt("ISBN")
                    tags_in = prompt("Tags (comma separated)")
                    total = prompt("Total Copies")
                    try:
                        total = int(total)
                    except:
                        print("Invalid total copies.")
                        continue
                    book = Book(
                        book_id=book_id,
                        title=title,
                        authors=split_comma(authors_in),
                        isbn=isbn,
                        tags=split_comma(tags_in),
                        total_copies=total,
                        available_copies=total
                    )
                    try:
                        lib.add_book(book)
                        print("Book added successfully.")
                    except (ValidationError, InvalidBookError) as e:
                        print(f"Error: {e}")

                elif sub == "update" and len(parts) == 3:
                    book_id = parts[2]
                    print("Leave fields blank to skip updating.")
                    title = prompt("Title")
                    authors_in = prompt("Authors (comma separated)")
                    isbn = prompt("ISBN")
                    tags_in = prompt("Tags (comma separated)")
                    total = prompt("Total Copies")
                    avail = prompt("Available Copies")
                    kwargs = {}
                    if title: kwargs["title"] = title
                    if authors_in: kwargs["authors"] = split_comma(authors_in)
                    if isbn: kwargs["isbn"] = isbn
                    if tags_in: kwargs["tags"] = split_comma(tags_in)
                    if total: kwargs["total_copies"] = int(total)
                    if avail: kwargs["available_copies"] = int(avail)
                    try:
                        lib.update_book(book_id, **kwargs)
                        print("Book updated.")
                    except (ValidationError, InvalidBookError) as e:
                        print(f"Error: {e}")

                elif sub == "remove" and len(parts) == 3:
                    book_id = parts[2]
                    try:
                        lib.remove_book(book_id)
                        print("Book removed.")
                    except InvalidBookError as e:
                        print(f"Error: {e}")

                elif sub == "get" and len(parts) == 3:
                    b = lib.get_book(parts[2])
                    if b:
                        print_book(b)
                    else:
                        print("Book not found.")

                elif sub == "list":
                    books = lib.list_books()
                    if not books:
                        print("No books.")
                    for b in books:
                        print_book(b)

                elif sub == "search" and len(parts) >= 4:
                    if parts[2] == "title":
                        res = lib.search_books(title_substr=" ".join(parts[3:]))
                    elif parts[2] == "author":
                        res = lib.search_books(author=" ".join(parts[3:]))
                    elif parts[2] == "tag":
                        res = lib.search_books(tag=" ".join(parts[3:]))
                    else:
                        print("Invalid search type.")
                        continue
                    if not res:
                        print("No matches.")
                    else:
                        for b in res:
                            print_book(b)
                else:
                    print("Invalid book command.")

            # --- User commands ---
            elif parts[0] == "user" and len(parts) >= 2:
                sub = parts[1]
                if sub == "add":
                    user_id = prompt("User ID")
                    name = prompt("Name")
                    email = prompt("Email")
                    try:
                        lib.add_user(User(user_id=user_id, name=name, email=email or None))
                        print("User added.")
                    except (ValidationError, InvalidUserError) as e:
                        print(f"Error: {e}")

                elif sub == "update" and len(parts) == 3:
                    user_id = parts[2]
                    print("Leave fields blank to skip updating.")
                    name = prompt("Name")
                    email = prompt("Email")
                    status = prompt("Status (active/inactive/banned)")
                    max_loans = prompt("Max Loans")
                    kwargs = {}
                    if name: kwargs["name"] = name
                    if email: kwargs["email"] = email
                    if status: kwargs["status"] = status
                    if max_loans: kwargs["max_loans"] = int(max_loans)
                    try:
                        lib.update_user(user_id, **kwargs)
                        print("User updated.")
                    except (ValidationError, InvalidUserError) as e:
                        print(f"Error: {e}")

                elif sub == "get" and len(parts) == 3:
                    u = lib.get_user(parts[2])
                    if u:
                        print_user(u)
                    else:
                        print("User not found.")

                elif sub == "list":
                    users = lib.list_users()
                    if not users:
                        print("No users.")
                    for u in users:
                        print_user(u)

                elif sub == "deactivate" and len(parts) == 3:
                    try:
                        lib.deactivate_user(parts[2])
                        print("User deactivated.")
                    except InvalidUserError as e:
                        print(f"Error: {e}")

                elif sub == "activate" and len(parts) == 3:
                    try:
                        lib.activate_user(parts[2])
                        print("User activated.")
                    except InvalidUserError as e:
                        print(f"Error: {e}")

                elif sub == "ban" and len(parts) == 3:
                    try:
                        lib.ban_user(parts[2])
                        print("User banned.")
                    except InvalidUserError as e:
                        print(f"Error: {e}")

                else:
                    print("Invalid user command.")

            # --- Borrow / Return ---
            elif parts[0] == "borrow" and len(parts) == 3:
                user_id, book_id = parts[1], parts[2]
                try:
                    tx = lib.borrow(user_id, book_id)
                    print(f"Borrow successful. Transaction ID: {tx.tx_id}. Due Date: {tx.due_date}.")
                except (InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, ValidationError) as e:
                    print(f"Error: {e}")

            elif parts[0] == "return" and len(parts) == 2:
                tx_id = parts[1]
                try:
                    tx = lib.return_book(tx_id)
                    print("Return successful.")
                except (TransactionError, InvalidBookError) as e:
                    print(f"Error: {e}")

            # --- Transaction queries ---
            elif parts[0] == "loans" and len(parts) >= 2:
                sub = parts[1]
                if sub == "active":
                    txs = lib.loans_active()
                    if not txs:
                        print("No active loans.")
                    else:
                        for t in txs:
                            print_tx(t)
                elif sub == "overdue":
                    txs = lib.loans_overdue()
                    if not txs:
                        print("No overdue loans.")
                    else:
                        for t in txs:
                            print_tx(t)
                elif sub == "user" and len(parts) == 3:
                    txs = lib.loans_user(parts[2])
                    if not txs:
                        print("No loans for user.")
                    else:
                        for t in txs:
                            print_tx(t)
                else:
                    print("Invalid loans command.")

            # --- Reports ---
            elif parts[0] == "report" and len(parts) >= 2:
                sub = parts[1]
                if sub == "summary":
                    s = lib.report_summary()
                    print(f"Total books: {s['total_books']}")
                    print(f"Total users: {s['total_users']}")
                    print(f"Active loans: {s['active_loans']}")
                    print(f"Overdue loans: {s['overdue_loans']}")
                elif sub == "user" and len(parts) == 3:
                    txs = lib.report_user(parts[2])
                    if not txs:
                        print("No transactions for user.")
                    else:
                        for t in txs:
                            overdue_mark = ""
                            # Mark overdue if due < today and not returned
                            from utils import parse_date, today_str
                            if t.status == "borrowed" and parse_date(t.due_date) < parse_date(today_str()):
                                overdue_mark = " [OVERDUE]"
                            print_tx(t)
                            if overdue_mark:
                                print(overdue_mark)
                else:
                    print("Invalid report command.")

            else:
                print("Unknown command. Type 'help'.")

        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye.")
            break
        except Exception as e:
            # Catch-all to prevent crash; keep message user-friendly
            print(f"Error: {e}")

if __name__ == "__main__":
    main()


#o/p:
# lms> type 'help' for commands.
# lms> book add
# Book ID: B1061
# Title: Python Basics
# Authors (comma separated): Mark Lutz
# ISBN: 900000223231
# Tags (comma separated): Programming,Python
# Total Copies: 4
# Book added successfully.
# lms> book get B1061
# - ID: B1061 | Title: Python Basics | Authors: Mark Lutz | ISBN: 900000223231 | Tags: Programming, Python | Total: 4 | Available: 4
# lms> user get U2002
# - ID: U2002 | Name: Riya Sharma | Email: riya.sharma@ust.com | Status: active | Max Loans: 5
# lms> user activate U2002
# User activated.
# lms> borrow U2002 B1061
# Borrow successful. Transaction ID: T22. Due Date: 11/29/2025.
# lms> loans active
# - TX: T3001 | User: U2001 | Book: B1001 | Borrow: 2025-10-01 | Due: 2025-10-15 | Return:  | Status: borrowed
# owed
# - TX: T3018 | User: U2025 | Book: B1012 | Borrow: 2025-11-04 | Due: 2025-11-18 | Return:  | Status: borrowed
# - TX: T3019 | User: U2009 | Book: B1005 | Borrow: 2025-11-05 | Due: 2025-11-19 | Return:  | Status: borrowed
# - TX: T3018 | User: U2025 | Book: B1012 | Borrow: 2025-11-04 | Due: 2025-11-18 | Return:  | Status: borrowed
# - TX: T3019 | User: U2009 | Book: B1005 | Borrow: 2025-11-05 | Due: 2025-11-19 | Return:  | Status: borrowed
# - TX: T22 | User: U2002 | Book: B1061 | Borrow: 11/15/2025 | Due: 11/29/2025 | Return:  | Status: borrowed
# lms> book get B1061
# - ID: B1061 | Title: Python Basics | Authors: Mark Lutz | ISBN: 900000223231 | Tags: Programming, Python | Total: 4 | Available: 3
# lms> save
# All data saved to CSV successfully.
# lms> return T22
# Return successful.
# lms> loans active
# - TX: T3001 | User: U2001 | Book: B1001 | Borrow: 2025-10-01 | Due: 2025-10-15 | Return:  | Status: borrowed
# - TX: T3004 | User: U2005 | Book: B1004 | Borrow: 2025-11-01 | Due: 2025-11-15 | Return:  | Status: borrowed
# - TX: T3007 | User: U2010 | Book: B1028 | Borrow: 2025-11-05 | Due: 2025-11-19 | Return:  | Status: borrowed
# - TX: T3008 | User: U2013 | Book: B1038 | Borrow: 2025-11-06 | Due: 2025-11-20 | Return:  | Status: borrowed
# - TX: T3010 | User: U2015 | Book: B1033 | Borrow: 2025-11-07 | Due: 2025-11-21 | Return:  | Status: borrowed
# - TX: T3012 | User: U2018 | Book: B1035 | Borrow: 2025-11-08 | Due: 2025-11-22 | Return:  | Status: borrowed
# - TX: T3014 | User: U2020 | Book: B1019 | Borrow: 2025-11-01 | Due: 2025-11-15 | Return:  | Status: borrowed
# - TX: T3016 | User: U2023 | Book: B1017 | Borrow: 2025-11-03 | Due: 2025-11-17 | Return:  | Status: borrowed
# - TX: T3018 | User: U2025 | Book: B1012 | Borrow: 2025-11-04 | Due: 2025-11-18 | Return:  | Status: borrowed
# - TX: T3019 | User: U2009 | Book: B1005 | Borrow: 2025-11-05 | Due: 2025-11-19 | Return:  | Status: borrowed
# lms> save
# All data saved to CSV successfully.
# lms> report summary
# Error: time data '2025-10-15' does not match format '%m/%d/%Y'
# lms> report summary
# Error: time data '2025-10-15' does not match format '%m/%d/%Y'
# lms> exit
# Goodbye.



