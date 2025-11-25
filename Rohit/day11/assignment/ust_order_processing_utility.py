import csv          # For reading and writing CSV files
import math         # For mathematical operations (ceil used here)
import os           # For file and folder path operations
from datetime import datetime, date, timedelta   # For handling dates

# Base directory where input, output, and log folders are located
BASE_DIR = r"C:\Users\Administrator\Desktop\ust_python_training\rohit\day11\assignment"

# Define subdirectories for input, output, and logs
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Define file paths for orders, processed results, skipped results, and logs
ORDERS_FILE = os.path.join(BASE_DIR, "order.csv")   # Input orders file
PROCESSED_FILE = os.path.join(OUTPUT_DIR, "processed_orders.txt")  # Output for processed orders
SKIPPED_FILE = os.path.join(OUTPUT_DIR, "skipped_orders.txt")      # Output for skipped orders
LOG_FILE = os.path.join(LOG_DIR, "execution_log.txt")              # Log file

# Function to log messages with timestamp and severity level
def log(message, level="INFO"):
    timestamp = date.today().strftime("%Y-%m-%d")   # Current date as string
    entry = f"[{timestamp}] {level}: {message}\n"   # Format log entry
    with open(LOG_FILE, "a", encoding="utf-8") as logf:   # Append to log file
        logf.write(entry)

# Function to create required folders if they don’t exist
def setup_folders():
    for folder in [INPUT_DIR, OUTPUT_DIR, LOG_DIR]:
        if not os.path.exists(folder):   # Check if folder exists
            os.mkdir(folder)             # Create folder if missing
    log("Folder check completed")        # Log folder setup completion

# Function to parse dates in multiple formats
def parse_date(date_str):
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"]   # Supported formats
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()   # Try parsing
        except ValueError:
            continue   # If format doesn’t match, try next
    return None        # Return None if parsing fails

# Function to calculate delivery date (5 days after order, skipping Sundays)
def calculate_delivery_date(order_date):
    delivery_date = order_date + timedelta(days=5)   # Base delivery = order_date + 5 days
    sundays_crossed = 0
    for i in range(1, 6):   # Check each day in the 5-day window
        check_day = order_date + timedelta(days=i)
        if check_day.weekday() == 6:   # weekday() == 6 means Sunday
            sundays_crossed += 1
    delivery_date += timedelta(days=sundays_crossed)   # Add extra days for Sundays
    return delivery_date

# Main function to process orders
def process_orders():
    today = date.today()   # Current date
    log("Started Order Processing")   # Log start

    # Check if orders file exists
    if not os.path.exists(ORDERS_FILE):
        log("Orders file not found", "ERROR")
        return

    # Open input orders file, processed output file, and skipped output file
    with open(ORDERS_FILE, mode="r", encoding="utf-8" ) as file, \
         open(PROCESSED_FILE, "w", encoding="utf-8") as processed, \
         open(SKIPPED_FILE, "w", encoding="utf-8") as skipped:

        # Read orders file as tab-delimited CSV
        reader = csv.DictReader(file, delimiter="\t") 
        next(reader)   # Skip header row if present
        header = reader.fieldnames   # Get column names
        print(header[0])             # Debug: print first header
        print(f"Headers found: {header}")   # Debug: print all headers

        # Iterate through each row in the orders file
        for row in reader:
            # Extract basic fields from header (first 3 columns)
            order_id = header[0]
            customer = header[1]
            product = header[2]

            # Validate numeric fields (quantity and unit_price)
            try:
                quantity = int(row.get("quantity"))
                unit_price = int(row.get("unit_price"))
            except (TypeError, ValueError):
                skipped.write(f"OrderID: {order_id} | Reason: Invalid numeric values\n")
                log(f"Order {order_id} skipped - Invalid numeric values", "WARNING")
                continue   # Skip this order

            # Parse order date
            order_date_str = row.get("order_date")
            order_date = parse_date(order_date_str)

            # Validation checks
            if quantity <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid quantity\n")
                log(f"Order {order_id} skipped - Invalid quantity", "WARNING")
                continue
            
            if unit_price <= 0:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid unit price\n")
                log(f"Order {order_id} skipped - Invalid unit price", "WARNING")
                continue
            
            if order_date is None:
                skipped.write(f"OrderID: {order_id} | Reason: Invalid date\n")
                log(f"Order {order_id} skipped - Invalid date", "WARNING")
                continue
            
            if order_date >= today:
                skipped.write(f"OrderID: {order_id} | Reason: Order date in the future\n")
                log(f"Order {order_id} skipped - Future date", "WARNING")
                continue

            # If all validations pass, process the order
            log(f"Processing order {order_id}")

            total_cost = math.ceil(quantity * unit_price)   # Calculate total cost
            delivery_date = calculate_delivery_date(order_date)   # Calculate delivery date

            # Write processed order details to file
            processed.write(
                f"OrderID: {order_id}\n"
                f"Customer: {customer}\n"
                f"Product: {product}\n"
                f"Quantity: {quantity}\n"
                f"Unit Price: {unit_price}\n"
                f"Total Cost: {total_cost}\n"
                f"Order Date: {order_date}\n"
                f"Estimated Delivery: {delivery_date}\n"
                "--------------------------------------------------\n"
            )

            log(f"Order {order_id} processed successfully")

    log("Finished Order Processing")   # Log completion

# Entry point of the script
if __name__ == "__main__":
    setup_folders()   # Ensure folders exist
    process_orders()  # Run order processing
