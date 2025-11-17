# Modules Task

# UST Order Processing Utility
# Modules Covered: math , datetime , os
# Business Scenario
# UST’s internal procurement team receives daily CSV files that contain:
# Order IDs
# Customer names
# Product names
# Product quantities
# Price per unit
# Order date
# A new high-priority automated tool is needed for basic processing of these CSVs.
# Your job is to create a beginner-level Python script that performs simple
# calculations and file operations using:
# math → calculate totals
# datetime.date / datetime.timedelta → validate dates, estimate delivery date
# os → create folders, check file existence, generate logs
# This represents a mini internal utility, similar to tools used inside UST Delivery Projects.

# Final Expected Output
# Your script will:
# 1. Create required folders
# 2. Read a sample orders CSV
# 3. Calculate total order cost using math module
# 4. Validate order date using datetime module
# 5. Calculate estimated delivery date (skip Sundays)
# 6. Write output to a text file
# 7. Create a log file showing processed and skipped orders
# folder structure (that you must generate using
# Python)
# Your script must automatically create this structure:
# UST_Order_Processing/
#  input/
#  orders.csv ← you will place sample file here manually
#  output/
#  processed_orders.txt
#  skipped_orders.txt
#  logs/
#  execution_log.txt
# Use the os module to create the above folders if they don’t exist.
# Sample orders.csv
# order_id,customer_name,product,quantity,unit_price,order_date
# 101,Asha Nair,Laptop,2,45000,2025-01-10
# 102,Rahul Menon,Keyboard,3,1200,2025-01-15
# 103,Divya Iyer,Mouse,-1,700,2025-09-20
# 104,Pradeep Kumar,Monitor,1,8500,2025-02-30
# 105,Anjali S,Laptop,2,42000,2024-12-01

# Import required modules
import math
import os
import csv
from datetime import date, datetime, timedelta

# Define output folder and file for processed orders
target_path = os.getcwd() + '/output'
new_file1 = "processed_orders.txt"

# Create output directory if it doesn't exist
if not os.path.exists(target_path):
     os.mkdir('output')

# Create (or overwrite) processed orders file
new_file_path1 = os.path.join(target_path, new_file1)
with open(new_file_path1, 'w') as file:
    pass  # Just creates/clears the file

# Define file for skipped orders
new_file2 = "skipped_orders.txt"

# Ensure output directory still exists
if not os.path.exists(target_path):
     os.mkdir('output')

# Create (or overwrite) skipped orders file
new_file_path2 = os.path.join(target_path, new_file2)
with open(new_file_path2, 'w') as file:
    pass

# Define logs directory and file
target_path3 = os.getcwd() + '/logs'
new_file3 = "execution_log.txt"

# Create logs directory if needed
if not os.path.exists(target_path3):
     os.mkdir('logs')

# Create (or overwrite) execution log file
new_file_path3 = os.path.join(target_path3, new_file3)
with open(new_file_path3, 'w') as file:
    pass

# Initialize lists to store processed and skipped order data
processed_orders = []
skipped_orders = []
log_orders = []
today = date.today()

# Validate date format (YYYY-MM-DD)
def is_valid_date(date_string):
    try:
        od=datetime.strptime(date_string,"%Y-%m-%d")
        return od
    except:
        return None  # Return None if date is invalid

# Calculate estimated delivery (add 5 days and skip Sundays)
def calculate_delivery(order_date):
    estimated_delivery = order_date + timedelta(days=5)

    # If delivery falls on Sunday (weekday = 6), push forward one day
    while estimated_delivery.weekday() == 6:
        estimated_delivery += timedelta(days=1)

    return estimated_delivery


# Read orders from CSV file
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        # Extract fields from CSV row
        order_id = row[headers[0]]
        customer = row[headers[1]]
        product = row[headers[2]]
        qty = int(row[headers[3]])
        price = int(row[headers[4]])
        order_date_raw = row[headers[5]]

        # Validate quantity
        if qty <= 0:
            skipped_orders.append((order_id, "Invalid quantity"))
            continue

        # Validate unit price
        if price <= 0:
            skipped_orders.append((order_id, "Invalid unit price"))
            continue

        # Validate date format
        order_date = is_valid_date(order_date_raw)
        if not order_date:
            skipped_orders.append((order_id, "Invalid date"))
            continue

        # Skip orders from the future
        if order_date > today:
            skipped_orders.append((order_id, "Order date in the future"))
            continue

        # Calculate cost and delivery date for valid orders
        total_cost = math.ceil(qty * price)
        delivery_date = calculate_delivery(order_date)

        # Save processed order data
        processed_orders.append({
            "order_id": order_id,
            "customer": customer,
            "product": product,
            "qty": qty,
            "price": price,
            "total": total_cost,
            "order_date": order_date,
            "estimated_delivery": delivery_date
        })

# Write processed orders to output file
with open("output/processed_orders.txt", "w") as file:
    for processed in processed_orders:
        file.write(
            f"OrderID: {processed['order_id']}\n"
            f"Customer: {processed['customer']}\n"
            f"Product: {processed['product']}\n"
            f"Quantity: {processed['qty']}\n"
            f"Unit Price: {processed['price']}\n"
            f"Total Cost: {processed['total']}\n"
            f"Order Date: {processed['order_date']}\n"
            f"Estimated Delivery: {processed['estimated_delivery']}\n"
            f" ----------\n"
        )

# Write skipped orders to file
with open("output/skipped_orders.txt", "w") as file:
    for order_id, reason in skipped_orders:
        file.write(f"OrderID: {order_id} | Reason: {reason}\n")

# Final message
print("Order processing completed successfully!")
