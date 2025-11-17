import math
import os
from datetime import datetime, timedelta, date
import csv

# Base directory
target_dir = "C:\\Users\\Administrator\\Desktop\\Training\\ust_python_training\\harsh\\day11\\ust_order_processing"
input_file = os.path.join(target_dir, "input")
output_file = os.path.join(target_dir, "output")
log_dir = os.path.join(target_dir, "logs")

# Ensure output and log folders exist
for folder in [output_file, log_dir]:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Created folder: {folder}")
    else:
        print(f"Folder already exists: {folder}")

# File paths
ORDERS_FILE = os.path.join(input_file, "orders.csv")
PROCESSED_FILE = os.path.join(output_file, "processed_orders.txt")
SKIPPED_FILE = os.path.join(output_file, "skipped_orders.txt")
LOG_FILE = os.path.join(log_dir, "execution_log.txt")

# Logging function
def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    with open(LOG_FILE, "a") as logf:
        logf.write(f"{timestamp} {level}: {message}\n")

# Delivery calculation
def calculate_delivery(order_date):
    delivery_date = order_date + timedelta(days=7)
    while delivery_date.weekday() == 6:  
        delivery_date += timedelta(days=1)
    return delivery_date

# Main order processing
def process_orders():
    if not os.path.exists(ORDERS_FILE):
        print(f"Orders file does not exist: {ORDERS_FILE}")
        log("Orders file missing. Cannot process orders.", "ERROR")
        return
    else:
        print(f"Orders file exists: {ORDERS_FILE}")

    # Clear old output files
    open(PROCESSED_FILE, 'w').close()
    open(SKIPPED_FILE, 'w').close()

    with open(ORDERS_FILE, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader) 

        for row in reader:
            order_id = row[0]
            customer = row[1]
            product = row[2]

            try:
                quantity = int(row[3])
                unit_price = int(row[4])
            except ValueError:
                with open(SKIPPED_FILE, 'a') as sf:
                    sf.write(f"OrderID: {order_id} | Reason: Invalid Quantity or Price\n")
                log(f"Order {order_id} skipped - Invalid Quantity or Price", "WARNING")
                continue

            if quantity <= 0:
                with open(SKIPPED_FILE, "a") as skipf:
                    skipf.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                continue

            if unit_price <= 0:
                with open(SKIPPED_FILE, "a") as skipf:
                    skipf.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                continue

            try:
                order_date = datetime.strptime(row[5], "%Y-%m-%d").date()
            except ValueError:
                with open(SKIPPED_FILE, "a") as skipf:
                    skipf.write(f"OrderID: {order_id} | Reason: Invalid date\n")
                log(f"Order {order_id} skipped - Invalid date", "WARNING")
                continue

            if order_date > date.today():
                with open(SKIPPED_FILE, "a") as skipf:
                    skipf.write(f"OrderID: {order_id} | Reason: Order date in the future\n")
                log(f"Order {order_id} skipped - Future date", "WARNING")
                continue

            log(f"Processing Order {order_id}")
            total_cost = math.ceil(quantity * unit_price)
            delivery_date = calculate_delivery(order_date)

            with open(PROCESSED_FILE, 'a') as out:
                out.write(
                    f"OrderID: {order_id}\n"
                    f"Customer: {customer}\n"
                    f"Product: {product}\n"
                    f"Quantity: {quantity}\n"
                    f"Unit Price: {unit_price}\n"
                    f"Total Cost: {total_cost}\n"
                    f"Order Date: {order_date}\n"
                    f"Estimated Delivery: {delivery_date}\n"
                    + "-"*50 + "\n"
                )

            log(f"Order {order_id} processed successfully")

    log("Finished Order Processing")

# Run the script
if __name__ == "__main__":
    process_orders()
