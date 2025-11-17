import sys
from library import Library
from utils import (
    safe_input, get_today_str, print_friendly_help,
    check_password
)
from models import (
    ValidationError, InvalidBookError, InvalidUserError,
    BookNotAvailableError, UserNotAllowedError, TransactionError
)

# --------------------------------------------------------------
# Global authentication state
# --------------------------------------------------------------
is_authenticated = False

# --------------------------------------------------------------
# ID Normalisation Helpers
# --------------------------------------------------------------
def resolve_book_id(raw: str) -> str:
    if not raw:
        return raw
    raw = raw.strip()
    if raw and raw[0].upper() == "B" and raw[1:].isdigit():
        return f"B{int(raw[1:]):04d}"
    if raw.isdigit():
        return f"B{int(raw):04d}"
    return raw.upper()


def resolve_user_id(raw: str) -> str:
    if not raw:
        return raw
    raw = raw.strip()
    if raw and raw[0].upper() == "U" and raw[1:].isdigit():
        return f"U{int(raw[1:])}"
    return raw.upper()


# --------------------------------------------------------------
# Command Parsing Helpers
# --------------------------------------------------------------
def normalize_command(command: str):
    raw_parts = command.strip().split()
    if not raw_parts:
        return [], []
    parts = [raw_parts[0].lower()]
    if len(raw_parts) > 1:
        parts.append(raw_parts[1].lower())
        for tok in raw_parts[2:]:
            parts.append(tok)
    return parts, raw_parts


def friendly_normalize(parts: list):
    if not parts:
        return parts
    p = parts.copy()
    # BOOK
    if p[0] == "add" and len(p) > 1 and p[1] == "book":
        return ["book", "add"]
    if p[0] == "list" and len(p) > 1 and p[1] in ("book", "books"):
        return ["book", "list"]
    if p[0] == "search" and len(p) > 1 and p[1] in ("book", "books"):
        return ["book", "search"] + p[2:]
    if p[0] == "update" and len(p) >= 3 and p[1] == "book":
        return ["book", "update", resolve_book_id(p[2])]
    if p[0] == "remove" and len(p) >= 3 and p[1] == "book":
        return ["book", "remove", resolve_book_id(p[2])]
    if p[0] == "show" and len(p) >= 3 and p[1] == "book":
        return ["book", "get", resolve_book_id(p[2])]
    # USER
    if p[0] == "add" and len(p) > 1 and p[1] == "user":
        return ["user", "add"]
    if p[0] == "update" and len(p) >= 3 and p[1] == "user":
        return ["user", "update", resolve_user_id(p[2])]
    if p[0] == "show" and len(p) >= 3 and p[1] == "user":
        return ["user", "get", resolve_user_id(p[2])]
    if p[0] == "list" and len(p) > 1 and p[1] in ("user", "users"):
        return ["user", "list"]
    if p[0] in ("activate", "deactivate", "ban") and len(p) >= 3 and p[1] == "user":
        return ["user", p[0], resolve_user_id(p[2])]
    # BORROW / RETURN
    if p[0] == "borrow" and len(p) >= 3:
        return ["borrow", resolve_user_id(p[1]), resolve_book_id(p[2])]
    if p[0] == "return" and len(p) >= 2:
        return ["return", p[1]]
    # LOANS
    if p[0] == "active" and len(p) > 1 and p[1] == "loans":
        return ["loans", "active"]
    if p[0] == "overdue" and len(p) > 1 and p[1] == "loans":
        return ["loans", "overdue"]
    if p[0] == "loans" and len(p) >= 3 and p[1] in ("for", "user"):
        idx = 2 if p[1] == "for" else 2
        return ["loans", "user", resolve_user_id(p[idx])]
    # REPORTS
    if p[0] == "summary":
        return ["report", "summary"]
    if p[0] == "report" and len(p) >= 3 and p[1] == "for":
        return ["report", "user", resolve_user_id(p[2])]
    # LOGOUT
    if p[0] == "logout":
        return ["logout"]
    return p


