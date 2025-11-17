import os
import csv
import datetime
import logging
from datetime import date
from datetime import datetime

LOG_FILE = os.path.join(r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day11\task2\UST_Order_Processing\logs","execution_log.txt")
ProcessedFile = os.path.join(r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day11\task2\UST_Order_Processing\output","processed_orders.txt")
SkippedFile = os.path.join(r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day11\task2\UST_Order_Processing\output","skipped_orders.txt")
Input = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day11\task2\UST_Order_Processing\input\orders.csv"

folders = ["UST_Order_Processing/input",
           "UST_Order_Processing/output",
           "UST_Order_Processing/logs"
           ]

for i in folders:
    if not os.path.exists(i):
        os.makedirs(i)

# Logs messages to a log file with a timestamp.
def log(message, level="INFO"):
    timestamp = date.today().strftime("%Y-%m-%d")  
    entry = f"[{timestamp} {message}]\n"  # Format the log message
    with open(LOG_FILE, 'a') as logf:  # Open the log file in append mode
        logf.write(entry)  # Write the log entry to the file

# Represents an order record and performs validation on the data.
class OrderRecord:
    def __init__(self, order_id, customer_name, product, quantity, unit_price, order_date):
        # Initializes the order record with provided data
        self.order_id = order_id
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.order_date = order_date
        self.error_reason = "" 

    # Validates the fields of the order record.
    def validate(self):
        # Validate customer name is not empty
        if self.customer_name.strip() == "":
            self.error_reason = "Customer Name Missing"
            log(f"order {self.order_id} skipped - Invalid Name")
            return False
        
        # Validate quantity is a positive integer
        try:
            self.quantity = int(self.quantity)
            if self.quantity <= 0:
                self.error_reason = "value must be a positive integer"
                log(f"order {self.order_id} skipped - Not a positive value")
                return False
        except ValueError:
            self.error_reason = "Quantity is not a valid integer"
            log(f"order {self.order_id} skipped - Value Error")
            return False
        
        # Validate unit price is a valid positive float
        try:
            self.unit_price = float(self.unit_price)
            if self.unit_price <= 0:
                self.unit_price = abs(self.unit_price)  # Ensure price is positive
        except ValueError:
            self.error_reason = "Price is not a valid number"
            log(f"order {self.order_id} skipped - Invalid number")
            return False
        
        # Validate order date is in the correct format and not in the future
        try:
            self.order_date = datetime.strptime(self.order_date, "%Y-%m-%d").date()
            today = datetime.today().date()
            if self.order_date > today:
                self.error_reason = "order date is in future"
                log(f"order {self.order_id} skipped - Order date in future")
                return False
        except ValueError:
            self.error_reason = "order date value error"
            log(f"order {self.order_id} skipped - Date value error")
            return False
        
        log(f"order {self.order_id} validation successful")
        return True  # Return True if all validations pass


# Manages the processing of orders, including reading, validating, and writing them.
class OrderProcessor:
    def __init__(self, input_file):
        # Initializes the processor with an input CSV file
        self.input_file = input_file
        self.valid_orders = []  # List to store valid orders
        self.invalid_orders = []  # List to store invalid orders
        log(f"OrderProcessor initialized with input file: {input_file}")

    # Reads orders from the input file and validates them.
    def read_orders(self):
        try:
            with open(self.input_file, 'r') as file:  # Open the input file
                reader = csv.DictReader(file)  
                for row in reader:
                    # Create an OrderRecord object for each row
                    order = OrderRecord(
                        row['order_id'], row['customer_name'], row['product'], row['quantity'], 
                        row['unit_price'], row['order_date']
                    )
                    if order.validate():  # If the order is valid, add it to valid orders list
                        self.valid_orders.append(order)
                    else:
                        row['error_reason'] = order.error_reason  # Add error reason for invalid orders
                        self.invalid_orders.append(row)  # Add invalid order to the list
            log(f"Finished reading orders from {self.input_file}")
        except FileNotFoundError:
            log(f"Error: File {self.input_file} not found", level="ERROR")
            print("Error: File not found!")  # Handle file not found error
        except KeyError as e:
            log(f"Error: Missing column {e} in the CSV file.", level="ERROR")
            print(f"Error: Missing column {e} in the CSV file.")  


    # Writes the valid orders to a new file.
    def write_valid_orders(self):
        log(f"Writing valid orders to {ProcessedFile}")
        with open(ProcessedFile, 'w', newline='') as file:  # Open the processed file in write mode
            fieldnames = ['order_id', 'customer_name', 'product', 'quantity', 'unit_price', 'order_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)  # Create a CSV writer
            writer.writeheader()  # Write the header row
            for order in self.valid_orders:  # Write each valid order
                writer.writerow({
                    'order_id': order.order_id,
                    'customer_name': order.customer_name,
                    'product': order.product,
                    'quantity': order.quantity,
                    'unit_price': order.unit_price,
                    'order_date': order.order_date
                })
        log(f"Finished writing valid orders to {ProcessedFile}")

    # Writes the invalid orders (with error reasons) to a new file.
    def write_invalid_orders(self):
        log(f"Writing invalid orders to {SkippedFile}")
        with open(SkippedFile, 'w', newline='') as file:  
            fieldnames = ['order_id', 'customer_name', 'product', 'quantity', 'unit_price', 'order_date', 'error_reason']
            writer = csv.DictWriter(file, fieldnames=fieldnames)  
            writer.writeheader() 
            for order in self.invalid_orders:  # Write each invalid order
                writer.writerow(order)
        log(f"Finished writing invalid orders to {SkippedFile}")

    # Process the orders: read, validate, and write valid/invalid orders.
    def process_orders(self):
        self.read_orders()  # Read orders and validate them
        self.write_valid_orders()  # Write valid orders to file
        self.write_invalid_orders()  # Write invalid orders to file

# Main function to run the order processing.
def main():
    process = OrderProcessor(Input)  
    process.process_orders()  # Process the orders (validate and write to files)
    print("Order processing complete.")  # Print a completion message after processing

if __name__ == '__main__':
    main()  # Call the main function to start processing orders
