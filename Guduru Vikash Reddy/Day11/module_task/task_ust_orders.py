import math

import os

import csv

from datetime import date, datetime, timedelta

target_path=os.getcwd() + '/output'

new_file1="processed_orders.txt"

if not os.path.exists(target_path):

     os.mkdir('output')

new_file_path1 = os.path.join(target_path,new_file1)

with open(new_file_path1,'w') as file:

    pass

 

target_path=os.getcwd() + '/output'

new_file2="skipped_orders.txt"

 

if not os.path.exists(target_path):

     os.mkdir('output')

new_file_path2 = os.path.join(target_path,new_file2)

with open(new_file_path2,'w') as file:

    pass

 

target_path3=os.getcwd() + '/logs'

new_file3="execution_log.txt"

 

if not os.path.exists(target_path3):

     os.mkdir('logs')

new_file_path3 = os.path.join(target_path3,new_file3)

with open(new_file_path3,'w') as file:

    pass

 
processed_orders = []

skipped_orders = []

today = date.today()

def is_valid_date(date_string):

    try:

        y, m, d = map(int, date_string.split("-"))

        return date(y, m, d)

    except:

        return None

 

 

def calculate_delivery(order_date):

    delivery = order_date + timedelta(days=5)

 

    while delivery.weekday() == 6:  

        delivery += timedelta(days=1)

 

    return delivery

 

 

with open("orders.csv", "r") as file:

    reader = csv.DictReader(file)

    header=["order_id","customer_name","product","quantity","unit_price","order_date"]

    for row in reader:

        order_id = row[header[0]]

        customer = row[header[1]]

        product = row[header[2]]

        qty = int(row[header[3]])

        price = int(row[header[4]])

        order_date_raw = row[header[5]]

 

        if qty <= 0:

            skipped_orders.append((order_id, "Invalid quantity"))

            continue

 

        if price <= 0:

            skipped_orders.append((order_id, "Invalid unit price"))

            continue

 

        order_date = is_valid_date(order_date_raw)

        if not order_date:

            skipped_orders.append((order_id, "Invalid date"))

            continue

 

        if order_date > today:

            skipped_orders.append((order_id, "Order date in the future"))

            continue

 

        total_cost = math.ceil(qty * price)

        delivery_date = calculate_delivery(order_date)

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

 

with open("output/processed_orders.txt", "w") as file:

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

with open("output/skipped_orders.txt", "w") as file:

    for order_id, reason in skipped_orders:

        file.write(f"OrderID: {order_id} | Reason: {reason}\n")


print("Order processing completed successfully!")

 






