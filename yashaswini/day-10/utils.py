# utils.py
import os, csv
from datetime import datetime, timedelta

DATE_FMT = "%m/%d/%Y"  # matches your CSV format (MM/DD/YYYY)

def today_str() -> str:
    return datetime.today().strftime(DATE_FMT)

def add_days(date_str: str, days: int) -> str:
    dt = datetime.strptime(date_str, DATE_FMT)
    return (dt + timedelta(days=days)).strftime(DATE_FMT)

def parse_date(date_str: str):
    return datetime.strptime(date_str, DATE_FMT)

def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")

def split_pipe(value: str):
    return [s.strip() for s in value.split("|") if s.strip()]

def split_comma(value: str):
    return [s.strip() for s in value.split(",") if s.strip()]

def read_csv(path: str):
    with open(path, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_csv(path: str, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
