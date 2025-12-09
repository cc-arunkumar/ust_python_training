
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
# ❌ Skip order if:
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
# �� processed_orders.txt format
# OrderID: 101
# Customer: Asha Nair
# Product: Laptop
# Quantity: 2
# Unit Price: 45000
# Total Cost: 90000
# Order Date: 2025-01-10
# Estimated Delivery: 2025-01-15
# --------------------------------------------------
# �� skipped_orders.txt format
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
# Modules Task 5

import math
import csv
from datetime import date,timedelta,datetime
import os
logs=[]

class Order:
    def __init__(self,order_id,customer_name,product,quantity,unit_price,order_date):
        self.order_id=order_id
        self.customer_name=customer_name
        self.product=product
        self.quantity=quantity
        self.unit_price=unit_price
        self.order_date=order_date
  
    def validate(self):
        
        #Checking if the given date format is correct or not 
        try:
            self.order_date=datetime.strptime(self.order_date, "%Y-%m-%d")
        except Exception:
            self.reason="Invalid date"
            return False
        
        #check if order date is in future
        if datetime.today()<self.order_date:
            self.reason="Order date in the future"
            return False
        
        #checking the quantity is valid
        self.quantity=int(self.quantity)
        if self.quantity<=0:
            self.reason="Invalid quantity"
            return False
        
        #checking the price is valid
        self.unit_price=int(self.unit_price)
        if self.unit_price<=0:
            self.reason="Invalid unit price"
            return False
        
        #calculating the total cost
        self.total_cost=math.ceil(self.quantity*self.unit_price)
        #calculating the estimated date
        self.delivery_date=self.order_date+timedelta(days=5)
        #chack if the delivery date is sunday if sunday add one more day
        if self.delivery_date.weekday()==6:
            self.delivery_date+=timedelta(days=1)
        
        return True

def writelogs(str):
    logs.append(str)

writelogs(f"[{date.today()}] INFO: Started Order Processing")
 
#creating the processed data file
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/output/processed_orders.txt'):
    os.mkdir(os.path.join('UST_Order_Processing','output'))
    with open(os.getcwd()+'/UST_Order_Processing/output/processed_orders.txt','w') as file:
        pass

#creating the skipped data file
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/output/skipped_orders.txt'):
    with open(os.getcwd()+'/UST_Order_Processing/output/skipped_orders.txt','w') as file:
        pass

#creating the logs file
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/logs/execution_log.txt'):
    os.mkdir(os.path.join('UST_Order_Processing','logs'))
    with open(os.getcwd()+'/UST_Order_Processing/logs/execution_log.txt','w') as file:
        pass

writelogs(f"[{date.today()}] INFO: Folder check completed")

processed=[]
skipped=[]

#Reading the file orders
with open(os.getcwd()+"/UST_Order_Processing/input/orders.csv","r") as file:
    data=csv.DictReader(file)
    headers=data.fieldnames
    for row in data:
        writelogs(f"[{date.today()}] INFO: Processing order {row["order_id"]}")
        order=Order(row["order_id"],row["customer_name"],row["product"],row["quantity"],row["unit_price"],row["order_date"])
        if order.validate():
           
            record=[order.order_id,order.customer_name,order.product,order.quantity,order.unit_price,order.total_cost,order.order_date,order.delivery_date] 
            processed.append(record)       
            writelogs(f"[{date.today()}] INFO: Order {order.order_id} processed successfully")
        else:
            # record={
            #     "order_id":order.order_id,
            #     "reason":order.reason
            # }
            record=[order.order_id,order.reason]
            skipped.append(record)
            writelogs(f"[{date.today()}] WARNING: Order {order.order_id} skipped -{order.reason}")

writelogs(f"[{date.today()}] INFO: Finished Order Processing")
#To write into the processed file
with open(os.getcwd()+"/UST_Order_Processing/output/processed_orders.txt","w",newline="") as file:
    for row in processed:
        file.write(f"OrderID: {row[0]} \n CustCustomer:{row[1]}\n Product: {row[2]} \n Quantity: {row[3]} \n Unit Price: {row[4]} \n Total Cost: {row[5]} \n Order Date: {row[6]} \n Estimated Delivery:{row[7]} \n ------------------------------- \n")

#To write the data into a skipped file
with open(os.getcwd()+"/UST_Order_Processing/output/skipped_orders.txt","w",newline="") as file:
    for row in skipped:
        file.write(f"OrderID: {row[0]}|Reason :{row[1]} \n")

#To write the logs
with open(os.getcwd()+"/UST_Order_Processing/logs/execution_log.txt","w",newline="") as file:
    for row in logs:
        file.write(f"{row}\n")
        