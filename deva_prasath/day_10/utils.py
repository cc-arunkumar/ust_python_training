# utils.py
import os
from datetime import datetime, timedelta
from typing import List, Any


def get_today_str() -> str:
    """
    Get current date in DD-MM-YYYY format.
    Uses system time (November 15, 2025 12:52 PM IST).
    """
    return datetime.now().strftime("%d-%m-%Y")


def add_days(date_str: str, days: int) -> str:
    """
    Add specified number of days to a date string.
    Input/Output format: DD-MM-YYYY
    """
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime("%d-%m-%Y")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e


def generate_id(prefix: str, existing_ids: set) -> str:
    """
    Generate unique ID with prefix (e.g., T1, B1001).
    Avoids collisions with existing IDs.
    """
    if not prefix:
        raise ValueError("Prefix cannot be empty")
    
    i = 1
    while True:
        new_id = f"{prefix}{i}"
        if new_id not in existing_ids:
            return new_id
        i += 1


def safe_input(prompt: str, type_cast=str, allow_empty: bool = False) -> Any:
    """
    Robust input function with validation and type casting.
    Repeats prompt on invalid input.
    """
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
    """Convert list to comma-separated string."""
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


# Optional: For future date parsing
def parse_date(date_str: str) -> datetime:
    """Parse DD-MM-YYYY to datetime object."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Date must be in DD-MM-YYYY format")