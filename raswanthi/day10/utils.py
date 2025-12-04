
from datetime import datetime, timedelta

DATE_FMT = "%d-%m-%Y"

def today_str():
    return datetime.now().strftime(DATE_FMT)

def add_days(date_str, days):
    dt = datetime.strptime(date_str, DATE_FMT)
    return (dt + timedelta(days=days)).strftime(DATE_FMT)

def parse_comma_list(s):
    return [x.strip() for x in s.split(",") if x.strip()] if s else []

def make_tx_id(next_num):
    return f"T{next_num}"
