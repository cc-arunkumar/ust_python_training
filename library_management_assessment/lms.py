# lms.py
from library import (
    Library,
    InvalidBookError,
    InvalidUserError,
    BookNotAvailableError,
    UserNotAllowedError,
    TransactionError,
    ValidationError
)
from models import Book, User,Transaction
from utils import parse_csv_list, safe_int, print_book, print_user, print_tx,today_str

def print_help():
    print("Commands:")
    print("  book add")
    print("  book update <book_id>")
    print("  book remove <book_id>")
    print("  book get <book_id>")
    print("  book list")
    print("  book search title=<substr> author=<name> tag=<tag>")
    print("  user add")
    print("  user update <user_id>")
    print("  user get <user_id>")
    print("  user list")
    print("  user deactivate <user_id>")
    print("  user activate <user_id>")
    print("  user ban <user_id>")
    print("  borrow <user_id> <book_id>")
    print("  return <transaction_id>")
    print("  loans active")
    print("  loans overdue")
    print("  loans user <user_id>")
    print("  report summary")
    print("  report user <user_id>")
    print("  save")
    print("  help")
    print("  exit")

def main():
    lib = Library()
    print("Welcome to Library Management System (LMS)")
    print("Type 'help' for commands.")
    while True:
        try:
            raw = input("lms> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not raw:
            continue
        parts = raw.split()
        cmd = parts[0].lower()

        try:
            if cmd == "help":
                print_help()

            # ---------------- BOOK COMMANDS ----------------
            elif cmd == "book":
                if len(parts) < 2:
                    print("Usage: book <add|update|get|remove|list|search>")
                    continue
                sub = parts[1].lower()

                if sub == "add":
                    book_id = input("Book ID: ").strip()
                    title = input("Title: ").strip()
                    authors_raw = input("Authors (comma separated): ").strip()
                    isbn = input("ISBN: ").strip()
                    tags_raw = input("Tags (comma separated): ").strip()
                    total = safe_int("Total Copies: ")
                    book = Book(
                        book_id,
                        title,
                        parse_csv_list(authors_raw, ","),
                        isbn,
                        parse_csv_list(tags_raw, ","),
                        total,
                        total
                    )
                    lib.add_book(book)
                    print("Book added successfully.")

                elif sub == "update":
                    if len(parts) < 3:
                        print("Usage: book update <book_id>")
                        continue
                    book_id = parts[2]
                    print("Leave fields empty to keep current values.")
                    title = input("Title: ").strip()
                    authors_raw = input("Authors (comma separated): ").strip()
                    isbn = input("ISBN: ").strip()
                    tags_raw = input("Tags (comma separated): ").strip()
                    total_raw = input("Total Copies: ").strip()
                    available_raw = input("Available Copies: ").strip()

                    payload = {}
                    if title:
                        payload["title"] = title
                    if authors_raw:
                        payload["authors"] = parse_csv_list(authors_raw, ",")
                    if isbn:
                        payload["isbn"] = isbn
                    if tags_raw:
                        payload["tags"] = parse_csv_list(tags_raw, ",")
                    if total_raw:
                        payload["total_copies"] = int(total_raw)
                    if available_raw:
                        payload["available_copies"] = int(available_raw)

                    book = lib.update_book(book_id, **payload)
                    print("Book updated successfully.")
                    print_book(book)

                elif sub == "remove":
                    if len(parts) < 3:
                        print("Usage: book remove <book_id>")
                        continue
                    lib.remove_book(parts[2])
                    print("Book removed successfully.")

                elif sub == "get":
                    if len(parts) < 3:
                        print("Usage: book get <book_id>")
                        continue
                    book = lib.get_book(parts[2])
                    print_book(book)

                elif sub == "list":
                    books = lib.list_books()
                    if not books:
                        print("No books found.")
                    else:
                        for b in books:
                            print_book(b)

                elif sub == "search":
                    title = None
                    author = None
                    tag = None
                    for token in parts[2:]:
                        if token.startswith("title="):
                            title = token.split("=", 1)[1]
                        elif token.startswith("author="):
                            author = token.split("=", 1)[1]
                        elif token.startswith("tag="):
                            tag = token.split("=", 1)[1]
                    results = lib.search_books(title_substr=title, author=author, tag=tag)
                    if not results:
                        print("No matching books.")
                    else:
                        for b in results:
                            print_book(b)

            # ---------------- USER COMMANDS ----------------
            elif cmd == "user":
                if len(parts) < 2:
                    print("Usage: user <add|update|get|list|deactivate|activate|ban>")
                    continue
                sub = parts[1].lower()

                if sub == "add":
                    user_id = input("User ID: ").strip()
                    name = input("Name: ").strip()
                    email = input("Email: ").strip()
                    max_loans_input = input("Max Loans (default=5): ").strip()
                    max_loans = int(max_loans_input) if max_loans_input else 5
                    user = User(user_id, name, email, "active", max_loans)
                    lib.add_user(user)
                    print("User added.")

                elif sub == "update":
                    if len(parts) < 3:
                        print("Usage: user update <user_id>")
                        continue
                    user_id = parts[2]
                    print("Leave fields empty to keep current values.")
                    name = input("Name: ").strip()
                    email = input("Email: ").strip()
                    status = input("Status (active/inactive/banned): ").strip()
                    max_loans = input("Max Loans: ").strip()
                    payload = {}
                    if name:
                        payload["name"] = name
                    if email:
                        payload["email"] = email
                    if status:
                        payload["status"] = status
                    if max_loans:
                        payload["max_loans"] = int(max_loans)
                    user = lib.update_user(user_id, **payload)
                    print("User updated successfully.")
                    print_user(user)

                elif sub == "get":
                    if len(parts) < 3:
                        print("Usage: user get <user_id>")
                        continue
                    user = lib.get_user(parts[2])
                    print_user(user)

                elif sub == "list":
                    users = lib.list_users()
                    if not users:
                        print("No users found.")
                    else:
                        for u in users:
                            print_user(u)

                elif sub in {"deactivate", "activate", "ban"}:
                    if len(parts) < 3:
                        print(f"Usage: user {sub} <user_id>")
                        continue
                    user = lib.set_user_status(parts[2], sub)
                    print(f"User {sub}d successfully.")
                    print_user(user)

            # ---------------- BORROW / RETURN ----------------
            elif cmd == "borrow":
                if len(parts) < 3:
                    print("Usage: borrow <user_id> <book_id>")
                    continue
                tx = lib.borrow_book(parts[1], parts[2])
                print(f"Borrow successful. Transaction ID: {tx.tx_id}. Due Date: {tx.due_date}.")

            elif cmd == "return":
                if len(parts) < 2:
                    print("Usage: return <transaction_id>")
                    continue
                lib.return_book(parts[1])
                print("Return successful.")

            # ---------------- LOANS ----------------
            elif cmd == "loans":
                if len(parts) < 2:
                    print("Usage: loans <active|overdue|user>")
                    continue
                sub = parts[1].lower()
                if sub == "active":
                    loans = lib.loans_active()
                    if not loans:
                        print("No active loans.")
                    else:
                        for tx in loans:
                            print_tx(tx)
                elif sub == "overdue":
                    loans = lib.loans_overdue()
                    if not loans:
                        print("No overdue loans.")
                    else:
                        for tx in loans:
                            print_tx(tx)
                elif sub == "user":
                    if len(parts) < 3:
                        print("Usage: loans user <user_id>")
                        continue
                    loans = lib.loans_user(parts[2])
                    if not loans:
                        print("No loans for user.")
                    else:
                        for tx in loans:
                            print_tx(tx)

                        # ---------------- REPORTS ----------------
            elif cmd == "report":
                if len(parts) < 2:
                    print("Usage: report <summary|user>")
                    continue
                sub = parts[1].lower()
                if sub == "summary":
                    summary = lib.report_summary()
                    for k, v in summary.items():
                        print(f"{k}: {v}")
                elif sub == "user":
                    if len(parts) < 3:
                        print("Usage: report user <user_id>")
                        continue
                    report = lib.report_user(parts[2])
                    if not report:
                        print("No transactions for user.")
                    else:
                        for r in report:
                            overdue_flag = " (OVERDUE)" if r.is_overdue(today_str()) else ""
                            print_tx(r)
                            if overdue_flag:
                                print(f"   -> {overdue_flag}")
                else:
                    print("Unknown report subcommand.")

            # ---------------- SAVE / EXIT ----------------
            elif cmd == "save":
                lib.save_all()
                print("All data saved to CSV successfully.")

            elif cmd == "exit":
                print("Goodbye.")
                break

            else:
                print("Unknown command. Type 'help' for available commands.")

        except (InvalidBookError, InvalidUserError, BookNotAvailableError,
                UserNotAllowedError, TransactionError, ValidationError) as e:
            print(f"Error: {e}")
        except Exception as e:
            # General catch to ensure the CLI never crashes
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()



"""
SAMPLE OUTPUT

T1001 | Arjun Selvan | Email: arjun.selvan@gmail.com
 | Status: active | Max Loans: 5

T1002 | Priya Natarajan | Email: priya.natarajan@yahoo.com
 | Status: active | Max Loans: 4

T1003 | Karthik Ramesh | Email: karthik.ramesh@outlook.com
 | Status: active | Max Loans: 5

T1004 | Divya Lakshmi | Email: divya.lakshmi@gmail.com
 | Status: active | Max Loans: 3

T1005 | Sathish Kumar | Email: sathish.kumar@hotmail.com
 | Status: active | Max Loans: 4

"""