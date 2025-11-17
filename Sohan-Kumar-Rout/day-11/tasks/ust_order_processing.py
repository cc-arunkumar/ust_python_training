import os
import math
import csv
from datetime import date, datetime, timedelta

BASE_DIR = "UST_Order_Processing"  
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

ORDERS_FILE = os.path.join(INPUT_DIR, "orders_in.csv")   
PROCESSED_FILE = os.path.join(OUTPUT_DIR, "processed_orders.txt")
SKIPPED_FILE = os.path.join(OUTPUT_DIR, "skipped_orders.txt")
LOG_FILE = os.path.join(LOG_DIR, "execution_log.txt")

def log(message, level="INFO"):
    timestamp = date.today().isoformat()
    with open(LOG_FILE, "a") as logf:
        logf.write(f"[{timestamp}] {level}: {message}\n")

def folders():
    for folder in [BASE_DIR, INPUT_DIR, OUTPUT_DIR, LOG_DIR]:
        os.makedirs(folder, exist_ok=True)
    log("Folder check completed")

def validate_date(order_date_str):
    try:
        order_date = datetime.strptime(order_date_str, "%d/%m/%Y").date()

        # order_date = datetime.strptime(order_date_str, "%Y/%m/%d").date()
    except ValueError:
        return None, "Invalid date"

    if order_date > date.today():
        return None, "Order date in the future"

    return order_date, None

def calculate_delivery(order_date):
    """Calculate delivery date (5 days after order date, skipping Sundays)."""
    delivery_date = order_date + timedelta(days=5)
    while delivery_date.weekday() == 6:  # Sunday = 6
        delivery_date += timedelta(days=1)
    return delivery_date

def process_orders():
    log("Started Order Processing")

    with open(ORDERS_FILE, "r") as file, \
         open(PROCESSED_FILE, "w") as processed, \
         open(SKIPPED_FILE, "w") as skipped:

        reader = csv.DictReader(file)

        for row in reader:
            order_id = row["order_id"]
            customer = row["customer_name"]
            product = row["product"]
            try:
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
            except ValueError:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity/price\n")
                log(f"Order {order_id} skipped - Invalid quantity/price", "WARNING")
                continue

            order_date, error = validate_date(row["order_date"])
            if error:
                skipped.write(f"OrderID: {order_id} | Reason: {error}\n")
                log(f"Order {order_id} skipped - {error}", "WARNING")
                continue

            if quantity <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                continue

            if unit_price <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                continue

            # Valid order → process
            log(f"Processing order {order_id}")
            total_cost = math.ceil(quantity * unit_price)
            delivery_date = calculate_delivery(order_date)

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
    folders()
    process_orders()
