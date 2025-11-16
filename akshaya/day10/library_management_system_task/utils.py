# utils.py
from datetime import datetime, timedelta

DATE_FMT = "%d-%m-%Y"

def today_str():
    return datetime.now().strftime(DATE_FMT)

def due_date_str(days):
    return (datetime.now() + timedelta(days=days)).strftime(DATE_FMT)

def parse_comma_list(value):
    if not value or not value.strip():
        return []
    return [v.strip() for v in value.split(",") if v.strip()]

def input_nonempty(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input cannot be empty.")
    return value
