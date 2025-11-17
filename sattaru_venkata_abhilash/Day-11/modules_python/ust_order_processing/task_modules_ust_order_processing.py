# UST Order Processing Utility
# Modules Covered: math , datetime , os

import math
import os
import csv
from datetime import date, datetime, timedelta

# -----------------------------
# CREATE OUTPUT AND LOG FOLDERS
# -----------------------------

target_path = os.getcwd() + '/output'
new_file1 = "processed_orders.txt"

if not os.path.exists(target_path):
    os.mkdir('output')

new_file_path1 = os.path.join(target_path, new_file1)
with open(new_file_path1, 'w') as file:
    pass   # Creates empty txt file

new_file2 = "skipped_orders.txt"
new_file_path2 = os.path.join(target_path, new_file2)
with open(new_file_path2, 'w') as file:
    pass

# Create logs folder
target_path3 = os.getcwd() + '/logs'
new_file3 = "execution_log.txt"

if not os.path.exists(target_path3):
    os.mkdir('logs')

new_file_path3 = os.path.join(target_path3, new_file3)
with open(new_file_path3, 'w') as file:
    pass

processed_orders = []
skipped_orders = []

today = date.today()
print("Today's date:", today)

# -----------------------------
# VALIDATE DATE FORMAT
# -----------------------------

def is_valid_date(date_string):
    try:
        y, m, d = map(int, date_string.split("-"))
        return date(y, m, d)
    except:
        return None

# -----------------------------
# CALCULATE DELIVERY DATE
# -----------------------------

def calculate_delivery(order_date):
    delivery = order_date + timedelta(days=5)

    # Skip Sunday
    while delivery.weekday() == 6:
        delivery += timedelta(days=1)

    return delivery

# -----------------------------
# READ CSV AND PROCESS ORDERS
# -----------------------------

print("Reading orders from CSV...")

with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    header = ["order_id", "customer_name", "product", "quantity", "unit_price", "order_date"]

    for row in reader:
        order_id = row[header[0]]
        customer = row[header[1]]
        product = row[header[2]]
        qty = int(row[header[3]])
        price = int(row[header[4]])
        order_date_raw = row[header[5]]

        print(f"\nProcessing Order ID: {order_id}")
        print(f"Customer: {customer}, Product: {product}")

        # -----------------------------
        # VALIDATIONS
        # -----------------------------

        if qty <= 0:
            print("❌ Skipped — Invalid Quantity")
            skipped_orders.append((order_id, "Invalid quantity"))
            continue

        if price <= 0:
            print("❌ Skipped — Invalid Unit Price")
            skipped_orders.append((order_id, "Invalid unit price"))
            continue

        order_date = is_valid_date(order_date_raw)
        if not order_date:
            print("❌ Skipped — Invalid Date Format")
            skipped_orders.append((order_id, "Invalid date"))
            continue

        if order_date > today:
            print("❌ Skipped — Date is in the future")
            skipped_orders.append((order_id, "Order date in the future"))
            continue

        # -----------------------------
        # VALID ORDER → PROCESS
        # -----------------------------

        total_cost = math.ceil(qty * price)
        delivery_date = calculate_delivery(order_date)

        print(f"✔ Valid Order")
        print(f"Quantity: {qty}, Unit Price: {price}")
        print(f"Total Cost (Rounded): {total_cost}")
        print(f"Order Date: {order_date}")
        print(f"Estimated Delivery: {delivery_date}")

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

# ------------------------------------------
# WRITE PROCESSED ORDERS TO TEXT FILE
# ------------------------------------------

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

# ------------------------------------------
# WRITE SKIPPED ORDERS
# ------------------------------------------

with open("skipped_orders.txt", "w") as file:
    for order_id, reason in skipped_orders:
        file.write(f"OrderID: {order_id} | Reason: {reason}\n")

print("\n===============================")
print("Order processing completed successfully!")
print(f"Total Processed: {len(processed_orders)}")
print(f"Total Skipped: {len(skipped_orders)}")
print("===============================")


# sample code:
# Today's date: 2025-11-17
# Reading orders from CSV...

# Processing Order ID: 101
# Customer: Rahul, Product: Keyboard
#  Valid Order
# Quantity: 2, Unit Price: 550
# Total Cost (Rounded): 1100
# Order Date: 2025-01-15
# Estimated Delivery: 2025-01-20

# Processing Order ID: 102
# Customer: Meena, Product: Mouse
#  Skipped — Invalid Quantity

# Processing Order ID: 103
# Customer: Arjun, Product: Laptop
#  Skipped — Date is in the future

# Processing Order ID: 104
# Customer: Riya, Product: Monitor
#  Skipped — Invalid Unit Price

# Processing Order ID: 105
# Customer: Sam, Product: Headset
#  Valid Order
# Quantity: 3, Unit Price: 1500
# Total Cost (Rounded): 4500
# Order Date: 2025-02-10
# Estimated Delivery: 2025-02-15

# Processing Order ID: 106
# Customer: John, Product: Cable
#  Skipped — Invalid Date Format

# Processing Order ID: 107
# Customer: Asha, Product: Charger
#  Skipped — Date is in the future

# Processing Order ID: 108
# Customer: Rohit, Product: USB Drive
#  Valid Order
# Quantity: 5, Unit Price: 450
# Total Cost (Rounded): 2250
# Order Date: 2025-01-10
# Estimated Delivery: 2025-01-15

# ===============================
# Order processing completed successfully!
# Total Processed: 3
# Total Skipped: 5
# ===============================
