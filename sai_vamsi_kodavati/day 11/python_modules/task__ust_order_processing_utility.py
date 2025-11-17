# task__ust_order_processing_utility

import math
import os
import csv
from datetime import date, datetime, timedelta

# Define output directory paths and filenames
target_path = os.getcwd() + '/output'
new_file1 = "processed_orders.txt"

# Create the output directory if it doesn't exist
if not os.path.exists(target_path):
     os.mkdir('output')

# Create/clear the processed orders output file
new_file_path1 = os.path.join(target_path, new_file1)
with open(new_file_path1, 'w') as file:
    pass

# Repeat setup for skipped orders file
target_path = os.getcwd() + '/output'
new_file2 = "skipped_orders.txt"

if not os.path.exists(target_path):
     os.mkdir('output')

new_file_path2 = os.path.join(target_path, new_file2)
with open(new_file_path2, 'w') as file:
    pass

# Setup for log directory
target_path3 = os.getcwd() + '/logs'
new_file3 = "execution_log.txt"

# Create logs directory if missing
if not os.path.exists(target_path3):
     os.mkdir('logs')

# Create/clear execution log file
new_file_path3 = os.path.join(target_path3, new_file3)
with open(new_file_path3, 'w') as file:
    pass

# Lists to track processed and skipped orders
processed_orders = []
skipped_orders = []

# Capture today's date for validation
today = date.today()

def is_valid_date(date_string):
    """Validate date format (YYYY-MM-DD). Return date object or None on failure."""
    try:
        y, m, d = map(int, date_string.split("-"))
        return date(y, m, d)
    except:
        return None

def calculate_delivery(order_date):
    """
    Add 5 days to the order date.
    If the resulting day is Sunday (weekday 6), shift to Monday.
    """
    delivery = order_date + timedelta(days=5)

    # Avoid Sunday delivery
    while delivery.weekday() == 6:
        delivery += timedelta(days=1)

    return delivery

# Read orders from CSV file
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)

    # Define expected CSV header keys
    header = ["order_id", "customer_name", "product", "quantity", "unit_price", "order_date"]

    for row in reader:
        # Extract and convert order fields
        order_id = row[header[0]]
        customer = row[header[1]]
        product = row[header[2]]
        qty = int(row[header[3]])
        price = int(row[header[4]])
        order_date_raw = row[header[5]]

        # Validate quantity
        if qty <= 0:
            skipped_orders.append((order_id, "Invalid quantity"))
            continue

        # Validate price
        if price <= 0:
            skipped_orders.append((order_id, "Invalid unit price"))
            continue

        # Validate order date format
        order_date = is_valid_date(order_date_raw)
        if not order_date:
            skipped_orders.append((order_id, "Invalid date"))
            continue

        # Ensure date is not in the future
        if order_date > today:
            skipped_orders.append((order_id, "Order date in the future"))
            continue

        # Calculate total cost and estimated delivery date
        total_cost = math.ceil(qty * price)
        delivery_date = calculate_delivery(order_date)

        # Store processed order info
        processed_orders.append({
            "order_id": order_id,
            "customer": customer,
            "product": product,
            "qty": qty,
            "price": price,
            "total": total_cost,
            "order_date": order_date.isoformat(),
            "delivery": delivery_date.isoformat()
        })

# Write processed orders to output file
with open("processed_orders.txt", "w") as file:
    for p in processed_orders:
        file.write(f"OrderID: {p['order_id']}\n")
        file.write(f"Customer: {p['customer']}\n")
        file.write(f"Product: {p['product']}\n")
        file.write(f"Quantity: {p['qty']}\n")
        file.write(f"Unit Price: {p['price']}\n")
        file.write(f"Total Cost: {p['total']}\n")
        file.write(f"Order Date: {p['order_date']}\n")
        file.write(f"Estimated Delivery: {p['delivery']}\n")
        file.write("-" * 50 + "\n")

# Write skipped orders to separate file
with open("skipped_orders.txt", "w") as file:
    for order_id, reason in skipped_orders:
        file.write(f"OrderID: {order_id} | Reason: {reason}\n")

print("Order processing completed successfully!")


# ---------------------------------------------------------------------------

# Sample Output

# Order processing completed successfully!