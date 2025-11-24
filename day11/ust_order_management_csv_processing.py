# Order Processing Script:

# Purpose:

# Reads orders from a raw CSV file, validates the data, and generates two output files:
# orders_processed.csv: Contains valid order records with calculated total amounts and standardized statuses.
# orders_skipped.csv: Contains invalid orders with an error reason for each failure.

# Validation checks performed:

# Missing Fields: Ensures no required fields are empty (order ID, customer name, state, product, quantity, price per unit, and status).
# Quantity: Checks that the quantity is a positive integer.
# Price per Unit: Verifies that the price per unit is a valid, non-negative number.
# State: Confirms that the state is one of the valid predefined states.
# Customer Name: Ensures that the customer name is non-empty and properly formatted.

# Processing Outcome:

# Processed Orders: Valid records are added to the orders_processed.csv file.
# Skipped Orders: Invalid records are added to the orders_skipped.csv file with an error reason.

# Output:

# Displays the count of processed and skipped orders in the terminal.


import csv

class OrderRecord:
    # A list of valid states where the orders can be processed
    validstates = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
        "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
        "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
        "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal"
    ]

    def __init__(self, order_id, customer_name, state, product, quantity, price_per_unit, status):
        # Initialize the order record with values
        self.order_id = order_id
        self.customer_name = customer_name
        self.state = state
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.status = status

    def validate(self):
        # Check if any required field is missing
        if self.order_id.strip() == "" or self.customer_name.strip() == "" or self.state.strip() == "" or \
           self.product.strip() == "" or self.quantity.strip() == "" or self.price_per_unit.strip() == "" or \
           self.status.strip() == "":
            self.reason = "Missing Values"
            return False
        
        # Validate quantity: it should be a positive integer
        try:
            self.quantity = int(self.quantity)
            if self.quantity <= 0:
                raise Exception
        except:
            self.reason = "Invalid Quantity"
            return False
        
        # Validate price per unit: it should be a valid integer
        try:
            self.price_per_unit = int(self.price_per_unit)
        except:
            self.reason = "Invalid Price per Unit"
            return False
        
        # If price per unit is negative, make it positive
        if self.price_per_unit < 0:
            self.price_per_unit = abs(self.price_per_unit)

        # Validate customer name
        self.customer_name = self.customer_name.strip()
        if self.customer_name == "":
            self.reason = "Invalid Customer Name"
            return False
        
        # Validate state: it should be in the list of valid states
        if self.state not in OrderRecord.validstates:
            self.reason = "Invalid State"
            return False
        
        # Calculate total amount for the order
        self.total_amount = self.quantity * self.price_per_unit
        
        # Standardize the status to uppercase
        self.status = self.status.strip().upper()
        
        return True

class OrderProcessor:
    processeddata = []  # List to store successfully processed data
    skippeddata = []    # List to store skipped (failed validation) data

    def reading(self):
        # Open and read the raw CSV file containing orders
        with open("orders_raw.csv", "r") as file:
            dictreader = csv.DictReader(file)  # Reading CSV as a dictionary
            for row in dictreader:
                # Create an OrderRecord object for each row
                order = OrderRecord(row["order_id"], row["customer_name"], row["state"], row["product"], 
                                    row["quantity"], row["price_per_unit"], row["status"])
                # Validate the order and process accordingly
                if order.validate():
                    # Prepare the valid order data for processing
                    record = {
                        "order_id": order.order_id,
                        "customer_name": order.customer_name,
                        "state": order.state,
                        "product": order.product,
                        "quantity": order.quantity,
                        "price_per_unit": order.price_per_unit,
                        "total_amount": order.total_amount,
                        "status": order.status
                    }
                    OrderProcessor.processeddata.append(record)  # Add to processed data
                else:
                    # Prepare the invalid order data with error reason
                    record = {
                        "order_id": order.order_id,
                        "customer_name": order.customer_name,
                        "state": order.state,
                        "product": order.product,
                        "quantity": order.quantity,
                        "price_per_unit": order.price_per_unit,
                        "status": order.status,
                        "error_reason": order.reason
                    }
                    OrderProcessor.skippeddata.append(record)  # Add to skipped data
        
        # Write processed data to 'orders_processed.csv'
        with open("orders_processed.csv", "w", newline="") as file:
            headers = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "total_amount", "status"]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(OrderProcessor.processeddata)  # Write processed orders
        
        # Write skipped data (with errors) to 'orders_skipped.csv'
        with open("orders_skipped.csv", "w", newline="") as file:
            headers = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status", "error_reason"]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(OrderProcessor.skippeddata)  # Write skipped orders

        # Output status
        print("Completed all operations.")
        print("*******************************************")
        print("Skipped: ", len(OrderProcessor.skippeddata))  # Number of skipped (invalid) orders
        print("Processed: ", len(OrderProcessor.processeddata))  # Number of successfully processed orders

# Initialize and call the order processor
x = OrderProcessor()
x.reading()



# Completed all operations.
# *******************************************

# Skipped:  61  
# Processed:  89