from datetime import datetime, timedelta

DATE_FMT = "%d-%m-%Y"

def today_str():
    """Return today's date as DD-MM-YYYY."""
    return datetime.now().strftime(DATE_FMT)

def due_date_str(days):
    """Return the due date as today + days."""
    return (datetime.now() + timedelta(days=days)).strftime(DATE_FMT)

def parse_comma_list(value):
    """Convert comma-separated input into a clean list."""
    if not value.strip():
        return []
    return [v.strip() for v in value.split(",")]

def input_nonempty(prompt):
    """Input helper that rejects empty values."""
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input cannot be empty.")
    return value