# --------------------------------------------------------------
# Small UI helpers (Style C box)
# --------------------------------------------------------------
def print_boxed_title(title: str):
    width = max(40, len(title) + 6)
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + title.center(width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝")


def prompt_continue():
    input("\nPress Enter to continue...")


# --------------------------------------------------------------
# Authentication helper
# --------------------------------------------------------------
def authenticate(lib: Library) -> bool:
    """Ask for password once per session."""
    global is_authenticated
    if is_authenticated:
        return True
    if check_password():
        print("[Success] Access granted.")
        is_authenticated = True
        return True
    else:
        print("[Error] Incorrect password.")
        return False


# --------------------------------------------------------------
# Commands that need authentication
# --------------------------------------------------------------
PROTECTED_COMMANDS = {
    "book", "user", "borrow", "return",
    "loans", "report", "save"
}


# --------------------------------------------------------------
# Process a parsed command
# --------------------------------------------------------------
def process_command(parts: list, raw_parts: list, lib: Library):
    global is_authenticated

    if not parts:
        return False

    action = parts[0]

    # PUBLIC: help (no password)
    if action == "help":
        print_friendly_help()
        return True

    # PUBLIC: logout (only works when already logged in)
    if action == "logout":
        if is_authenticated:
            is_authenticated = False
            print("Logged out. You will need the password again for admin actions.")
        else:
            print("You are not logged in.")
        return True

    # PROTECTED actions
    if action in PROTECTED_COMMANDS and not is_authenticated:
        if not authenticate(lib):
            return True          # password wrong → stop processing
        # now authenticated for the rest of the session

    # ------------------------------------------------------------------
    #  ALL ORIGINAL COMMAND LOGIC (unchanged, just indented)
    # ------------------------------------------------------------------
    if action == "save":
        lib.save_all()
        print("All data saved to CSV files.")
        return True

    # BOOKS
    if action == "book":
        if len(parts) < 2:
            print("Usage: book add | update <id> | remove <id> | get <id> | list")
            return True
        sub = parts[1]

        # add
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
            print(f"[Success] Book '{title}' added (ID: {book_id})")
            return True

        # update
        if sub == "update":
            bid = parts[2] if len(parts) >= 3 else safe_input("Enter Book ID to update: ")
            bid = resolve_book_id(bid)
            book = lib.get_book(bid)
            print(f"=== Updating Book: {book.title} ===")
            print("Leave blank to keep current value.")
            new_title = input(f"Title [{book.title}]: ").strip()
            new_authors = input(f"Authors [{', '.join(book.authors)}]: ").strip()
            new_isbn = input(f"ISBN [{book.isbn or 'None'}]: ").strip()
            new_tags = input(f"Tags [{', '.join(book.tags)}]: ").strip()
            new_copies = input(f"Total Copies [{book.total_copies}]: ").strip()
            updates = {}
            if new_title:
                updates["title"] = new_title
            if new_authors:
                updates["authors"] = [a.strip() for a in new_authors.split(",") if a.strip()]
            if new_isbn:
                updates["isbn"] = new_isbn
            if new_tags:
                updates["tags"] = [t.strip() for t in new_tags.split(",") if t.strip()]
            if new_copies:
                updates["total_copies"] = int(new_copies)
            lib.update_book(bid, **updates)
            print("[Success] Book updated.")
            return True

        # remove
        if sub == "remove":
            bid = parts[2] if len(parts) >= 3 else safe_input("Enter Book ID to remove: ")
            bid = resolve_book_id(bid)
            book = lib.get_book(bid)
            confirm = input(f"Are you sure you want to remove '{book.title}' (ID: {bid})? [y/N]: ").strip().lower()
            if confirm == "y":
                lib.remove_book(bid)
                print("[Success] Book removed.")
            else:
                print("Removal cancelled.")
            return True

        # get / show
        if sub == "get":
            bid = parts[2] if len(parts) >= 3 else safe_input("Enter Book ID to view: ")
            bid = resolve_book_id(bid)
            book = lib.get_book(bid)
            print("\n--- Book Details ---")
            print(f"ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Authors: {', '.join(book.authors)}")
            print(f"ISBN: {book.isbn or 'N/A'}")
            print(f"Tags: {', '.join(book.tags)}")
            print(f"Available: {book.available_copies}/{book.total_copies}")
            print(f"Status: {'Available' if book.is_available() else 'Not Available'}")
            return True

        # list
        if sub == "list":
            books = lib.list_books()
            print(f"\n=== All Books ({len(books)}) ===")
            for b in books:
                status = "Available" if b.is_available() else "Not Available"
                print(f"{b.book_id}: {b.title} [{b.available_copies}/{b.total_copies}] [{status}]")
            return True

        # search
        if sub == "search":
            if len(parts) < 4:
                print("Usage: book search [title|author|tag] <value>")
                return True
            field = parts[2]
            value = " ".join(parts[3:])
            results = []
            if field == "title":
                results = lib.search_books(title=value)
            elif field == "author":
                results = lib.search_books(author=value)
            elif field == "tag":
                results = lib.search_books(tag=value)
            else:
                print("Search by: title, author or tag")
                return True
            if not results:
                print("No books found.")
            else:
                print(f"\n=== Search Results ({len(results)}) ===")
                for b in results:
                    print(f"{b.book_id}: {b.title} [{b.available_copies}/{b.total_copies}]")
            return True

    # USERS
    if action == "user":
        if len(parts) < 2:
            print("Usage: user add | update <id> | get <id> | list | activate <id> | deactivate <id> | ban <id>")
            return True
        sub = parts[1]

        # add
        if sub == "add":
            print("=== Add New Member ===")
            user_id = safe_input("Member ID: ")
            name = safe_input("Name: ")
            email = safe_input("Email (optional): ", allow_empty=True)
            lib.add_user(user_id, name, email or None)
            print(f"[Success] Member '{name}' added (ID: {user_id})")
            return True

        # update
        if sub == "update":
            uid = parts[2] if len(parts) >= 3 else safe_input("Enter Member ID to update: ")
            uid = resolve_user_id(uid)
            user = lib.get_user(uid)
            print(f"=== Updating Member: {user.name} ===")
            new_name = input(f"Name [{user.name}]: ").strip()
            new_email = input(f"Email [{user.email or 'None'}]: ").strip()
            updates = {}
            if new_name:
                updates["name"] = new_name
            if new_email:
                updates["email"] = new_email
            lib.update_user(uid, **updates)
            print("[Success] Member updated.")
            return True

        # get
        if sub == "get":
            uid = parts[2] if len(parts) >= 3 else safe_input("Enter Member ID to view: ")
            uid = resolve_user_id(uid)
            user = lib.get_user(uid)
            print("\n--- Member Details ---")
            print(f"ID: {user.user_id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email or 'N/A'}")
            print(f"Status: {user.status.capitalize()}")
            active = sum(1 for t in lib.transactions if t.user_id == user.user_id and t.status == "borrowed")
            print(f"Active Loans: {active}")
            return True

        # list
        if sub == "list":
            users = lib.list_users()
            print(f"\n=== All Members ({len(users)}) ===")
            for u in users:
                print(f"{u.user_id}: {u.name} [{u.status}]")
            return True

        # activate / deactivate / ban
        if sub in ("activate", "deactivate", "ban"):
            uid = parts[2] if len(parts) >= 3 else safe_input(f"Enter Member ID to {sub}: ")
            uid = resolve_user_id(uid)
            user = lib.get_user(uid)
            if sub == "activate":
                user.activate()
            elif sub == "deactivate":
                user.deactivate()
            else:
                user.ban()
            print(f"[Success] Member {sub}d.")
            return True

    # BORROW
    if action == "borrow":
        uid = parts[1] if len(parts) >= 3 else safe_input("Enter Member ID: ")
        uid = resolve_user_id(uid)
        bid = parts[2] if len(parts) >= 3 else safe_input("Enter Book ID: ")
        bid = resolve_book_id(bid)
        tx = lib.borrow_book(uid, bid)
        print(f"[Success] Borrow successful! Transaction ID: {tx.tx_id} Due: {tx.due_date}")
        return True

    # RETURN
    if action == "return":
        txid = raw_parts[1].strip() if len(raw_parts) >= 2 else safe_input("Enter Transaction ID to return: ")
        lib.return_book(txid)
        print("[Success] Book returned successfully.")
        return True

    # LOANS
    if action == "loans":
        if len(parts) < 2:
            print("Usage: loans active | overdue | user <id>")
            return True
        sub = parts[1]
        if sub == "active":
            active = lib.active_loans()
            if not active:
                print("No active loans.")
            else:
                print(f"\n=== Active Loans ({len(active)}) ===")
                for t in active:
                    print(f"{t.tx_id}: {t.book_id} → {t.user_id} | Due: {t.due_date}")
            return True
        if sub == "overdue":
            overdue = lib.overdue_loans()
            if not overdue:
                print("No overdue loans.")
            else:
                print(f"\n=== OVERDUE LOANS ({len(overdue)}) ===")
                for t in overdue:
                    print(f"{t.tx_id}: {t.book_id} → {t.user_id} | Due: {t.due_date}")
            return True
        if sub == "user" and len(parts) >= 3:
            uid = resolve_user_id(parts[2])
            history = lib.user_loan_history(uid)
            user = lib.get_user(uid)
            print(f"\n=== Loan History: {user.name} ({uid}) ===")
            today = get_today_str()
            for t in history:
                status = t.status.upper()
                if t.status == "borrowed" and t.is_overdue(today):
                    status = "OVERDUE"
                print(f"{t.tx_id} | {t.book_id} | {t.borrow_date.strftime('%d-%m-%Y')} → {t.due_date} | {status}")
            return True

    # REPORTS
    if action == "report":
        if len(parts) < 2:
            print("Usage: report summary | user <id>")
            return True
        sub = parts[1]
        if sub == "summary":
            r = lib.summary_report()
            print("\n=== Library Summary ===")
            print(f"Total Books : {r['total_books']}")
            print(f"Total Members: {r['total_users']}")
            print(f"Active Loans : {r['active_loans']}")
            print(f"Overdue Loans: {r['overdue_loans']}")
            return True
        if sub == "user" and len(parts) >= 3:
            uid = resolve_user_id(parts[2])
            rep = lib.user_history_report(uid)
            user = rep["user"]
            print(f"\n=== Transaction Report: {user.name} ({uid}) ===")
            for t in rep["transactions"]:
                status = t.status.upper()
                if t.status == "borrowed" and t.is_overdue(get_today_str()):
                    status = "OVERDUE"
                print(f"{t.tx_id} | {t.book_id} | {t.borrow_date.strftime('%d-%m-%Y')} → {t.due_date} | {status}")
            if rep["overdue"]:
                print(f"\nOverdue: {len(rep['overdue'])} item(s)")
            return True

    return False


# --------------------------------------------------------------
# Menu implementations (unchanged except auth status display)
# --------------------------------------------------------------
def books_menu(lib: Library):
    while True:
        print_boxed_title("BOOKS MENU")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. View Book")
        print("5. List All Books")
        print("6. Search Books")
        print("7. Back")
        choice = input("Choose option or type command: ").strip()
        if not choice:
            continue
        if choice.isdigit():
            if choice == "1":
                process_command(["book","add"], ["book","add"], lib)
            elif choice == "2":
                bid = safe_input("Enter Book ID to update: ")
                parts, raw = normalize_command(f"book update {bid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "3":
                bid = safe_input("Enter Book ID to remove: ")
                parts, raw = normalize_command(f"book remove {bid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "4":
                bid = safe_input("Enter Book ID to view: ")
                parts, raw = normalize_command(f"book get {bid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "5":
                process_command(["book","list"], ["book","list"], lib)
            elif choice == "6":
                field = input("Search by (title/author/tag): ").strip().lower()
                if field not in ("title","author","tag"):
                    print("Invalid field.")
                else:
                    val = input("Enter search value: ").strip()
                    parts, raw = normalize_command(f"book search {field} {val}")
                    parts = friendly_normalize(parts)
                    process_command(parts, raw, lib)
            elif choice == "7":
                return
            else:
                print("Invalid selection.")
        else:
            parts, raw = normalize_command(choice)
            parts = friendly_normalize(parts)
            handled = process_command(parts, raw, lib)
            if not handled:
                print("Unknown book command.")
        prompt_continue()


def users_menu(lib: Library):
    while True:
        print_boxed_title("USERS MENU")
        print("1. Add Member")
        print("2. Update Member")
        print("3. View Member")
        print("4. List Members")
        print("5. Activate / Deactivate / Ban")
        print("6. Back")
        choice = input("Choose option or type command: ").strip()
        if not choice:
            continue
        if choice.isdigit():
            if choice == "1":
                process_command(["user","add"], ["user","add"], lib)
            elif choice == "2":
                uid = safe_input("Enter Member ID to update: ")
                parts, raw = normalize_command(f"user update {uid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "3":
                uid = safe_input("Enter Member ID to view: ")
                parts, raw = normalize_command(f"user get {uid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "4":
                process_command(["user","list"], ["user","list"], lib)
            elif choice == "5":
                uid = safe_input("Enter Member ID: ")
                uid = resolve_user_id(uid)
                act = input("Type (activate/deactivate/ban): ").strip().lower()
                if act not in ("activate","deactivate","ban"):
                    print("Invalid action.")
                else:
                    parts, raw = normalize_command(f"user {act} {uid}")
                    parts = friendly_normalize(parts)
                    process_command(parts, raw, lib)
            elif choice == "6":
                return
            else:
                print("Invalid selection.")
        else:
            parts, raw = normalize_command(choice)
            parts = friendly_normalize(parts)
            handled = process_command(parts, raw, lib)
            if not handled:
                print("Unknown user command.")
        prompt_continue()


def borrow_flow(lib: Library):
    print_boxed_title("BORROW BOOK")
    uid = safe_input("Enter Member ID: ")
    uid = resolve_user_id(uid)
    bid = safe_input("Enter Book ID: ")
    bid = resolve_book_id(bid)
    try:
        tx = lib.borrow_book(uid, bid)
        print(f"[Success] Borrow successful! Transaction ID: {tx.tx_id} Due: {tx.due_date}")
    except Exception as e:
        print(f"Error: {e}")
    prompt_continue()


def return_flow(lib: Library):
    print_boxed_title("RETURN BOOK")
    txid = safe_input("Enter Transaction ID to return: ").strip()
    try:
        lib.return_book(txid)
        print("[Success] Book returned successfully.")
    except Exception as e:
        print(f"Error: {e}")
    prompt_continue()


def loans_menu(lib: Library):
    while True:
        print_boxed_title("LOANS")
        print("1. Active Loans")
        print("2. Overdue Loans")
        print("3. User Loan History")
        print("4. Back")
        choice = input("Choose option or type command: ").strip()
        if not choice:
            continue
        if choice.isdigit():
            if choice == "1":
                process_command(["loans","active"], ["loans","active"], lib)
            elif choice == "2":
                process_command(["loans","overdue"], ["loans","overdue"], lib)
            elif choice == "3":
                uid = safe_input("Enter Member ID: ")
                parts, raw = normalize_command(f"loans user {uid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "4":
                return
            else:
                print("Invalid selection.")
        else:
            parts, raw = normalize_command(choice)
            parts = friendly_normalize(parts)
            handled = process_command(parts, raw, lib)
            if not handled:
                print("Unknown loans command.")
        prompt_continue()


def reports_menu(lib: Library):
    while True:
        print_boxed_title("REPORTS")
        print("1. Summary")
        print("2. User Report")
        print("3. Back")
        choice = input("Choose option or type command: ").strip()
        if not choice:
            continue
        if choice.isdigit():
            if choice == "1":
                process_command(["report","summary"], ["report","summary"], lib)
            elif choice == "2":
                uid = safe_input("Enter Member ID: ")
                parts, raw = normalize_command(f"report for {uid}")
                parts = friendly_normalize(parts)
                process_command(parts, raw, lib)
            elif choice == "3":
                return
            else:
                print("Invalid selection.")
        else:
            parts, raw = normalize_command(choice)
            parts = friendly_normalize(parts)
            handled = process_command(parts, raw, lib)
            if not handled:
                print("Unknown reports command.")
        prompt_continue()


# --------------------------------------------------------------
# Main loop
# --------------------------------------------------------------
def main():
    lib = Library()
    print_boxed_title("LIBRARY MANAGEMENT SYSTEM")
    print("Type 'help' for commands. Admin access required for most operations.")
    print()

    while True:
        auth_status = "[Authenticated]" if is_authenticated else "[Guest Mode]"
        print_boxed_title(f"MAIN MENU {auth_status}")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Loans")
        print("6. Reports")
        print("7. Save")
        print("8. Logout" if is_authenticated else "8. (no logout)")
        print("9. Exit")
        choice = input("Enter option number or type a command (type 'help'): ").strip()
        if not choice:
            continue

        # numeric menu
        if choice.isdigit():
            if choice == "1":
                books_menu(lib)
            elif choice == "2":
                users_menu(lib)
            elif choice == "3":
                borrow_flow(lib)
            elif choice == "4":
                return_flow(lib)
            elif choice == "5":
                loans_menu(lib)
            elif choice == "6":
                reports_menu(lib)
            elif choice == "7":
                process_command(["save"], ["save"], lib)
            elif choice == "8":
                if is_authenticated:
                    process_command(["logout"], ["logout"], lib)
                else:
                    print("You are not logged in.")
            elif choice == "9":
                confirm = input("Save before exit? [Y/n]: ").strip().lower()
                if confirm != "n":
                    lib.save_all()
                    print("Data saved.")
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid selection.")
            continue

        # typed command
        try:
            parts, raw_parts = normalize_command(choice)
            parts = friendly_normalize(parts)
            handled = process_command(parts, raw_parts, lib)
            if not handled:
                print("Unknown command. Type 'help' for the full list.")
        except (
            InvalidBookError, InvalidUserError, BookNotAvailableError,
            UserNotAllowedError, TransactionError, ValidationError
        ) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()