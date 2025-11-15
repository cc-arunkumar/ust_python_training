# utils.py
from datetime import datetime, timedelta

DATE_FMT = "%d-%m-%Y"

# ---------------- General Helpers ----------------
def parse_csv_list(raw, sep=","):
    """Convert a comma-separated string into a list of trimmed values."""
    if not raw:
        return []
    return [x.strip() for x in raw.split(sep) if x.strip()]

def today_str():
    """Return today's date as DD-MM-YYYY string."""
    return datetime.today().strftime(DATE_FMT)

def due_date_str(days=14):
    """Return due date string (today + N days)."""
    return (datetime.today() + timedelta(days=int(days))).strftime(DATE_FMT)

def generate_id(prefix, existing_ids):
    """
    Generate a new ID with given prefix.
    Example: prefix='B', existing_ids=['B1','B2'] -> 'B3'
    """
    max_num = 0
    for _id in existing_ids:
        if _id and _id.startswith(prefix):
            try:
                n = int(_id[len(prefix):])
                if n > max_num:
                    max_num = n
            except ValueError:
                continue
    return f"{prefix}{max_num + 1}"

def safe_int(prompt):
    """Prompt user until they enter a valid integer."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid number. Please enter an integer.")

# ---------------- Pretty Printers ----------------
def print_book(book):
    """Nicely print a Book object."""
    print(f"{book.book_id} | {book.title} | ISBN: {book.isbn or '-'} | "
          f"Authors: {', '.join(book.authors) or '-'} | Tags: {', '.join(book.tags) or '-'} | "
          f"Total: {book.total_copies} | Available: {book.available_copies}")

def print_user(user):
    """Nicely print a User object."""
    print(f"{user.user_id} | {user.name} | Email: {user.email or '-'} | "
          f"Status: {user.status} | Max Loans: {user.max_loans}")

def print_tx(tx):
    """Nicely print a Transaction object."""
    print(f"{tx.tx_id} | Book: {tx.book_id} | User: {tx.user_id} | "
          f"Borrow: {tx.borrow_date} | Due: {tx.due_date} | "
          f"Return: {tx.return_date or '-'} | Status: {tx.status}")
