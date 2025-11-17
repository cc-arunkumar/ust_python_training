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
# This represents a mini internal utility, similar to tools used inside UST Delivery
# Projects.
# Final Expected Output
# Your script will:
# 1. Create required folders
# Modules Task 1
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
# Modules Task 2
# Validation Rules You MUST Apply:
# Skip order if:
# quantity ≤ 0
# unit_price ≤ 0
# order_date is invalid (e.g., 2025-02-30)
# order_date is in the future beyond today
# Required CALCULATIONS (Using math
# module)
# For valid orders:
# total_cost = math.ceil(quantity * unit_price)
# Use ceil() to round UP the amount.
# Delivery Date Logic (Using datetime
# module)
# Delivery time is always 5 days after order date.
# But:
# If delivery date falls on a Sunday, add 1 more day
# If delivery date crosses two Sundays, skip both
# Use:
# from datetime import date, timedelta
# Example Delivery Calculation
# Modules Task 3
# Order date: 2025-01-10
# Add 5 days = 2025-01-15 (Check weekday)
# If Sunday ( weekday() == 6 ) → +1 day
# Output File Requirements
# processed_orders.txt format
# OrderID: 101
# Customer: Asha Nair
# Product: Laptop
# Quantity: 2
# Unit Price: 45000
# Total Cost: 90000
# Order Date: 2025-01-10
# Estimated Delivery: 2025-01-15
# --------------------------------------------------
# skipped_orders.txt format
# OrderID: 103 | Reason: Invalid quantity
# OrderID: 104 | Reason: Invalid date
# OrderID: 105 | Reason: Order date in the future
# LOG FILE Requirements
# (logs/execution_log.txt)
# Every step must be logged:
# [2025-01-18] INFO: Started Order Processing
# [2025-01-18] INFO: Folder check completed
# [2025-01-18] INFO: Processing order 101
# Modules Task 4
# [2025-01-18] INFO: Order 101 processed successfully
# [2025-01-18] WARNING: Order 104 skipped - Invalid date
# [2025-01-18] INFO: Finished Order Processing
# Use os.path.exists, os.mkdir, file handling, and datetime timestamps.




import os
import math
import csv
from datetime import datetime, date, timedelta

# creating the folders
folders = {
    "input": "task/input",
    "output": "task/output",
    "logs": "task/logs"
}
#setting path to the files
input_file = os.path.join(folders["input"], "orders.csv")
processed_file = os.path.join(folders["output"], "processed_orders.txt")
skipped_file = os.path.join(folders["output"], "skipped_orders.txt")
# creating the folder if not exists
def create_folders():
    for folder in folders.values():
        if not os.path.exists(folder):
            os.makedirs(folder)
# performing the validation rules
def validate_date(order_date_str):
    try:
        order_date = datetime.strptime(order_date_str, "%Y-%m-%d").date()
        if order_date > date.today():
            return False
        return True
    except ValueError:
        return False

def calculate_total_cost(quantity, unit_price):
    return math.ceil(quantity * unit_price)

def calculate_delivery_date(order_date):
    delivery_date = order_date + timedelta(days=5)
    if delivery_date.weekday() == 6:
        delivery_date += timedelta(days=1)
    return delivery_date.strftime("%d-%m-%y,%A:") + str(delivery_date.weekday())

def process_orders():
    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        processed_orders = []
        skipped_orders = []

        for row in reader:
            order_id = row["order_id"]
            customer_name = row["customer_name"]
            product = row["product"]
            quantity = int(row["quantity"])
            unit_price = float(row["unit_price"])
            order_date_str = row["order_date"]
            
            if quantity <= 0:
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid quantity")
                continue
            if unit_price <= 0:
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid price")
                continue
            if not validate_date(order_date_str):
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid date")
                continue

            order_date = datetime.strptime(order_date_str, "%Y-%m-%d").date()
            formatted_order_date = order_date.strftime("%d-%m-%y,%A:") + str(order_date.weekday())
            total_cost = calculate_total_cost(quantity, unit_price)
            estimated_delivery = calculate_delivery_date(order_date)

            processed_orders.append(f"""
OrderID: {order_id}
Customer: {customer_name}
Product: {product}
Quantity: {quantity}
Unit Price: {unit_price}
Total Cost: {total_cost}
Order Date: {formatted_order_date}
Estimated Delivery: {estimated_delivery}
--------------------------------------------------
            """)
        
        with open(processed_file, "w") as f:
            f.writelines(processed_orders)
        
        with open(skipped_file, "w") as f:
            f.writelines([f"{order}\n" for order in skipped_orders])

def main():
    create_folders()
    process_orders()

if __name__ == "__main__":
    main()
