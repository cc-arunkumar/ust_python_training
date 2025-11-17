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

import csv

class MissingColumnInCsvFileError(Exception):
    pass

class BlankFieldError(Exception):
    pass

valid_state = [
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
class OrderRecord:
    def __init__(self,data):
        self.data = data
        
    def order_check(self):
        try:
                
            if self.data['quantity'].isdigit()==False or self.data['quantity'] == '0':
                self.data['error_reason'] = "quantity is not valid"
                return self.data
            
            if self.data['price_per_unit'] == "":
                raise BlankFieldError
            elif int(self.data['price_per_unit'])<0:
                self.data['price_per_unit'] = abs(int(self.data['price_per_unit']))
            
            if 'customer_name'not in self.data or self.data['customer_name'] == "":
                self.data['error_reason'] = "customer name missing"
                return self.data
             
            if self.data['state'] not in valid_state:
                self.data['error_reason'] = "state is not valid"
                return self.data
            
            self.data['total_amount'] = int(self.data['quantity'])*int(self.data['price_per_unit'])
            
            self.data['status'] = self.data['status'].upper()
            
        except MissingColumnInCsvFileError:
            self.data['error_reason'] = "some column is missing"
            return self.data
        
        except BlankFieldError:
            self.data['error_reason'] = "some datas are blank"
            return self.data
        
        except ValueError as v:
            self.data['error_reason'] = v
            return self.data
        
        except TypeError as t:
            self.data['error_reason'] = t
            return self.data
        
        else:
            return self.data
        


class OrderProcessor(OrderRecord):
    def __init__(self):
        skipped = 0
        processed = 0
        with open("orders_raw.csv","r") as file:
            all_data = csv.DictReader(file)
            
            for data in all_data:
                obj = OrderRecord(data)
                new_data = obj.order_check()
                
                if 'error_reason' in new_data:
                    with open("orders_skipped.csv","a",newline="") as file1:
                        write = csv.writer(file1)
                        write.writerow(data.values())
                        skipped += 1
                        
                else:
                    with open("orders_processed.csv","a",newline="") as file2:
                        write = csv.writer(file2)
                        write.writerow(data.values())
                        processed += 1
                        
            print("Processed data: ",processed)
            print("Skipped data: ",skipped)
                        
OrderProcessor()

# output

# Processed data:  89
# Skipped data:  61