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
 
class OrderRecord:
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
        # Store the raw CSV row for validation
        self.row = row
        self.error = ""  # To store validation error message
 
    def validate(self):
        """Validate the order record and apply transformations."""

        # Extract and clean fields
        name = self.row.get("customer_name", "").strip()
        state = self.row.get("state", "").strip()
        qty = self.row.get("quantity", "")
        price = self.row.get("price_per_unit", "")
        status = self.row.get("status", "").strip()
 
        # Rule 7: Skip completely empty rows
        if not any(self.row.values()):
            self.error = "Empty row"
            return False
 
        # Rule 3: Customer name must not be empty
        if name == "":
            self.error = "Missing customer_name"
            return False
       
        # Rule 4: State must be valid
        if state not in self.valid_state:
            self.error = f"Invalid state: {state}"
            return False
 
        # Rule 1: Quantity must be a positive integer
        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except:
            self.error = f"Invalid quantity: {qty}"
            return False
 
        # Rule 2: price must be a positive number (negative → absolute)
        try:
            price = float(price)
            if price < 0:
                price = abs(price)
        except:
            self.error = f"Invalid price_per_unit: {price}"
            return False
       
        # Rule 5: Compute total amount
        total = qty * price

        # Rule 6: Normalize status to uppercase
        status = status.upper()
 
        # If all validations pass → return cleaned/processed record
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
   
class OrderProcessor:
    def __init__(self, filename):
        # Input CSV file
        self.filename = filename
        # Lists to store valid and invalid processed data
        self.valid = []
        self.invalid = []
 
    def process(self):
        """Read, validate, and classify each order record."""
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            # Loop through each row in CSV
            for row in reader:
                order = OrderRecord(row)
                result = order.validate()

                # If valid, add to valid list
                if result:
                    self.valid.append(result)
                else:
                    # If invalid, add error reason and store in invalid list
                    row["error_reason"] = order.error
                    self.invalid.append(row)

        # After processing, write output CSV files
        self.write_outputs()
 
    def write_outputs(self):
        """Write valid and invalid orders to separate CSV files."""

        # ------------------------- #
        #   Write Valid Orders CSV
        # ------------------------- #
        with open("orders_processed.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Header row for processed CSV
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","total_amount","status"
            ])

            # Write clean records
            for v in self.valid:
                writer.writerow(v.values())
 
        # ------------------------- #
        #   Write Skipped Orders CSV
        # ------------------------- #
        with open("orders_skipped.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # Header row for skipped CSV
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","status","error_reason"
            ])

            # Write invalid records with error messages
            for i in self.invalid:
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
               
        # Summary
        print("Processing Completed")
        print("Valid Orders: ", len(self.valid))
        print("Skipped Orders: ", len(self.invalid))
        print("Processing Completed successfully!")

# Entry point
if __name__ == "__main__":
    OrderProcessor("orders_raw.csv").process()



# Sample Input — orders_raw.csv
# order_id,customer_name,state,product,quantity,price_per_unit,status
# 1001,Asha Verma,Uttar Pradesh,Mobile Phone,1,15000,shipped
# 1002,Imran Shaikh,Maharashtra,Laptop Bag,two,800,pending
# 1003,Lobsang Tsering,Ladakh,Mouse,3,-350,delivered
# 1004,Priya Singh,Karnataka,Keyboard,0,700,cancelled
# 1005,R. Kumar,Tamil Nadu,Tablet,2,,shipped


# Sample Output — orders_processed.csv

# order_id,customer_name,state,product,quantity,price_per_unit,total_amount,status
# 1001,Asha Verma,Uttar Pradesh,Mobile Phone,1,15000.0,15000.0,SHIPPED
# 1003,Lobsang Tsering,Ladakh,Mouse,3,350.0,1050.0,DELIVERED