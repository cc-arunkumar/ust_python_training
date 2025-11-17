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

import csv
#initiating class
class OrderRecord:
    def __init__(self, order_id, customer_name, state, product, quantity, price_per_unit, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.state = state
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.status = status
        self.error_reason = ""
    
    #validate function
    def validate(self):
        # Validate customer_name 
        if not self.customer_name.strip():
            self.error_reason = "Customer name is missing"
            return False
       
        # Validate quantity 
        try:
            self.quantity = int(self.quantity)
            if self.quantity <= 0:
                self.error_reason = "Quantity must be a positive integer"
                return False
        except ValueError:
            self.error_reason = "Quantity is not a valid integer"
            return False
       
        # Validate price_per_unit (must be a positive number)
        try:
            self.price_per_unit = float(self.price_per_unit)
            if self.price_per_unit <= 0:
                self.price_per_unit = abs(self.price_per_unit)
        except ValueError:
            self.error_reason = "Price per unit is not a valid number"
            return False

        #defining valid states
        valid_states = ["Andhra Pradesh","Jammu & Kashmir" "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
            "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab","Rajasthan",
            "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal","Ladakh"]
        
        if self.state not in valid_states:
            self.error_reason = "Invalid state"
            return False
       
        return True
   
    #calculatinf total_amount
    def compute_total_amount(self):
        return self.quantity * self.price_per_unit
   
    def transform_status(self):
        self.status = self.status.upper()
 
 
#orderprocessor class
class OrderProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.valid_orders = []
        self.invalid_orders = []
    
    #read orders
    def read_orders(self):
        try:
            #open file
            with open(self.input_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order = OrderRecord(
                        row['order_id'], row['customer_name'], row['state'],
                        row['product'], row['quantity'], row['price_per_unit'], row['status']
                    )
                    if order.validate():
                        order.total_amount = order.compute_total_amount()
                        order.transform_status()
                        self.valid_orders.append(order)
                    else:
                        row['error_reason'] = order.error_reason
                        self.invalid_orders.append(row)
        #exceptions
        except FileNotFoundError:
            print("Error: File not found!")
        except KeyError as e:
            print(f"Error: Missing column {e} in the CSV file.")
   
    def write_valid_orders(self, output_file):
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'total_amount', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
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
    #writing in a file
    def write_invalid_orders(self, output_file):
        with open(output_file, 'w', newline='') as file:
            fieldnames = ['order_id', 'customer_name', 'state', 'product', 'quantity', 'price_per_unit', 'status', 'error_reason']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for order in self.invalid_orders:
                writer.writerow(order)
    #process orders
    def process_orders(self):
        self.read_orders()
        self.write_valid_orders('orders_processed.csv')
        self.write_invalid_orders('orders_skipped.csv')
        
    def print_processed_and_skipped(self):
    # Print the count of processed and skipped orders
        print(f"\nTotal Processed Orders: {len(self.valid_orders)}")
        print(f"Total Skipped Orders: {len(self.invalid_orders)}")
 
 
def main():
    processor = OrderProcessor(r'D:\training\ust_python_training\deva_prasath\day_11\orders_raw.csv')
    processor.process_orders()
    print("Order processing complete.")
    processor.print_processed_and_skipped()
    
 
if __name__ == '__main__':
    main()

