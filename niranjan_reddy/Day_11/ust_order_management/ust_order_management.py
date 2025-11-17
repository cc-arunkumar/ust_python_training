
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


import os
import csv

# ---------------------------------------
# Class: ValidRecord
# Purpose: Validate a single row (order record)
# ---------------------------------------
class ValidRecord:
    # Predefined list of valid Indian states
    valid_state = [
        "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
        "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
        "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
        "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
        "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
        "Uttar Pradesh","Uttarakhand","West Bengal"
    ]

    def __init__(self, row):
        # Store a single CSV row as a dictionary
        self.row = row

    def validate(self):
        """
        Validate each field in the row:
        - Ensure row is not empty
        - Check customer name
        - Validate state
        - Convert quantity to integer and validate
        - Convert price to float and validate
        - Calculate total amount
        - Return cleaned/validated record OR False if errors found
        """

        # Extract fields safely (with defaults)
        name = self.row.get("customer_name", "").strip()
        state = self.row.get("state", "").strip()
        qty = self.row.get("quantity", "")
        price = self.row.get("price_per_unit", "")
        status = self.row.get("status", "").strip()

        # Check if row is entirely empty
        if not any(self.row.values()):
            self.error = "rows are empty"
            return False

        # Customer name validation
        if name == "":
            self.error = "customer name is missing"
            return False

        # Validate state name
        if state not in self.valid_state:
            self.error = f"Invalid state: {state}"
            return False

        # Validate quantity as integer > 0
        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except ValueError:
            self.error = f"Invalid quantity: {qty}"
            return False

        # Validate price as float
        try:
            price = float(price)
            # Auto-correct negative prices by taking absolute value
            if price < 0:
                price = abs(price)
        except:
            self.error = f"Invalid price_per_unit: {price}"
            return False

        # Calculate total amount
        total = qty * price
        status = status.upper()  

        # Return a validated and cleaned record
        return {
            "order_id": self.row.get("order_id", ""),
            "customer_name": name,
            "state": state,
            "product": self.row.get("product", ""),
            "quantity": qty,
            "price_per_unit": price,
            "total_amount": total,
            "status": status
        }


# ---------------------------------------
# Class: ProcessedRecord
# Purpose: Read CSV, validate rows, save valid & invalid results in separate files
# ---------------------------------------
class ProcessedRecord:
    def __init__(self, filename):
        self.filename = filename
        self.valid = []      
        self.error_data = []  

    def process(self):
        """Read CSV file and validate each row."""
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                order = ValidRecord(row)
                result = order.validate()

                if result:
                    self.valid.append(result)  
                else:
                    row["error_reason"] = order.error  
                    self.error_data.append(row)
         # Write processed results to files
        self.write_outputs() 

    def write_outputs(self):
        """Write valid and invalid rows to separate output CSV files."""

        # ------------------------
        # Write valid records
        # ------------------------
        with open("orders_processed.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","total_amount","status"
            ])
            for val in self.valid:
                writer.writerow(val.values())

        # ------------------------
        # Write invalid/skipped records
        # ------------------------
        with open("orders_skipped.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","status","error_reason"
            ])
            for i in self.error_data:
                writer.writerow([
                    i.get("order_id",""),
                    i.get("customer_name",""),
                    i.get("state",""),
                    i.get("product",""),
                    i.get("quantity",""),
                    i.get("price_per_unit"),
                    i.get("status",""),
                    i.get("error_reason")
                ])

        # Summary output
        print("Processed Rows: ", len(self.valid))
        print("Skipped Rows: ", len(self.error_data))


# ---------------------------------------
# Run script if executed directly
# ---------------------------------------
if __name__ == "__main__":
    ProcessedRecord("orders_raw.csv").process()


# Sample Output
# Processed Rows:  89
# Skipped Rows:  61
 