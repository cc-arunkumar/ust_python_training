import os
import math
import csv
from datetime import date, datetime, timedelta

# === BASE FOLDER ===
BASE_FOLDER = r"C:/UST python/Praveen D/day 11/UST_Order_Processing"

# === SUB FOLDERS ===
INPUT_FOLDER = os.path.join(BASE_FOLDER, "input")
OUTPUT_FOLDER = os.path.join(BASE_FOLDER, "output")
LOG_FOLDER = os.path.join(BASE_FOLDER, "logs")

# === FILE PATHS ===
ORDERS_FILE = os.path.join(INPUT_FOLDER, "orders.csv")
PROCESSED_FILE = os.path.join(OUTPUT_FOLDER, "processed_orders.txt")
SKIPPED_FILE = os.path.join(OUTPUT_FOLDER, "skipped_orders.txt")
LOG_FILE = os.path.join(LOG_FOLDER, "execution_log.txt")


def log(message, level="INFO"):
    today_str = date.today().isoformat()
    line = f"[{today_str}] {level}: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(line)


def create_folders():
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    os.makedirs(LOG_FOLDER, exist_ok=True)


def read_orders():
    orders = []
    if not os.path.exists(ORDERS_FILE):
        log("orders.csv not found in input folder", level="WARNING")
        return orders

    with open(ORDERS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            orders.append(row)
    return orders


def parse_order_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d").date()
        return dt, None
    except ValueError:
        return None, "Invalid date"


def calculate_delivery_date(order_date):

    days_added = 0
    current = order_date
    while days_added < 5:
        current += timedelta(days=1)
        if current.weekday() != 6:  # not Sunday
            days_added += 1
    return current


def validate_order(row):

    # quantity
    try:
        quantity = int(row["quantity"])
    except ValueError:
        return False, "Invalid quantity format", None

    if quantity <= 0:
        return False, "Invalid quantity", None

    # unit_price
    try:
        unit_price = float(row["unit_price"])
    except ValueError:
        return False, "Invalid unit price format", None

    if unit_price <= 0:
        return False, "Invalid unit price", None

    # order_date
    order_date_str = row["order_date"]
    order_date, date_error = parse_order_date(order_date_str)
    if date_error is not None:
        return False, date_error, None

    # future date check
    today = date.today()
    if order_date > today:
        return False, "Order date in the future", None

    # all good
    return True, None, order_date


def process_orders():
    create_folders()
    log("Started Order Processing")

    orders = read_orders()
    log("Folder check completed")
    log(f"Total orders read: {len(orders)}")

    with open(PROCESSED_FILE, "w", encoding="utf-8") as processed_file, \
         open(SKIPPED_FILE, "w", encoding="utf-8") as skipped_file:

        for row in orders:
            order_id = row.get("order_id", "").strip()
            log(f"Processing order {order_id}")

            is_valid, reason, order_date = validate_order(row)

            if not is_valid:
                skipped_line = f"OrderID: {order_id} | Reason: {reason}\n"
                skipped_file.write(skipped_line)
                log(f"Order {order_id} skipped - {reason}", level="WARNING")
                continue

            quantity = int(row["quantity"])
            unit_price = float(row["unit_price"])
            total_cost = math.ceil(quantity * unit_price)

            delivery_date = calculate_delivery_date(order_date)

            processed_file.write(f"OrderID: {order_id}\n")
            processed_file.write(f"Customer: {row['customer_name']}\n")
            processed_file.write(f"Product: {row['product']}\n")
            processed_file.write(f"Quantity: {quantity}\n")
            processed_file.write(f"Unit Price: {int(unit_price)}\n")
            processed_file.write(f"Total Cost: {total_cost}\n")
            processed_file.write(f"Order Date: {order_date.isoformat()}\n")
            processed_file.write(f"Estimated Delivery: {delivery_date.isoformat()}\n")
            processed_file.write("-" * 50 + "\n")

            log(f"Order {order_id} processed successfully")

    log("Finished Order Processing")


if __name__ == "__main__":
    process_orders()
