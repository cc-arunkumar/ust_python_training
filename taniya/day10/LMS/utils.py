from datetime import datetime, timedelta
import re

# Define the date format used throughout the system (Day-Month-Year)
DATE_FMT = "%d-%m-%Y"

# -------------------------------
# Date utilities
# -------------------------------

def today_str() -> str:
    """
    Return today's date as a string in DD-MM-YYYY format.
    Example: "24-11-2025"
    """
    return datetime.today().strftime(DATE_FMT)

def add_days_str(date_str: str, days: int) -> str:
    """
    Add a number of days to a given date string.
    Args:
        date_str: date in DD-MM-YYYY format
        days: number of days to add
    Returns:
        New date string in DD-MM-YYYY format
    """
    base = datetime.strptime(date_str, DATE_FMT)   # Convert string to datetime object
    return (base + timedelta(days=days)).strftime(DATE_FMT)  # Add days and return as string

# -------------------------------
# Email validation
# -------------------------------

def validate_email(email: str) -> bool:
    """
    Validate email format using regex.
    Args:
        email: email string to validate
    Returns:
        True if valid or empty, False if invalid
    """
    if not email:   # Allow empty email (optional field)
        return True
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"   # Basic regex for email validation
    return re.match(pattern, email) is not None

# -------------------------------
# CSV input parsing helpers
# -------------------------------

def csv_authors_from_input(text: str) -> list:
    """
    Convert a comma-separated string of authors into a list.
    Args:
        text: "John Doe, Jane Smith"
    Returns:
        ["John Doe", "Jane Smith"]
    """
    if not text:
        return []
    return [a.strip() for a in text.split(",") if a.strip()]

def csv_tags_from_input(text: str) -> list:
    """
    Convert a comma-separated string of tags into a list.
    Args:
        text: "Programming, Beginner"
    Returns:
        ["Programming", "Beginner"]
    """
    if not text:
        return []
    return [t.strip() for t in text.split(",") if t.strip()]