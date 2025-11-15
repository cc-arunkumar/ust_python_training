from storage import CSVStorage
from library import Library
from models import Book, User, InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError
from utils import csv_authors_from_input, csv_tags_from_input

HELP_TEXT = """
Commands:
  book add
  book update <book_id>
  book remove <book_id>
  book get <book_id>
  book list
  book search title <substring>
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
  return <tx_id>

  loans active
  loans overdue
  loans user <user_id>

  report summary
  report user <user_id>

  save
  help
  exit
"""

def prompt(text):
    return input(text).strip()

def print_book(b: Book):
    print(f"{b.book_id} | {b.title} | Authors: {', '.join(b.authors)} | ISBN: {b.isbn} | Tags: {', '.join(b.tags)} | Total: {b.total_copies} | Available: {b.available_copies}")

def print_user(u: User):
    print(f"{u.user_id} | {u.name} | Email: {u.email or '-'} | Status: {u.status} | Max Loans: {u.max_loans}")

def print_tx(t):
    print(f"{t.tx_id} | Book: {t.book_id} | User: {t.user_id} | Borrow: {t.borrow_date} | Due: {t.due_date} | Return: {t.return_date or '-'} | Status: {t.status}")

def main():
    storage = CSVStorage()
    lib = Library(storage)

    print("lms> type 'help' for commands.")
    while True:
        try:
            cmd = input("lms> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not cmd:
            continue

        tokens = cmd.split()
        try:
            if tokens[0] == "help":
                print(HELP_TEXT)

            elif tokens[0] == "exit":
                print("Goodbye.")
                break

            elif tokens[0] == "save":
                lib.save_all()
                print("All data saved to CSV successfully.")

            # Book commands
            elif tokens[0] == "book" and len(tokens) >= 2:
                sub = tokens[1]

                if sub == "add":
                    book_id = prompt("Book ID: ")
                    title = prompt("Title: ")
                    authors_in = prompt("Authors (comma separated): ")
                    isbn = prompt("ISBN: ")
                    tags_in = prompt("Tags (comma separated): ")
                    total_copies = int(prompt("Total Copies: ") or "0")
                    available_copies_in = prompt("Available Copies (leave empty to default to Total): ")
                    available_copies = int(available_copies_in) if available_copies_in else total_copies

                    b = Book(
                        book_id=book_id,
                        title=title,
                        authors=csv_authors_from_input(authors_in),
                        isbn=isbn,
                        tags=csv_tags_from_input(tags_in),
                        total_copies=total_copies,
                        available_copies=available_copies
                    )
                    lib.add_book(b)
                    print("Book added successfully.")

                elif sub == "update" and len(tokens) == 3:
                    book_id = tokens[2]
                    print("Leave field empty to skip updating.")
                    new_title = prompt("Title: ")
                    new_authors = prompt("Authors (comma separated): ")
                    new_isbn = prompt("ISBN: ")
                    new_tags = prompt("Tags (comma separated): ")
                    new_total = prompt("Total Copies: ")
                    new_available = prompt("Available Copies: ")
                    kwargs = {}
                    if new_title: kwargs["title"] = new_title
                    if new_authors: kwargs["authors"] = new_authors
                    if new_isbn: kwargs["isbn"] = new_isbn
                    if new_tags: kwargs["tags"] = new_tags
                    if new_total: kwargs["total_copies"] = int(new_total)
                    if new_available: kwargs["available_copies"] = int(new_available)
                    lib.update_book(book_id, **kwargs)
                    print("Book updated.")

                elif sub == "remove" and len(tokens) == 3:
                    lib.remove_book(tokens[2])
                    print("Book removed.")

                elif sub == "get" and len(tokens) == 3:
                    b = lib.get_book(tokens[2])
                    if b: print_book(b)
                    else: print("Book not found.")

                elif sub == "list":
                    items = lib.list_books()
                    if not items: print("No books.")
                    else:
                        for b in items: print_book(b)

                elif sub == "search" and len(tokens) >= 4:
                    field = tokens[2]
                    query = " ".join(tokens[3:])
                    if field == "title":
                        res = lib.search_books_title(query)
                    elif field == "author":
                        res = lib.search_books_author(query)
                    elif field == "tag":
                        res = lib.search_books_tag(query)
                    else:
                        print("Unknown search field.")
                        continue
                    if not res:
                        print("No matching books.")
                    else:
                        for b in res:
                            print_book(b)

                else:
                    print("Invalid book command. Type 'help'.")

            # User commands
            elif tokens[0] == "user" and len(tokens) >= 2:
                sub = tokens[1]

                if sub == "add":
                    user_id = prompt("User ID: ")
                    name = prompt("Name: ")
                    email = prompt("Email: ")
                    max_loans_in = prompt("Max Loans (default 5): ")
                    max_loans = int(max_loans_in or "5")
                    u = User(user_id=user_id, name=name, email=email or None, max_loans=max_loans)
                    lib.add_user(u)
                    print("User added.")

                elif sub == "update" and len(tokens) == 3:
                    user_id = tokens[2]
                    print("Leave field empty to skip updating.")
                    name = prompt("Name: ")
                    email = prompt("Email: ")
                    status = prompt("Status (active/inactive/banned): ")
                    max_loans = prompt("Max Loans: ")
                    kwargs = {}
                    if name: kwargs["name"] = name
                    if email: kwargs["email"] = email
                    if status: kwargs["status"] = status
                    if max_loans: kwargs["max_loans"] = int(max_loans)
                    lib.update_user(user_id, **kwargs)
                    print("User updated.")

                elif sub == "get" and len(tokens) == 3:
                    u = lib.get_user(tokens[2])
                    if u: print_user(u)
                    else: print("User not found.")

                elif sub == "list":
                    items = lib.list_users()
                    if not items: print("No users.")
                    else:
                        for u in items: print_user(u)

                elif sub == "deactivate" and len(tokens) == 3:
                    lib.deactivate_user(tokens[2])
                    print("User deactivated.")

                elif sub == "activate" and len(tokens) == 3:
                    lib.activate_user(tokens[2])
                    print("User activated.")

                elif sub == "ban" and len(tokens) == 3:
                    lib.ban_user(tokens[2])
                    print("User banned.")

                else:
                    print("Invalid user command. Type 'help'.")

            # Borrow / Return
            elif tokens[0] == "borrow" and len(tokens) == 3:
                user_id, book_id = tokens[1], tokens[2]
                t = lib.borrow(user_id, book_id)
                print(f"Borrow successful. Transaction ID: {t.tx_id}. Due Date: {t.due_date}.")

            elif tokens[0] == "return" and len(tokens) == 2:
                tx_id = tokens[1]
                lib.return_book(tx_id)
                print("Return successful.")

            # Transactions queries
            elif tokens[0] == "loans" and len(tokens) >= 2:
                sub = tokens[1]
                if sub == "active":
                    res = lib.loans_active()
                    if not res: print("No active loans.")
                    else:
                        for t in res: print_tx(t)
                elif sub == "overdue":
                    res = lib.loans_overdue()
                    if not res: print("No overdue loans.")
                    else:
                        for t in res: print_tx(t)
                elif sub == "user" and len(tokens) == 3:
                    res = lib.loans_user(tokens[2])
                    if not res: print("No loans for user.")
                    else:
                        for t in res: print_tx(t)
                else:
                    print("Invalid loans command.")

            # Reports
            elif tokens[0] == "report" and len(tokens) >= 2:
                sub = tokens[1]
                if sub == "summary":
                    r = lib.report_summary()
                    print(f"Total books: {r['total_books']}")
                    print(f"Total users: {r['total_users']}")
                    print(f"Active loans: {r['active_loans']}")
                    print(f"Overdue loans: {r['overdue_loans']}")
                elif sub == "user" and len(tokens) == 3:
                    user_id = tokens[2]
                    txs = lib.report_user_history(user_id)
                    if not txs:
                        print("No history for user.")
                    else:
                        for t in txs:
                            print_tx(t)
                else:
                    print("Invalid report command.")

            else:
                print("Unknown command. Type 'help'.")

        except (InvalidBookError, InvalidUserError, BookNotAvailableError, UserNotAllowedError, TransactionError, ValidationError) as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Validation Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
