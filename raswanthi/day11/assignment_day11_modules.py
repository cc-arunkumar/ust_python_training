import os
import csv
import math
from datetime import date, datetime, timedelta
#creating directories for storing files
base_directory = "ust_order_processing"
input_directory = os.path.join(base_directory, "input")
output_directory = os.path.join(base_directory, "output")
log_directory = os.path.join(base_directory, "logs")

#creating and joining files with directories
orders_file = os.path.join(input_directory, "orders.csv")
processed_file = os.path.join(output_directory, "processed_orders.txt")
skipped_file = os.path.join(output_directory, "skipped_orders.txt")
log_file = os.path.join(log_directory, "execution_log.txt")


for folder in [base_directory, input_directory, output_directory, log_directory]:
    if not os.path.exists(folder):
        os.mkdir(folder)
        
#calculating estimated delivery
def calculate_delivery(order_date):
    delivery_date = order_date + timedelta(days=5)
    while delivery_date.weekday() == 6: 
        delivery_date += timedelta(days=1)
    return delivery_date

#processing orders
def process_orders():
    today = date.today().strftime("%Y-%m-%d")

    with open(log_file, "w") as logfile:
        logfile.write(f"[{today}] INFO: Started Order Processing\n")

    if not os.path.exists(orders_file):
        with open(log_file, "a") as logfile:
            logfile.write(f"[{today}] ERROR: Orders file not found\n")
        return

    with open(log_file, "a") as logfile:
        logfile.write(f"[{today}] INFO: Folder check completed\n")

    with (
        open(orders_file, "r") as csvfile,
        open(processed_file, "w") as processed,
        open(skipped_file, "w") as skipped
    ):
        reader = csv.DictReader(csvfile)

        for row in reader:
            order_id = row["order_id"]
            customer = row["customer_name"]
            product = row["product"]

            #validations
            with open(log_file, "a") as logfile:
                logfile.write(f"[{today}] INFO: Processing order {order_id}\n")

            if not row["quantity"].isdigit() or not row["unit_price"].isdigit():
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity/price\n")
                continue

            quantity = int(row["quantity"])
            unit_price = int(row["unit_price"])

            if quantity <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                continue

            if unit_price <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                continue

            try_date = row["order_date"].split("-")
            if len(try_date) != 3 or not all(part.isdigit() for part in try_date):
                skipped.write(f"OrderID: {order_id} | Reason: Invalid date format\n")
                continue

            try:
                order_date = datetime.strptime(row["order_date"], "%Y-%m-%d").date()
            except Exception:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid date\n")
                continue

            if order_date > date.today():
                skipped.write(f"OrderID: {order_id} | Reason: Order date in the future\n")
                continue
            
            total_cost = math.ceil(quantity * unit_price)
            delivery_date = calculate_delivery(order_date)

            #writing to processed
            processed.write(
                f"OrderID: {order_id}\n" f"Customer: {customer}\n"
                 f"Product: {product}\n" f"Quantity: {quantity}\n"
                f"Unit Price: {unit_price}\n" f"Total Cost: {total_cost}\n"
                f"Order Date: {order_date}\n" f"Estimated Delivery: {delivery_date}\n" + "-"*50 + "\n"
            )

            with open(log_file, "a") as logfile:
                logfile.write(f"[{today}] INFO: Order {order_id} processed successfully\n")

    with open(log_file, "a") as logfile:
        logfile.write(f"[{today}] INFO: Finished Order Processing\n")

if __name__ == "__main__":
    process_orders()
    
    
