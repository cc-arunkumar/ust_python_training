# utils.py
from datetime import datetime, timedelta

def today():
    return datetime.now().strftime("%d-%m-%Y")

def due_after_14_days():
    return (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

def generate_id(prefix, existing):
    n = len(existing) + 1
    return f"{prefix}{n}"
