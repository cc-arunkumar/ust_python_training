import os
import math
import csv
from datetime import datetime, date, timedelta

# File structure
# UST_Order_Processing/
#  input/
#    orders.csv ← You will place the sample file here manually
#  output/
#    processed_orders.txt ← Will contain the processed orders
#    skipped_orders.txt ← Will contain skipped orders with reasons
#  logs/
#    execution_log.txt ← Will log the execution details

base_folder = "UST_Order_Processing"
input_folder = os.path.join(base_folder, "input")
output_folder = os.path.join(base_folder, "output")
logs_folder = os.path.join(base_folder, "logs")

input_file = os.path.join(input_folder, "orders.csv")
processed_orders_file = os.path.join(output_folder, "processed_orders.txt")
skipped_orders_file = os.path.join(output_folder, "skipped_orders.txt")
execution_log_file = os.path.join(logs_folder, "execution_log.txt")

# Function to create necessary directories if they don't exist
def create_folders():
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(logs_folder, exist_ok=True)

    # Create an empty log file if it doesn't exist
    if not os.path.exists(execution_log_file):
        with open(execution_log_file, 'w') as log_file:
            log_file.write("")  # Initialize log file
            
    print(f"Log file located at: {execution_log_file}")

# Function to log messages with timestamp and log level
def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(execution_log_file, "a") as log_file:
        log_file.write(f"[{timestamp}] {level}: {message}\n")

# Function to validate the order date (checks if the date is valid and not in the future)
def validate_date(order_date):
    try:
        order_date = datetime.strptime(order_date, "%Y-%m-%d").date()
        if order_date > date.today():  # Ensure order date is not in the future
            return False, "Order date is in the future"
        return True, order_date
    except ValueError:
        return False, "Invalid date"

# Function to calculate the delivery date (adds 5 days and skips weekends)
def calculate_delivery_date(order_date):
    delivery_date = order_date + timedelta(days=5)
    while delivery_date.weekday() == 6:  # Skip weekends (Sunday)
        delivery_date += timedelta(days=1)
    return delivery_date

# Main function to process the orders from the CSV file
def process_orders():
    processed_orders = []  # List to hold successfully processed orders
    skipped_orders = []    # List to hold orders that were skipped

    try:
        with open(input_file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)  # Reading the CSV file as a dictionary
            for row in reader:
                order_id = row["order_id"]
                customer_name = row["customer_name"]
                product = row["product"]
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
                order_date = row["order_date"]

                # Validate quantity: must be a positive integer
                if quantity <= 0:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid quantity")
                    log_message(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                    continue

                # Validate unit price: must be a positive number
                if unit_price <= 0:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid unit price")
                    log_message(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                    continue

                # Validate order date
                is_valid_date, date_or_error = validate_date(order_date)
                if not is_valid_date:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: {date_or_error}")
                    log_message(f"Order {order_id} skipped - {date_or_error}", "WARNING")
                    continue

                # Calculate the total cost (rounded up to the nearest integer)
                total_cost = math.ceil(quantity * unit_price)

                # Calculate the delivery date based on order date
                delivery_date = calculate_delivery_date(date_or_error)

                # Prepare the processed order details for output
                processed_orders.append(f"""
OrderID: {order_id}
Customer: {customer_name}
Product: {product}
Quantity: {quantity}
Unit Price: {unit_price}
Total Cost: {total_cost}
Order Date: {order_date}
Estimated Delivery: {delivery_date.strftime("%Y-%m-%d")}
--------------------------------------------------""")

                # Log that the order has been processed successfully
                log_message(f"Order {order_id} processed successfully")

    except Exception as e:
        print(f"Error reading the CSV file: {e}")

    # Write processed orders to the output file
    with open(processed_orders_file, "w") as processed_file:
        processed_file.write("\n".join(processed_orders))

    # Write skipped orders to the skipped orders file
    with open(skipped_orders_file, "w") as skipped_file:
        skipped_file.write("\n".join(skipped_orders))

    # Log that the order processing is completed
    log_message("Order processing completed")

# Main function to initiate the process
def main():
    create_folders()  # Create necessary directories
    log_message("Started Order Processing")  # Log that the processing started
    process_orders()  # Process the orders

# Run the main function if this is the main script
if __name__ == "__main__":
    main()


# output
# refer to contents of ust_order_processing_utility.py for the results