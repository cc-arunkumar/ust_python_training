# Day 11
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
# Input CSV (orders_raw.csv) – Sample
# Columns include:
# order_id customer_name state product quantity price_per_unit status
# 1001 Asha Verma Uttar Pradesh Mobile Phone 1 15000 shipped
# 1002 Imran Shaikh Maharashtra Laptop Bag two 800 pending
# 1003 Lobsang
# Tsering
# Ladakh Mouse 3 -350 delivered
# 1004 Priya Singh Karnataka Keyboard 0 700 cancelled
# 1005 R. Kumar Tamil Nadu Tablet 2 shipped
# Business Rules
# Apply the following validations and transformations:
# 1. quantity must be a positive integer
# If non-numeric or zero, record must be skipped
# 2. price_per_unit must be positive
# If blank or non-numeric, skip the record
# Day 11 1
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
import csv


class OrderRecord:
    validstates=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
        "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    def __init__(self,order_id,customer_name,state,product,quantity,price_per_unit,status):
        self.order_id=order_id
        self.customer_name=customer_name
        self.state=state
        self.product=product
        self.quantity=quantity
        self.price_per_unit=price_per_unit
        self.status=status
        
    def validate(self):
        #Checking quantity is positive
        if self.order_id.strip()=="" or self.customer_name.strip()=="" or self.state.strip()=="" or self.product.strip()=="" or self.quantity.strip()=="" or self.price_per_unit.strip()=="" or self.status.strip()=="":
            self.reason="Missing Values"
            return False
        
        #checking for quantity
        try:
            self.quantity=int(self.quantity)
            if self.quantity<=0:
                raise Exception
        except:
            self.reason="Invalid Quantity"
            return False
        
        #checking for price_per_unit
        try:
            self.price_per_unit=int(self.price_per_unit)
        except:
            self.reason="Invalid Price per Unit"
            return False
        if self.price_per_unit<0:
                self.price_per_unit=abs(self.price_per_unit)
        
        
        #checking for customer_name
        self.customer_name=self.customer_name.strip()
        if self.customer_name=="":
            self.reason="Invalid Customer Name"
            return False
        
        #checking for valid state
        if self.state not in OrderRecord.validstates:
            self.reason="Invalid State"
            return False
        
        #calculating total amount
        self.total_amount=self.quantity*self.price_per_unit
        
        #standardizing status
        self.status=self.status.strip().upper()
        
        return True
        
        
    
class OrderProcessor:
    processeddata=[]
    skippeddata=[]
    def reading(self):
        with open("orders_raw.csv","r") as file:
            dictreader=csv.DictReader(file)
            for row in dictreader:
                order=OrderRecord(row["order_id"],row["customer_name"],row["state"],row["product"],row["quantity"],row["price_per_unit"],row["status"])
                if order.validate(): 
                    record={
                        "order_id":order.order_id,
                        "customer_name":order.customer_name,
                        "state":order.state,
                        "product":order.product,
                        "quantity":order.quantity,
                        "price_per_unit":order.price_per_unit,
                        "total_amount":order.total_amount,
                        "status":order.status
                    }                  
                    OrderProcessor.processeddata.append(record)
                else:
                    record={
                        "order_id":order.order_id,
                        "customer_name":order.customer_name,
                        "state":order.state,
                        "product":order.product,
                        "quantity":order.quantity,
                        "price_per_unit":order.price_per_unit,
                        "status":order.status,
                        "error_reason":order.reason
                    }   
                    OrderProcessor.skippeddata.append(record)
    
        with open("orders_processed.csv","w",newline="") as file:
            headers=["order_id","customer_name","state","product","quantity","price_per_unit","total_amount","status"]
            writer=csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(OrderProcessor.processeddata)
        with open("orders_skipped.csv","w",newline="") as file:
            headers=["order_id","customer_name","state","product","quantity","price_per_unit","status","error_reason"]
            writer=csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            
            writer.writerows(OrderProcessor.skippeddata)
        print("completed all operations Processed= ",len(OrderProcessor.processeddata),"skipper= ",len(OrderProcessor.skippeddata))
            
x=OrderProcessor()
x.reading()