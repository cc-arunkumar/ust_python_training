from datetime import datetime, timedelta
import re

DATE_FMT = "%d-%m-%Y"

def today_str() -> str:
    return datetime.today().strftime(DATE_FMT)

def add_days_str(date_str: str, days: int) -> str:
    base = datetime.strptime(date_str, DATE_FMT)
    return (base + timedelta(days=days)).strftime(DATE_FMT)

def validate_email(email: str) -> bool:
    if not email:
        return True
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None

def csv_authors_from_input(text: str) -> list:
    if not text:
        return []
    return [a.strip() for a in text.split(",") if a.strip()]

def csv_tags_from_input(text: str) -> list:
    if not text:
        return []
    return [t.strip() for t in text.split(",") if t.strip()]
