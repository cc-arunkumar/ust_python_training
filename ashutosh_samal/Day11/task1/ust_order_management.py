import csv  # Import the CSV module for reading and writing CSV files

class OrderRecord:
    # Constructor to initialize the OrderRecord object with order details
    def __init__(self, order_id, customer_name, state, product, quantity, price_per_unit, status):
        self.order_id = order_id  
        self.customer_name = customer_name  
        self.state = state  
        self.product = product  
        self.quantity = quantity  
        self.price_per_unit = price_per_unit  
        self.status = status 
        self.error_reason = ""  
    
    # Function to validate the order data (checks for empty customer name, non-positive quantity, invalid state, etc.)
    def validate(self):
        # Check if the customer name is empty or contains only spaces
        if self.customer_name.strip() == "":
            self.error_reason = "Customer Name Missing"
            return False
        
        # Check if the quantity is a valid positive integer
        try:
            self.quantity = int(self.quantity)
            if self.quantity <= 0:
                self.error_reason = "value must be a positive integer"
                return False
        except ValueError:
            self.error_reason = "Quantity is not a valid integer"
            return False
        
        # Check if the price per unit is a valid positive float
        try:
            self.price_per_unit = float(self.price_per_unit)
            if self.price_per_unit <= 0:
                self.price_per_unit = abs(self.price_per_unit)  
        except ValueError:
            self.error_reason = "Price is not a valid number"
            return False
        
        # Define the list of valid states
        valid_state = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
            "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
            "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", 
            "West Bengal", "Ladakh"]
        
        # Check if the state is valid
        if self.state not in valid_state:
            self.error_reason = "Invalid state"
            return False

        return True  # Return True if all validations pass
    
    # Function to compute the total amount of the order (quantity * price_per_unit)
    def compute_total_amount(self):
        return self.quantity * self.price_per_unit
    
    # Function to transform the order status to uppercase
    def transform_status(self):
        self.status = self.status.upper()


class OrderProcessor:
    # Constructor to initialize the OrderProcessor object with the input file path
    def __init__(self, input_file):
        self.input_file = input_file  
        self.valid_orders = []  
        self.invalid_orders = []  
    
    # Function to read orders from the input CSV file and validate each order
    def read_orders(self):
        try:
            # Open the CSV file for reading
            with open(self.input_file, 'r') as file:
                reader = csv.DictReader(file)  
                # Iterate through each row (order) in the file
                for row in reader:
                    # Create an OrderRecord object for each row
                    order = OrderRecord(
                        row['order_id'], row['customer_name'], row['state'],
                        row['product'], row['quantity'], row['price_per_unit'], row['status']
                    )
                    # Validate the order
                    if order.validate():
                        order.total_amount = order.compute_total_amount()  
                        order.transform_status()  
                        self.valid_orders.append(order)  # Add valid order to the list
                    else:
                        row['error_reason'] = order.error_reason  # Add the error reason to the row for invalid orders
                        self.invalid_orders.append(row)  # Add invalid order to the list
        except FileNotFoundError:
            print("Error: File not found!")  # Error handling if the file is not found
        except KeyError as e:
            print(f"Error: Missing column {e} in the CSV file.")  # Error handling if a column is missing
    
    # Function to write valid orders to an output CSV file
    def write_valid_orders(self, output_file):
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'total_amount', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)  # Create a CSV DictWriter object
            writer.writeheader() 
            for order in self.valid_orders:
                writer.writerow({
                    'order_id': order.order_id,
                    'customer_name': order.customer_name,
                    'state': order.state,
                    'product': order.product,
                    'quantity': order.quantity,
                    'price_per_unit': order.price_per_unit,
                    'total_amount': order.total_amount,
                    'status': order.status
                })
    
    # Function to write invalid orders to an output CSV file
    def write_invalid_orders(self, output_file):
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'status', 'error_reason']
            writer = csv.DictWriter(file, fieldnames=fieldnames)  # Create a CSV DictWriter object
            writer.writeheader()  
            for order in self.invalid_orders:
                writer.writerow(order)
    
    # Function to process orders: read, validate, and save valid and invalid orders
    def process_orders(self):
        self.read_orders()  
        self.write_valid_orders('orders_processed.csv')  
        self.write_invalid_orders('orders_skipped.csv')  
    
        # Print the number of processed (valid) and skipped (invalid) orders
        print(f"Number of processed (valid) orders: {len(self.valid_orders)}")
        print(f"Number of skipped (invalid) orders: {len(self.invalid_orders)}")


# Main function to run the order processing
def main():
    process = OrderProcessor('orders_raw.csv')  
    process.process_orders()  
    print("Order processing complete.")  

# Run the main function if this file is being executed directly
if __name__ == '__main__':
    main()


#Sample Execution
# Number of processed (valid) orders: 91
# Number of skipped (invalid) orders: 59
# Order processing complete.