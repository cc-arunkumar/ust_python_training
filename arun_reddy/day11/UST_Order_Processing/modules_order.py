import os
import csv
import datetime
import math

# Function to log execution steps with timestamp, message type, and details
def execution(msg_t, t):
    """
    Log execution events to execution.txt file
    msg_t: Type of message (INFO, WARNING, ERROR)
    t: Details/description of the event
    """
    today = datetime.date.today()
    with open("execution.txt", "a", newline="") as file:
        file.writelines(f"{today} {msg_t} {t} \n")

# Set the output folder path where processed and skipped orders will be saved
targetpath = "D:/ust_python_training/arun_reddy/day11/UST_Order_Processing/output"

# Create output folder if it doesn't exist
if not os.path.exists(targetpath):
    os.mkdir(targetpath)
    print("folder created successfully")
else:
    print("folder already exists")
    
execution("INFO", "completed")
    

# Path for file to store successfully processed orders
filepath = "D:/ust_python_training/arun_reddy/day11/UST_Order_Processing/output/processed_orders.txt"

# Create processed orders file if it doesn't exist
if not os.path.exists(filepath):
    with open(filepath, "w") as file:
        pass
    print("File created succssfully")
else:
    print("File already exists")

# Path for file to store orders that failed validation (skipped orders)
filepath2 = "D:/ust_python_training/arun_reddy/day11/UST_Order_Processing/output/skipped_orders.txt"

# Create skipped orders file if it doesn't exist
if not os.path.exists(filepath2):
    with open(filepath2, "w") as file:
        pass
    print("File created successfulley")
else:
    print("file not creatd")


# Lists to store processed and skipped orders after validation
processedlist = []  # Orders that passed all validations
skippedlist = []    # Orders that failed validation

# Function to validate and process each order row
def validate_row(item):
    """
    Validates each order and separates them into processed or skipped lists
    Checks: quantity > 0, unit_price > 0, order_date is today or in past
    If valid: calculates total cost and sets delivery date (5 days from order date)
    If invalid: adds to skipped list with error reason
    """
    try:
        execution("INFO", f"started order{item['order_id']}")
        
        # Validate quantity is positive
        for row in item:
            if row == "quantity" and int(item[row]) <= 0:
                msg = 'Invalid Quantity'
                raise Exception
                
            # Validate unit price is positive
            if int(item["unit_price"]) <= 0:
                msg = 'Invalid Unit_price'
                raise Exception
            
            # Validate order date is not in the future
            future = datetime.date.strptime(item["order_date"], "%Y-%m-%d")
            if future > datetime.date.today():
                raise Exception("Invalid date and time")
                
    except Exception as e:
        # If validation fails, add order to skipped list with error reason
        skippedlist.append(item)
        item["reason"] = e
        execution("WARNING", e)
    else:
        # If validation passes, calculate total cost and set delivery date
        item["totalcost"] = math.ceil(int(item["quantity"]) * int(item["unit_price"]))
        future = future + datetime.timedelta(5)  # Add 5 days for delivery
        
        # If delivery date falls on Sunday (weekday 6), keep it as is
        if future.weekday() == 6:
            item["delivery_date"] = future
        
        execution("INFO", f"ordered successfully {item['order_id']}")
        processedlist.append(item)
    
    
# Read orders from input CSV file and validate each one
with open("orders.csv", "r") as file:
    content = csv.DictReader(file)
    for data in content:
        validate_row(data)

# Show total number of successfully processed orders
print(len(processedlist))


# Write successfully processed orders to output file
with open("processed_orders.txt", "w", newline='') as file:
    headers = ["order_id", "customer_name", "product", "quantity", "unit_price", "order_date", "total_cost", "delivery_date"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    # Write each processed order row to the file
    for item in processedlist:
        writer.writerow({h: item.get(h, "") for h in headers}) 

# Write skipped orders (failed validation) to output file with reason
with open("skipped_orders.txt", "w", newline='') as file:
    headers = ["order_id", "customer_name", "product", "quantity", "unit_price", "order_date", "total_cost", "delivery_date", "reason"]
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    # Write each skipped order row with error reason to the file
    for item in skippedlist:
        writer.writerow({h: item.get(h, "") for h in headers})

# Log completion of order processing
execution("INFO", "Finished Order Processing")

    
