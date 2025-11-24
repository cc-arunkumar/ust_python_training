import math
import os
from datetime import datetime, timedelta, date
import csv

base_dir = "ust_python_training/prudhvi_rajeev_kumar/day 11/UST_Order_Processing"
input_file = os.path.join(base_dir, "input")
output_file = os.path.join(base_dir, "output")
log_dir = os.path.join(base_dir, "logs")

# If folders not present making the new folders.
for folder in [input_file, output_file, log_dir]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Creating the files inside the Directory.
ORDERS_FILE = os.path.join(input_file, "orders.csv")
PROCESSED_FILE = os.path.join(output_file, "processed_orders.txt")
SKIPPED_FILE = os.path.join(output_file, "skipped_orders.txt")
LOG_FILE = os.path.join(log_dir, "execution_log.txt")

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    with open(LOG_FILE, "a") as logf:
        logf.write(f"{timestamp} {level}: {message}\n")
        
#Creating a function to calculate the delivery date except for sundays. 
def calculate_delivery(order_date):
    delivery_date =  order_date + timedelta(days=7)
    while delivery_date.weekday() == 6:
          delivery_date += timedelta(days=1)
    return delivery_date

#Process orders function where it reads the file from csv file and performs the operations.
def process_orders():
    open(PROCESSED_FILE, 'w').close()
    open(SKIPPED_FILE, 'w').close()
    
    with open(ORDERS_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            order_id = row["order_id"]
            customer = row["customer_name"]
            product = row["product"]
            
            try:
                quantity = int(row['quantity'])
                unit_price = int(row['unit_price'])
            #It will throw ValueError when the data is not converted to integer.
            except ValueError:
                with open(SKIPPED_FILE, 'a') as sf:
                    sf.write(f"OrderID : {order_id}, Reason : Invalid Quantity or Price\n")
                log(f"OrderID {order_id} skipped because of Invalid Quantity or Invalid Price.")
                continue
            #If the quantity is less than 0 then also skip.
            if quantity <= 0:
                with open(SKIPPED_FILE, "a") as sf:
                    sf.write(f"OrderID: {order_id}  Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                continue
            #If unit price is less than 0 then also getting skipped.
            if unit_price <= 0:
                with open(SKIPPED_FILE, "a") as sf:
                    sf.write(f"OrderID: {order_id}  Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price")
                continue
            
            #If there is an error in date format then also it will throw value error and get skipped.
            try:
                order_date = datetime.strptime(row["order_date"], "%Y-%m-%d").date()
            except ValueError:
                with open(SKIPPED_FILE, "a") as sf:
                    sf.write(f"OrderID: {order_id}  Reason: Invalid date\n")
                log(f"Order {order_id} skipped - Invalid date", "WARNING")
                continue
            
            #If order date is greater than today's date then also get skipped.
            if order_date > date.today():
                with open(SKIPPED_FILE, "a") as sf:
                    sf.write(f"OrderID: {order_id}  Reason: Order date is after today.\n")
                log(f"Order {order_id} skipped - Future date")
                continue
            
            log(f"Processing Order of {order_id}")
            #Calculating the total Cost and delivery_date.
            total_cost = math.ceil(quantity * unit_price)
            delivery_date = calculate_delivery(order_date)
            
            with open(PROCESSED_FILE, 'a') as out:
                out.write(
                    f"OrderID: {order_id}\n"
                    f"Customer: {customer}\n"
                    f"Product: {product}\n"
                    f"Quantity: {quantity}\n"
                    f"Unit Price: {unit_price}\n"
                    f"Total Cost: {total_cost}\n"
                    f"Order Date: {order_date}\n"
                    f"Estimated Delivery: {delivery_date}\n"
                    + "-" * 50 + "\n"
                )
                
            log(f"Order {order_id} processed successfully")
    log("Finished Order Processing")
    
if __name__ == "__main__":
    process_orders()
            