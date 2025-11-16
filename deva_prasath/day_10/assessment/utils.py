# # utils.py
# import os
# from datetime import datetime, timedelta
# from typing import List, Any





# def check_password() -> bool:
#     """
#     Simple password check function.
#     Asks for the password and compares it with the stored password.
#     Returns True if correct, otherwise False.
#     """
#     correct_password = "admin123"  # Predefined password
#     entered_password = input("Please enter the password: ").strip()
    
#     if entered_password == correct_password:
#         return True
#     else:
#         print("Incorrect password! Access denied.")
#         return False



# def get_today_str() -> str:
#     """
#     Get current date in DD-MM-YYYY format.
#     Uses system time (November 15, 2025 12:52 PM IST).
#     """
#     return datetime.now().strftime("%d-%m-%Y")


# def add_days(date_str: str, days: int) -> str:
#     """
#     Add specified number of days to a date string.
#     Input/Output format: DD-MM-YYYY
#     """
#     try:
#         date_obj = datetime.strptime(date_str, "%d-%m-%Y")
#         new_date = date_obj + timedelta(days=days)
#         return new_date.strftime("%d-%m-%Y")
#     except ValueError as e:
#         raise ValueError(f"Invalid date format: {date_str}") from e


# def generate_id(prefix: str, existing_ids: set) -> str:
#     """
#     Generate unique ID with prefix (e.g., T1, B1001).
#     Avoids collisions with existing IDs.
#     """
#     if not prefix:
#         raise ValueError("Prefix cannot be empty")
    
#     i = 1
#     while True:
#         new_id = f"{prefix}{i}"
#         if new_id not in existing_ids:
#             return new_id
#         i += 1


# def safe_input(prompt: str, type_cast=str, allow_empty: bool = False) -> Any:
#     """
#     Robust input function with validation and type casting.
#     Repeats prompt on invalid input.
#     """
#     while True:
#         try:
#             value = input(prompt).strip()
#             if not value and not allow_empty:
#                 print("This field cannot be empty. Please try again.")
#                 continue
#             if type_cast == int:
#                 return int(value)
#             elif type_cast == float:
#                 return float(value)
#             elif type_cast == bool:
#                 return value.lower() in ("true", "1", "yes", "y")
#             else:
#                 return value
#         except ValueError:
#             print(f"Invalid input. Please enter a valid {type_cast.__name__}.")
#         except KeyboardInterrupt:
#             print("\nOperation cancelled by user.")
#             raise
#         except EOFError:
#             print("\nInput stream ended.")
#             raise


# def validate_non_empty(value: str, field_name: str) -> str:
#     """Ensure string is not empty after stripping."""
#     if not value or not value.strip():
#         raise ValueError(f"{field_name} cannot be empty")
#     return value.strip()


# def format_list(items: List[str]) -> str:
#     """Convert list to comma-separated string."""
#     return ", ".join(items) if items else "None"


# def clear_screen():
#     """Clear terminal screen."""
#     os.system('cls' if os.name == 'nt' else 'clear')


# def confirm_action(message: str) -> bool:
#     """Ask for confirmation (y/n)."""
#     while True:
#         response = input(f"{message} [y/N]: ").strip().lower()
#         if response in ("y", "yes"):
#             return True
#         elif response in ("n", "no", ""):
#             return False
#         else:
#             print("Please enter 'y' or 'n'.")


# def parse_date(date_str: str) -> datetime:
#     """Parse DD-MM-YYYY to datetime object."""
#     try:
#         return datetime.strptime(date_str, "%d-%m-%Y")
#     except ValueError:
#         raise ValueError("Date must be in DD-MM-YYYY format")

# # utils.py  (only the part that is changed – keep the rest of the file unchanged)

# def print_friendly_help():
#     """User-friendly help that a non-technical person can understand."""
#     help_text = """
# Welcome to the Library Management System!

# You type a short command and press Enter.  Below are the most common things you can do.
# (You can always type **help** to see this screen again.)

# --------------------------------------------------------------------
# BOOKS
# --------------------------------------------------------------------
# add book                – Add a new book (you will be asked for title, author, etc.)
# update book <id>         – Change details of a book (ID is shown when you list books)
# remove book <id>         – Delete a book (you will be asked to confirm)
# show book <id>           – See full details of one book
# list books               – Show every book in the library
# search books <word>      – Find books that contain the word in title, author or tag

# --------------------------------------------------------------------
# USERS (Members)
# --------------------------------------------------------------------
# add user                – Register a new library member
# update user <id>        – Change a member's name, email or loan limit
# show user <id>          – See a member's details and how many books they have out
# list users              – Show every member
# activate user <id>      – Let the member borrow books again
# deactivate user <id>    – Temporarily stop a member from borrowing
# ban user <id>           – Permanently block a member from borrowing

# --------------------------------------------------------------------
# BORROW / RETURN
# --------------------------------------------------------------------
# borrow <member_id> <book_id>   – Lend a book to a member
# return <transaction_id>        – Return a borrowed book (transaction ID is shown after borrow)

