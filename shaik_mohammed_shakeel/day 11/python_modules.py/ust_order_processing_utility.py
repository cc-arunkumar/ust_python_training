import math
import os
import csv
from datetime import date, datetime, timedelta
 
# Directory where output files will be created
target_path = os.getcwd() + '/output'
new_file1 = "processed_orders.txt"
 
# Create output directory if not present
if not os.path.exists(target_path):
     os.mkdir('output')

# Create an empty processed_orders.txt file
new_file_path1 = os.path.join(target_path, new_file1)
with open(new_file_path1, 'w') as file:
    pass
 
# Creating skipped_orders.txt in same output directory
target_path = os.getcwd() + '/output'
new_file2 = "skipped_orders.txt"
 
if not os.path.exists(target_path):
     os.mkdir('output')

new_file_path2 = os.path.join(target_path, new_file2)
with open(new_file_path2,'w') as file:
    pass
 
# Directory for logs
target_path3 = os.getcwd() + '/logs'
new_file3 = "execution_log.txt"
 
# Create logs directory if missing
if not os.path.exists(target_path3):
     os.mkdir('logs')

# Create empty execution log file
new_file_path3 = os.path.join(target_path3, new_file3)
with open(new_file_path3,'w') as file:
    pass
 
# Lists to store valid and invalid orders
processed_orders = []
skipped_orders = []
 
# Current date used to validate order dates
today = date.today()
 
# -----------------------------
# FUNCTION: Validate a date string (YYYY-MM-DD)
# Returns date object if valid, otherwise None
# -----------------------------
def is_valid_date(date_string):
    try:
        y, m, d = map(int, date_string.split("-"))
        return date(y, m, d)
    except:
        return None
 
# -----------------------------
# FUNCTION: Calculate delivery date
# Adds 5 days, skips Sundays
# -----------------------------
def calculate_delivery(order_date):
    delivery = order_date + timedelta(days=5)

    # If delivery date falls on Sunday, move to Monday
    while delivery.weekday() == 6:  
        delivery += timedelta(days=1)

    return delivery
 
# -----------------------------
# MAIN: Read and process orders CSV
# -----------------------------
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames   # Column names

    for row in reader:

        # Extract values from row
        order_id = row[header[0]]
        customer = row[header[1]]
        product = row[header[2]]
        qty = int(row[header[3]])
        price = int(row[header[4]])
        order_date_raw = row[header[5]]

        # -------- Validation checks --------

        # Quantity must be positive
        if qty <= 0:
            skipped_orders.append((order_id, "Invalid quantity"))
            continue
 
        # Unit price must be positive
        if price <= 0:
            skipped_orders.append((order_id, "Invalid unit price"))
            continue
 
        # Check date format
        order_date = is_valid_date(order_date_raw)
        if not order_date:
            skipped_orders.append((order_id, "Invalid date"))
            continue
 
        # Order date cannot be in the future
        if order_date > today:
            skipped_orders.append((order_id, "Order date in the future"))
            continue
 
        # Calculate cost & delivery date
        total_cost = math.ceil(qty * price)
        delivery_date = calculate_delivery(order_date)

        # Save valid order details
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
 
# -----------------------------
# WRITE VALID ORDERS TO FILE
# -----------------------------
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

# -----------------------------
# WRITE SKIPPED ORDERS TO FILE
# -----------------------------
with open("skipped_orders.txt", "w") as file:
    for order_id, reason in skipped_orders:
        file.write(f"OrderID: {order_id} | Reason: {reason}\n")
 
# Completion message
print("Order processing completed successfully!")

#sample output
# Order processing completed successfully!