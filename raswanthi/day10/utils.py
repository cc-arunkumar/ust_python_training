#importing datetime, timedelta
from datetime import datetime, timedelta
from typing import Tuple

DATE_FMT = "%d-%m-%Y"


def today_str() -> str:
    return datetime.now().strftime(DATE_FMT)


def add_days(date_str: str, days: int) -> str:
    dt = datetime.strptime(date_str, DATE_FMT)
    return (dt + timedelta(days=days)).strftime(DATE_FMT)


def parse_comma_list(s: str) -> list:
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def make_tx_id(next_num: int) -> str:
    return f"T{next_num}"


def make_book_id_seq(prefix: str, next_num: int) -> str:
    return f"{prefix}{next_num}"


def validate_non_empty(label: str, value: str) -> Tuple[bool, str]:
    if not value or not value.strip():
        return False, f"{label} cannot be empty."
    return True, ""