# --------------------------------------------------------------------
# LOANS & REPORTS
# --------------------------------------------------------------------
# active loans            – List every book that is currently borrowed
# overdue loans           – List books that are late
# loans for <member_id>   – Show the full borrowing history of a member

# summary                 – Quick overview: total books, members, active loans, overdue
# report for <member_id>  – Detailed history for one member

# --------------------------------------------------------------------
# SYSTEM
# --------------------------------------------------------------------
# save                    – Write all data to the CSV files (also done automatically on exit)
# exit                    – Quit the program

# --------------------------------------------------------------------
# Tip: The **ID** of a book or member is the short code that appears when you list them.
#      Example:  B001  or  U005
# """
#     print(help_text)




# utils.py
import os
from datetime import datetime, timedelta
from typing import List, Any


def get_today_str() -> str:
    """Get current date in DD-MM-YYYY format."""
    return datetime.now().strftime("%d-%m-%Y")


def add_days(date_str: str, days: int) -> str:
    """Add specified number of days to a date string."""
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime("%d-%m-%Y")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e


def generate_id(prefix: str, existing_ids: set) -> str:
    """Generate unique ID with prefix (e.g., T1, B1001)."""
    if not prefix:
        raise ValueError("Prefix cannot be empty")
    i = 1
    while True:
        new_id = f"{prefix}{i}"
        if new_id not in existing_ids:
            return new_id
        i += 1


def safe_input(prompt: str, type_cast=str, allow_empty: bool = False) -> Any:
    """Robust input function with validation and type casting."""
    while True:
        try:
            value = input(prompt).strip()
            if not value and not allow_empty:
                print("This field cannot be empty. Please try again.")
                continue
            if type_cast == int:
                return int(value)
            elif type_cast == float:
                return float(value)
            elif type_cast == bool:
                return value.lower() in ("true", "1", "yes", "y")
            else:
                return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_cast.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise
        except EOFError:
            print("\nInput stream ended.")
            raise


def validate_non_empty(value: str, field_name: str) -> str:
    """Ensure string is not empty after stripping."""
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
    return value.strip()


def format_list(items: List[str]) -> str:
    """Convert list to comma‑separated string."""
    return ", ".join(items) if items else "None"


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def confirm_action(message: str) -> bool:
    """Ask for confirmation (y/n)."""
    while True:
        response = input(f"{message} [y/N]: ").strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no", ""):
            return False
        else:
            print("Please enter 'y' or 'n'.")


def parse_date(date_str: str) -> datetime:
    """Parse DD-MM-YYYY to datetime object."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Date must be in DD-MM-YYYY format")


def print_friendly_help():
    """User‑friendly help that a non‑technical person can understand."""
    help_text = """
Welcome to the Library Management System!
You type a short command and press Enter. Below are the most common things you can do.
(You can always type **help** to see this screen again.)
--------------------------------------------------------------------
BOOKS
--------------------------------------------------------------------
add book – Add a new book (you will be asked for title, author, etc.)
update book <id> – Change details of a book (ID is shown when you list books)
remove book <id> – Delete a book (you will be asked to confirm)
show book <id> – See full details of one book
list books – Show every book in the library
search books <word> – Find books that contain the word in title, author or tag
--------------------------------------------------------------------
USERS (Members)
--------------------------------------------------------------------
add user – Register a new library member
update user <id> – Change a member's name, email or loan limit
show user <id> – See a member's details and how many books they have out
list users – Show every member
activate user <id> – Let the member borrow books again
deactivate user <id> – Temporarily stop a member from borrowing
ban user <id> – Permanently block a member from borrowing
--------------------------------------------------------------------
BORROW / RETURN
--------------------------------------------------------------------
borrow <member_id> <book_id> – Lend a book to a member
return <transaction_id> – Return a borrowed book (transaction ID is shown after borrow)
--------------------------------------------------------------------
LOANS & REPORTS
--------------------------------------------------------------------
active loans – List every book that is currently borrowed
overdue loans – List books that are late
loans for <member_id> – Show the full borrowing history of a member
summary – Quick overview: total books, members, active loans, overdue
report for <member_id> – Detailed history for one member
--------------------------------------------------------------------
SYSTEM
--------------------------------------------------------------------
save – Write all data to the CSV files (also done automatically on exit)
logout – End the admin session (you will need the password again)
exit – Quit the program
--------------------------------------------------------------------
Tip: The **ID** of a book or member is the short code that appears when you list them.
     Example: B001 or U005
"""
    print(help_text)


# --------------------------------------------------------------
# NEW: Simple password check (hard‑coded, no encryption)
# --------------------------------------------------------------
def check_password(prompt: str = "Enter admin password: ") -> bool:
    """
    Simple password verification.
    Change the PASSWORD constant below to whatever you want.
    """
    PASSWORD = "admin123"          # ← CHANGE THIS TO YOUR DESIRED PASSWORD
    pwd = input(prompt).strip()
    return pwd == PASSWORD