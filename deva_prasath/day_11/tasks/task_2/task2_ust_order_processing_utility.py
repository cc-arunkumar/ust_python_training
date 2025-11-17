#  UST Order Processing Utility 
# Modules Covered: 
# math , 
# datetime , 
# Business Scenario
#  os
#  USTʼs internal procurement team receives daily CSV files that contain:
#  Order IDs
#  Customer names
#  Product names
#  Product quantities
#  Price per unit
#  Order date
#  A new high-priority automated tool is needed for basic processing of these CSVs.
#  Your job is to create a beginner-level Python script that performs simple 
# calculations and file operations using:
#  math → calculate totals
#  datetime.date / datetime.timedelta → validate dates, estimate delivery date
#  os → create folders, check file existence, generate logs
#  This represents a mini internal utility, similar to tools used inside UST Delivery 
# Projects.

import os
import csv
import math
import datetime
from datetime import date
from datetime import timedelta
from datetime import datetime
import logging

#creating log file
LOG_FILE=os.path.join(r"D:\training\ust_python_training\UST_Order_Processing\logs","execution_log.txt")

def log(message,level="INFO"):
    timestamp=date.today().strftime("%Y-%m-%d")
    entry=f"[{timestamp}] {level}:{message}\n"
    with open(LOG_FILE,'a') as logf:
        logf.write(entry)

#initialising directory paths
folders=[
    "UST_Order_Processing/input",
    "UST_Order_Processing/output",
    "UST_Order_Processing/logs",
]
#checking and creating
for i in folders:
    if not os.path.exists(i):
        os.makedirs(i)

input_file=r"D:\training\ust_python_training\UST_Order_Processing\input\orders.csv"
orders=[]

with open(input_file,newline="") as file:
    #read as dict
    reader=csv.DictReader(file)
    for row in reader:
        #appending to list orders
        orders.append(row)

#validation total_cost
def calculate_total_cost(quantity,unit_price):
    return math.ceil(quantity*unit_price)

#date validation
def validate_date(order_date_str):
    try:
        order_date=datetime.strptime(order_date_str,"%Y-%m-%d").date()
        today=datetime.today().date()
        if order_date>today:
            return False,"Order date in the future"
        return True, order_date
    except ValueError:
        return False,"Invalid date"


#delivery date calculation
def calculate_delivery_date(order_date):
    delivery_date=order_date+timedelta(days=5)
    while delivery_date.weekday()==6:  
        delivery_date+=timedelta(days=1)
    return delivery_date

#writing processed orders in processed file
def write_processed(processed_orders):
    with open("UST_Order_Processing/output/processed_orders.txt","w") as file:
        for order in processed_orders:
            file.write(f"OrderID:{order['order_id']}\n")
            file.write(f"Customer:{order['customer_name']}\n")
            file.write(f"Product:{order['product']}\n")
            file.write(f"Quantity:{order['quantity']}\n")
            file.write(f"Unit Price:{order['unit_price']}\n")
            file.write(f"Total Cost:{order['total_cost']}\n")
            file.write(f"Order Date:{order['order_date']}\n")
            file.write(f"Estimated Delivery Date:{order['delivery_date']}\n")
            file.write("-----------------------------------------------------\n")

#writing skipped orders in skipped_orders list
def write_skipped(skipped_orders):
    with open("UST_Order_Processing/output/skipped_orders.txt","w") as file:
        for order in skipped_orders:
            file.write(f"OrderID:{order['order_id']}|Reason:{order['reason']}\n")
            
#main function
def process_order():
    processed_orders=[]
    skipped_orders=[]
    
    for order in orders:
        order_id=order['order_id']
        customer_name=order['customer_name']
        product=order['product']
        quantity=int(order['quantity'])
        unit_price=float(order['unit_price'])
        order_date_str=order['order_date']

        #quantity validation
        if quantity<=0 or unit_price<=0:
            skipped_orders.append({"order_id":order_id,"reason":"Invalid quantity or price"})
            log(f"Order{order_id} skipped -Invalid number format",level="WARNING")
            continue 
        
        #date validation
        valid,res=validate_date(order_date_str)
        if not valid:
            skipped_orders.append({"order_id":order_id,"reason": res})
            log(f"Order{order_id} skipped -Invalid date",level="WARNING")
            continue 
        
        
        order_date=res  
        #calculate total cost
        total_cost=calculate_total_cost(quantity, unit_price)
    
        delivery_date=calculate_delivery_date(order_date)
        #adding processed orders
        processed_orders.append({
            "order_id":order_id,
            "customer_name":customer_name,
            "product":product,
            "quantity":quantity,
            "unit_price":unit_price,
            "total_cost":total_cost,
            "order_date":order_date,
            "delivery_date":delivery_date
        })
    #write files function call
    write_processed(processed_orders)
    write_skipped(skipped_orders)
    
#calling main function
process_order()