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
import os
import math
import datetime
import csv

# Define folder and file paths
folders = ["task_module/UST_Order_processing/input", "task_module/UST_Order_processing/output", "task_module/UST_Order_processing/logs"]
files = ["task_module/UST_Order_processing/output/processed_orders.txt", "task_module/UST_Order_processing/output/skipped_orders.txt", "task_module/UST_Order_processing/logs/execution.txt"]

# Create the necessary folders and files
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)  
        print(f"Folder created: {folder}")
    else:
        print(f"Folder already exists: {folder}")

for file_path in files:
    if not os.path.exists(file_path): 
        with open(file_path, 'w') as file:  
            file.write("")  
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

input_csv = "task_module/UST_Order_processing/input/orders.csv"
processed_output_file = "task_module/UST_Order_processing/output/processed_orders.txt"
skipped_output_file = "task_module/UST_Order_processing/output/skipped_orders.txt"


def validate(orders):
    if orders["quantity"] <= 0:
        return False, "Invalid quantity"
    if orders["unit_price"] <= 0:
        return False, "Invalid unit price"
    
    try:
        order_date = datetime.date.fromisoformat(orders["order_date"])
    except ValueError:
        return False, "Invalid date format"
    
    if order_date >= datetime.date.today():
        return False, "Order date in the future"
    return True, None
def calculate_total_cost(orders):
    return math.ceil(orders["quantity"] * orders["unit_price"])
def get_estimated_date(order_date):
    delivery_date = order_date + datetime.timedelta(days=5)
    if delivery_date.weekday() == 6:
        delivery_date += datetime.timedelta(days=1)
    if (delivery_date + datetime.timedelta(days=7)).weekday() == 6:
        return None 
    return delivery_date
def process_orders_from_csv(csv_file):
    processed_orders = []
    skipped_orders = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            order = {
                "order_id": int(row["order_id"]),"customer": row["customer_name"],
                "product": row["product"],"quantity": int(row["quantity"]),
                "unit_price": float(row["unit_price"]),"order_date": row["order_date"]}
            is_valid, reason = validate(order)
            if is_valid:
                order_date = datetime.date.fromisoformat(order["order_date"])
                total_cost = calculate_total_cost(order)
                delivery_date = get_estimated_date(order_date)
                
                if delivery_date:
                    processed_orders.append({
                        "order_id": order["order_id"],"customer": order["customer"],
                        "product": order["product"],"quantity": order["quantity"],
                        "unit_price": order["unit_price"],"total_cost": total_cost,
                        "order_date": order_date,"estimated_delivery": delivery_date})
                else:
                    skipped_orders.append(f"OrderID: {order['order_id']} | Reason: Delivery crosses two Sundays")
            else:
                skipped_orders.append(f"OrderID: {order['order_id']} | Reason: {reason}")

    
    return processed_orders, skipped_orders
def write_processed_orders(orders):
    with open(processed_output_file, "w") as f:
        for order in orders:
            f.write(f"OrderID: {order['order_id']}\n")
            f.write(f"Customer: {order['customer']}\n")
            f.write(f"Product: {order['product']}\n")
            f.write(f"Quantity: {order['quantity']}\n")
            f.write(f"Unit Price: {order['unit_price']}\n")
            f.write(f"Total Cost: {order['total_cost']}\n")
            f.write(f"Order Date: {order['order_date']}\n")
            f.write(f"Estimated Delivery: {order['estimated_delivery']}\n")
            f.write("-" * 50 + "\n")
    print(f"Processed orders written to {processed_output_file}")
def write_skipped_orders(skipped_orders):
    with open(skipped_output_file, "w") as f:
        for skipped_order in skipped_orders:
            f.write(skipped_order + "\n")
    print(f"Skipped orders written to {skipped_output_file}")
processed_orders, skipped_orders = process_orders_from_csv(input_csv)
write_processed_orders(processed_orders)
write_skipped_orders(skipped_orders)





# skipped_orders
# OrderID: 103 | Reason: Invalid quantity
# OrderID: 104 | Reason: Invalid date format
# OrderID: 105 | Reason: Order date in the future
# OrderID: 107 | Reason: Invalid quantity
# OrderID: 108 | Reason: Invalid unit price





# processed_orders
# OrderID: 101Customer: Asha NairProduct: LaptopQuantity: 2Unit Price: 45000.0Total Cost: 90000Order Date: 2025-01-10Estimated Delivery: 2025-01-15--------------------------------------------------
# OrderID: 102Customer: Rahul MenonProduct: KeyboardQuantity: 3Unit Price: 1200.0Total Cost: 3600Order Date: 2025-01-15Estimated Delivery: 2025-01-20--------------------------------------------------
# OrderID: 106Customer: Sameer RProduct: HeadphonesQuantity: 1Unit Price: 2500.0Total Cost: 2500Order Date: 2025-03-05Estimated Delivery: 2025-03-10--------------------------------------------------