# UST Order Management CSV Processing
# Scenario
# UST is working with a large Indian e-commerce marketplace that handles orders from diverse customers
# across India. The operations team receives a raw CSV export each day containing order details from multiple
# states, regions, and customer backgrounds.
# Your task is to build a Python program that reads this CSV file, validates the data, applies business rules, and
# writes two separate CSV outputs:
# 1. Cleaned and processed orders
# 2. Invalid or skipped records (due to validation failures)
# This ensures high-quality order data for downstream financial and fulfillment teams.
# Objective
# Create a Python program using Object-Oriented Programming (OOP) and proper error handling to:
# 1. Read an input CSV: orders_raw.csv
# 2. Validate and transform order data
# 3. Write valid processed orders to: orders_processed.csv
# 4. Write skipped/invalid records to: orders_skipped.csv
# Business Rules
# Apply the following validations and transformations:
# 1. quantity must be a positive integer
# If non-numeric or zero, record must be skipped
# 2. price_per_unit must be positive
# If blank or non-numeric, skip the record
# If negative, convert to absolute value
# 3. customer_name must not be empty
# If missing or blank → skip the record
# 4. state must be one of the valid Indian states
# Store a predefined list of valid states
# If not part of the list → skip the record
# 5. Add a new computed column:
# total_amount = quantity * price_per_unit
# 6. Normalize status to uppercase:
# Example: shipped → SHIPPED
# 7. Skip completely empty rows automatically
# 8. All skipped/invalid records must be logged to a separate CSV file:
# orders_skipped.csv
# Include a column error_reason explaining why the record was rejected.
# Technical Requirements
# OOP
# Your solution must include at least two classes:
# 1. OrderRecord
# Represents a single order
# Performs field-level validation and transformation
# Returns whether the record is valid or not
# 2. OrderProcessor
# Reads the CSV file
# Instantiates OrderRecord objects
# Tracks valid and invalid records
# Writes processed data to orders_processed.csv
# Writes skipped/invalid data to orders_skipped.csv
# Error Handling Requirements
# Your script must gracefully handle the following:
# File not found
# Missing columns in the CSV
# Conversion errors (e.g., quantity = "two")
# Blank fields
# Day 11 2
# Invalid state names
# Errors should not stop the program. They should be logged to console and inserted into the skipped CSV file.
# Output Format
# orders_processed.csv
# | order_id | customer_name | state | product | quantity | price_per_unit | total_amount | status |
# orders_skipped.csv
# | order_id | customer_name | state | product | quantity | price_per_unit | status | error_reason |
# Deliverables
# 1. Python script: process_orders.py
# 2. Sample input: orders_raw.csv
# 3. Output files:
# orders_processed.csv
# orders_skipped.csv

import os
import csv

orders_processed = {}
orders_skipped = []
indian_states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]


#Custom Exceptions
class MissingColumnError(Exception):
    pass

class ConversionError(Exception):
    pass

class BlankFieldError(Exception):
    pass

class InvalidStateNameError(Exception):
    pass

def validate_row(item):
    try:
        for data in item:
            if item[data]!='':
                if data=="quantity" and int(item[data])<=0:
                    return False,"Invalid quantity"

                if data=="price_per_unit" and int(item[data]) :
                    pass
                
                if data=="customer_name" and len(item[data].strip())==0:
                    return False,"No customer name"
                

                if data=="state" and item[data] not in indian_states:
                    return False,"Not valid state"
            else:
                return False,"Field Missing"

    except Exception as e:
        return False,str(e)
    else:
        return True,"Success"




class OrderRecord:

    def __init__(self,order_id='',customer_name='',state='',product='',quantity='',price_per_unit='',status=''):
        self.order_id = order_id
        self.customer_name = customer_name
        self.state = state
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.status = status

    def validate(self):
        
        return validate_row(self.__dict__)
    

class OrderProcessor:
    def __init__(self, data_dir="data"):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(BASE_DIR, data_dir)
        self.orders_file = os.path.join(self.data_dir, "orders_raw.csv")
        self.orders_processed = os.path.join(self.data_dir,"orders_processed.csv")
        self.orders_skipped = os.path.join(self.data_dir,"orders_skipped.csv")

    def read_csv(self):
        with open(self.orders_file,"r") as file:
            dict_read = csv.DictReader(file)
            header = dict_read.fieldnames

            for data in dict_read:
                obj = OrderRecord(
                    data["order_id"],
                    data["customer_name"],
                    data["state"],
                    data["product"],
                    data["quantity"],
                    data["price_per_unit"],
                    data["status"]
                )
                con,stmt=obj.validate()
                if(con):
                    orders_processed[obj.order_id]={
                        "customer_name": obj.customer_name,
                        "state": obj.state,
                        "product": obj.product,
                        "quantity": obj.quantity,
                        "price_per_unit": abs(int(obj.price_per_unit)),
                        "status": obj.status.upper(),
                        "total_amount" : int(obj.quantity) * abs(int(obj.price_per_unit))
                    }
                else:
                    orders_skipped.append({
                        "order_id":obj.order_id,
                        "customer_name": obj.customer_name,
                        "state": obj.state,
                        "product": obj.product,
                        "quantity": obj.quantity,
                        "price_per_unit": obj.price_per_unit,
                        "status": obj.status,
                        "reason":stmt
                    })
    
    def write_csv(self):
        with open(self.orders_processed,"w",newline="") as file1:
            orders =[]
            header = ["order_id","customer_name", "state","product","quantity","price_per_unit","status","total_amount"]
            processed = csv.DictWriter(file1,header)
            for i in orders_processed:
                orders.append({
                    "order_id":i,
                    "customer_name": orders_processed[i]["customer_name"],
                    "state": orders_processed[i]["state"],
                    "product": orders_processed[i]["product"],
                    "quantity": orders_processed[i]["quantity"],
                    "price_per_unit": orders_processed[i]["price_per_unit"],
                    "status": orders_processed[i]["status"],
                    "total_amount" : orders_processed[i]["total_amount"]
                })
            processed.writeheader()
            processed.writerows(orders)
        
        with open(self.orders_skipped,"w",newline="") as file2:
            header = ["order_id","customer_name", "state","product","quantity","price_per_unit","status","reason"]
            skipped = csv.DictWriter(file2,header)
            skipped.writeheader()
            skipped.writerows(orders_skipped)
            



a=OrderProcessor()
a.read_csv()
a.write_csv()

print(f"Total processed orders : {len(orders_processed)}")
print(f"Total skipped orders : {len(orders_skipped)}")


            
#Output
# Total processed orders : 89
# Total skipped orders : 61
    


    