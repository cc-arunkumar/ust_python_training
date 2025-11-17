import os
import math
import csv
from datetime import datetime, date, timedelta

# File structure
# UST_Order_Processing/
#  input/
#  orders.csv ← you will place sample file here manually
#  output/
#  processed_orders.txt
#  skipped_orders.txt
#  logs/
#  execution_log.txt

base_folder = "UST_Order_Processing"
input_folder = os.path.join(base_folder, "input")
output_folder = os.path.join(base_folder, "output")
logs_folder = os.path.join(base_folder, "logs")

input_file = os.path.join(input_folder, "orders.csv")
processed_orders_file = os.path.join(output_folder, "processed_orders.txt")
skipped_orders_file = os.path.join(output_folder, "skipped_orders.txt")
execution_log_file = os.path.join(logs_folder, "execution_log.txt")



def create_folders():
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(logs_folder, exist_ok=True)

    if not os.path.exists(execution_log_file):
        with open(execution_log_file, 'w') as log_file:
            log_file.write("")  
            
    print(f"Log file located at: {execution_log_file}")



def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(execution_log_file, "a") as log_file:
        log_file.write(f"[{timestamp}] {level}: {message}\n")


def validate_date(order_date):
    try:
        order_date = datetime.strptime(order_date, "%Y-%m-%d").date()
        if order_date > date.today():
            return False, "Order date is in the future"
        return True, order_date
    except ValueError:
        return False, "Invalid date"


def calculate_delivery_date(order_date):
    delivery_date = order_date + timedelta(days=5)
    while delivery_date.weekday() == 6:  
        delivery_date += timedelta(days=1)
    return delivery_date



def process_orders():
    processed_orders = []
    skipped_orders = []

    try:
        with open(input_file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                order_id = row["order_id"]
                customer_name = row["customer_name"]
                product = row["product"]
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])
                order_date = row["order_date"]

            
                if quantity <= 0:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid quantity")
                    log_message(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                    continue

          
                if unit_price <= 0:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid unit price")
                    log_message(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                    continue

              
                is_valid_date, date_or_error = validate_date(order_date)
                if not is_valid_date:
                    skipped_orders.append(f"OrderID: {order_id} | Reason: {date_or_error}")
                    log_message(f"Order {order_id} skipped - {date_or_error}", "WARNING")
                    continue

        
                total_cost = math.ceil(quantity * unit_price)


                delivery_date = calculate_delivery_date(date_or_error)

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

                log_message(f"Order {order_id} processed successfully")

    except Exception as e:
        print(f"Error reading the CSV file: {e}")

    with open(processed_orders_file, "w") as processed_file:
        processed_file.write("\n".join(processed_orders))

    with open(skipped_orders_file, "w") as skipped_file:
        skipped_file.write("\n".join(skipped_orders))

    log_message("Order processing completed")


def main():
    create_folders()  
    log_message("Started Order Processing")
    process_orders()  


if __name__ == "__main__":
    main()
