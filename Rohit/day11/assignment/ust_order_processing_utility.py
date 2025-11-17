import csv
import math
import os
from datetime import datetime, date, timedelta

# Use your path directly
BASE_DIR = r"C:\Users\Administrator\Desktop\ust_python_training\rohit\day11\assignment"

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

ORDERS_FILE = os.path.join(BASE_DIR, "order.csv")   # <-- your file directly
PROCESSED_FILE = os.path.join(OUTPUT_DIR, "processed_orders.txt")
SKIPPED_FILE = os.path.join(OUTPUT_DIR, "skipped_orders.txt")
LOG_FILE = os.path.join(LOG_DIR, "execution_log.txt")

def log(message, level="INFO"):
    timestamp = date.today().strftime("%Y-%m-%d")
    entry = f"[{timestamp}] {level}: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(entry)

def setup_folders():
    for folder in [INPUT_DIR, OUTPUT_DIR, LOG_DIR]:
        if not os.path.exists(folder):
            os.mkdir(folder)
    log("Folder check completed")

def parse_date(date_str):
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

def calculate_delivery_date(order_date):
    delivery_date = order_date + timedelta(days=5)
    sundays_crossed = 0
    for i in range(1, 6):
        check_day = order_date + timedelta(days=i)
        if check_day.weekday() == 6:
            sundays_crossed += 1
    delivery_date += timedelta(days=sundays_crossed)
    return delivery_date

def process_orders():
    today = date.today()
    log("Started Order Processing")

    if not os.path.exists(ORDERS_FILE):
        log("Orders file not found", "ERROR")
        return

    with open(ORDERS_FILE, mode="r", encoding="utf-8" ) as file, \
         open(PROCESSED_FILE, "w", encoding="utf-8") as processed, \
         open(SKIPPED_FILE, "w", encoding="utf-8") as skipped:

        reader = csv.DictReader(file, delimiter="\t") 
        # headers = reader.fieldnames
        next(reader)
        header = reader.fieldnames
        print(header[0])# Skip header row if present
        print(f"Headers found: {header}")
        for row in reader:
            order_id = header[0]
            customer = header[1]
            product = header[2]

            try:
                quantity = int(row.get("quantity"))
                unit_price = int(row.get("unit_price"))
            except (TypeError, ValueError):
                skipped.write(f"OrderID: {order_id} | Reason: Invalid numeric values\n")
                log(f"Order {order_id} skipped - Invalid numeric values", "WARNING")
                continue
            

            order_date_str = row.get("order_date")
            order_date = parse_date(order_date_str)

            if quantity <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                continue
            
            if unit_price <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                continue
            
            if order_date is None:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid date\n")
                log(f"Order {order_id} skipped - Invalid date", "WARNING")
                continue
            
            if order_date >= today:
                skipped.write(f"OrderID: {order_id} | Reason: Order date in the future\n")
                log(f"Order {order_id} skipped - Future date", "WARNING")
                continue

            log(f"Processing order {order_id}")

            total_cost = math.ceil(quantity * unit_price)
            delivery_date = calculate_delivery_date(order_date)

            processed.write(
                f"OrderID: {order_id}\n"
                f"Customer: {customer}\n"
                f"Product: {product}\n"
                f"Quantity: {quantity}\n"
                f"Unit Price: {unit_price}\n"
                f"Total Cost: {total_cost}\n"
                f"Order Date: {order_date}\n"
                f"Estimated Delivery: {delivery_date}\n"
                "--------------------------------------------------\n"
            )

            log(f"Order {order_id} processed successfully")

    log("Finished Order Processing")

if __name__ == "__main__":
    setup_folders()
    process_orders()
