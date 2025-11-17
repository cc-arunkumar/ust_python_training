#Task UST Order Processing Utility

#importing modules
import os
import csv
import math
from datetime import date, datetime, timedelta

#files and directories fromation
BASE_DIR = "UST_Order_Processing"
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

ORDERS_FILE = os.path.join(INPUT_DIR, "orders_input.csv")
PROCESSED_FILE = os.path.join(OUTPUT_DIR, "processed_orders.txt")
SKIPPED_FILE = os.path.join(OUTPUT_DIR, "skipped_orders.txt")
LOG_FILE = os.path.join(LOG_DIR, "execution_log.txt")

#Log file creation
def log(message, level="INFO"):
    timestamp = date.today().strftime("%Y-%m-%d")
    entry = f"[{timestamp}] {level}: {message}\n"
    with open(LOG_FILE, "a") as logf:
        logf.write(entry)

#Setting up the directory structure
def folders():
    for folder in [BASE_DIR, INPUT_DIR, OUTPUT_DIR, LOG_DIR]:
        if not os.path.exists(folder):
            os.mkdir(folder)
    log("Folder check completed")

#Validation in date
def validate_date(order_date_str):
    try:
        order_dt = datetime.strptime(order_date_str, "%d/%m/%Y").date()
        if order_dt > date.today():
            return None, "Order date is in the future"
        return order_dt, None
    except ValueError:
        return None, "Invalid date format"
    
#Calculating the delivery
def calculate_delivery(order_dt):
    delivery_dt = order_dt + timedelta(days=5)
    while delivery_dt.weekday() == 6:
        delivery_dt += timedelta(days=1)
    return delivery_dt

#Adding datas in processed file and skipped file by reading the orders_input.csv
def process_orders():
    log("Started Order Processing")

    if not os.path.exists(ORDERS_FILE):
        log("Orders file not found", level="ERROR")
        return

    with open(ORDERS_FILE, "r", newline="") as csvfile, \
         open(PROCESSED_FILE, "w") as processed, \
         open(SKIPPED_FILE, "w") as skippedfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            order_id = row["order_id"]
            customer = row["customer_name"]
            product = row["product"]
            try:
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
            except ValueError:
                skippedfile.write(f"OrderID: {order_id} | Reason: Invalid number format\n")
                log(f"Order {order_id} skipped - Invalid number format", level="WARNING")
                continue

            order_dt, reason = validate_date(row["order_date"])
            if quantity <= 0:
                skippedfile.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", level="WARNING")
                continue
            if unit_price <= 0:
                skippedfile.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price", level="WARNING")
                continue
            if order_dt is None:
                skippedfile.write(f"OrderID: {order_id} | Reason: {reason}\n")
                log(f"Order {order_id} skipped - {reason}", level="WARNING")
                continue

            log(f"Processing order {order_id}")
            total_cost = math.ceil(quantity * unit_price)
            delivery_dt = calculate_delivery(order_dt)

            processed.write(
                f"OrderID: {order_id}\n"
                f"Customer: {customer}\n"
                f"Product: {product}\n"
                f"Quantity: {quantity}\n"
                f"Unit Price: {unit_price:.2f}\n"
                f"Total Cost: {total_cost}\n"
                f"Order Date: {order_dt}\n"
                f"Estimated Delivery: {delivery_dt}\n\n"
            )
            log(f"Order {order_id} processed successfully")

    log("Finished Order Processing")

if __name__ == "__main__":
    folders()
    process_orders()
