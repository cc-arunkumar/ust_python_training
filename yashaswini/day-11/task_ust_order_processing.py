import os
import csv
import math
import logging
from datetime import datetime, date, timedelta

# Folder setup
folders = {
    "input": "task/input",
    "output": "task/output",
    "logs": "task/logs"
}

# File paths
input_file = os.path.join(folders["input"], "orders.csv")
processed_file = os.path.join(folders["output"], "processed_orders.txt")
skipped_file = os.path.join(folders["output"], "skipped_orders.txt")
log_file = os.path.join(folders["logs"], "execution_log.txt")

def create_folders():
    """Make sure folders exist."""
    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)

def setup_logging():
    """Setup logging."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format= "%(message)s"
    )

def validate_date(order_date_str):
    """Check if date is valid and not in the future."""
    try:
        order_date = datetime.strptime(order_date_str, "%Y-%m-%d").date()
        return order_date <= date.today()
    except ValueError:
        return False

def calculate_total_cost(quantity, unit_price):
    """Calculate total cost (rounded up)."""
    return math.ceil(quantity * unit_price)

def calculate_delivery_date(order_date):
    """Add 5 days, skip Sunday if needed."""
    delivery_date = order_date + timedelta(days=5)
    while delivery_date.weekday() == 6:  # 6 = Sunday
        delivery_date += timedelta(days=1)
    return delivery_date.strftime("%d-%m-%y,%A")

def process_orders():
    """Read orders, validate, process, and save results."""
    processed_orders, skipped_orders = [], []

    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            order_id = row["order_id"]
            customer = row["customer_name"]
            product = row["product"]
            try:
                quantity = int(row["quantity"])
                price = float(row["unit_price"])
            except ValueError:
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid number")
                continue

            if quantity <= 0:
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid quantity")
                continue
            if price <= 0:
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid price")
                continue
            if not validate_date(row["order_date"]):
                skipped_orders.append(f"OrderID: {order_id} | Reason: Invalid date")
                continue

            order_date = datetime.strptime(row["order_date"], "%Y-%m-%d").date()
            total_cost = calculate_total_cost(quantity, price)
            delivery = calculate_delivery_date(order_date)

            processed_orders.append(
                f"OrderID: {order_id}\nCustomer: {customer}\nProduct: {product}\n"
                f"Quantity: {quantity}\nUnit Price: {price}\nTotal Cost: {total_cost}\n"
                f"Order Date: {order_date.strftime('%d-%m-%y,%A')}\n"
                f"Estimated Delivery: {delivery}\n{'-'*50}\n"
            )

    # Save results
    with open(processed_file, "w") as f:
        f.writelines(processed_orders)
    with open(skipped_file, "w") as f:
        f.writelines([order + "\n" for order in skipped_orders])

def main():
    create_folders()
    setup_logging()
    logging.info("Started order processing")
    process_orders()
    logging.info("Finished order processing")

if __name__ == "__main__":
    main()


# Output

# Contents in execution_log.txt file

# 2025-11-17 16:07:55,608 - INFO - Started order processing script.
# 2025-11-17 16:07:55,615 - INFO - Processing OrderID: 101, Customer: Asha Nair, Product: Laptop
# 2025-11-17 16:07:55,616 - INFO - Calculated total cost: 90000
# 2025-11-17 16:07:55,616 - INFO - Estimated delivery date: 15-01-25,Wednesday:2
# 2025-11-17 16:07:55,616 - INFO - Processing OrderID: 102, Customer: Rahul Menon, Product: Keyboard
# 2025-11-17 16:07:55,616 - INFO - Calculated total cost: 3600
# 2025-11-17 16:07:55,616 - INFO - Estimated delivery date: 20-01-25,Monday:0
# 2025-11-17 16:07:55,616 - WARNING - OrderID: 103 skipped due to invalid quantity.
# 2025-11-17 16:07:55,618 - ERROR - Invalid date format for order date: 2025-02-30
# 2025-11-17 16:07:55,618 - WARNING - OrderID: 104 skipped due to invalid date.
# 2025-11-17 16:07:55,619 - WARNING - Order date 2026-01-01 is in the future.
# 2025-11-17 16:07:55,619 - WARNING - OrderID: 105 skipped due to invalid date.
# 2025-11-17 16:07:55,619 - INFO - Processing OrderID: 106, Customer: Sameer R, Product: Headphones
# 2025-11-17 16:07:55,619 - INFO - Calculated total cost: 2500
# 2025-11-17 16:07:55,619 - INFO - Estimated delivery date: 10-03-25,Monday:0
# 2025-11-17 16:07:55,619 - WARNING - OrderID: 107 skipped due to invalid quantity.
# 2025-11-17 16:07:55,619 - WARNING - OrderID: 108 skipped due to invalid price.
# 2025-11-17 16:07:55,619 - INFO - Processing OrderID: 109, Customer: Lekha Joseph, Product: Printer
# 2025-11-17 16:07:55,619 - INFO - Calculated total cost: 12000
# 2025-11-17 16:07:55,619 - INFO - Estimated delivery date: 06-12-24,Friday:4
# 2025-11-17 16:07:55,619 - INFO - Processing OrderID: 110, Customer: John Daniel, Product: SSD
# 2025-11-17 16:07:55,619 - INFO - Calculated total cost: 10500
# 2025-11-17 16:07:55,620 - INFO - Estimated delivery date: 23-07-25,Wednesday:2
# 2025-11-17 16:07:55,620 - INFO - Processing OrderID: 111, Customer: Vinod Kumar, Product: Router
# 2025-11-17 16:07:55,620 - INFO - Calculated total cost: 4500
# 2025-11-17 16:07:55,620 - INFO - Estimated delivery date: 27-05-25,Tuesday:1
# 2025-11-17 16:07:55,620 - ERROR - Invalid date format for order date: 2025-01-32
# 2025-11-17 16:07:55,620 - WARNING - OrderID: 112 skipped due to invalid date.
# 2025-11-17 16:07:55,620 - ERROR - Invalid date format for order date: 2025-13-10
# 2025-11-17 16:07:55,620 - WARNING - OrderID: 113 skipped due to invalid date.
# 2025-11-17 16:07:55,620 - ERROR - Invalid date format for order date: 2025-00-15
# 2025-11-17 16:07:55,620 - WARNING - OrderID: 114 skipped due to invalid date.
# 2025-11-17 16:07:55,620 - INFO - Processing OrderID: 115, Customer: Kiran Babu, Product: Monitor
# 2025-11-17 16:07:55,620 - INFO - Calculated total cost: 8500
# 2025-11-17 16:07:55,620 - INFO - Estimated delivery date: 10-01-25,Friday:4
# 2025-11-17 16:07:55,620 - WARNING - OrderID: 116 skipped due to invalid quantity.
# 2025-11-17 16:07:55,620 - WARNING - Order date 2027-05-10 is in the future.
# 2025-11-17 16:07:55,620 - WARNING - OrderID: 117 skipped due to invalid date.
# 2025-11-17 16:07:55,621 - INFO - Processing OrderID: 118, Customer: Nithin P, Product: Mousepad
# 2025-11-17 16:07:55,621 - INFO - Calculated total cost: 800
# 2025-11-17 16:07:55,621 - INFO - Estimated delivery date: 10-11-25,Monday:0
# 2025-11-17 16:07:55,621 - INFO - Processing OrderID: 119, Customer: Sachin Patil, Product: Printer
# 2025-11-17 16:07:55,621 - INFO - Calculated total cost: 13000
# 2025-11-17 16:07:55,621 - INFO - Estimated delivery date: 03-11-25,Monday:0
# 2025-11-17 16:07:55,621 - INFO - Processing OrderID: 120, Customer: Roshan George, Product: Laptop
# 2025-11-17 16:07:55,621 - INFO - Calculated total cost: 110000
# 2025-11-17 16:07:55,621 - INFO - Estimated delivery date: 22-04-25,Tuesday:1
# 2025-11-17 16:07:55,621 - INFO - Processing OrderID: 121, Customer: Anu Mathew, Product: Keyboard
# 2025-11-17 16:07:55,621 - INFO - Calculated total cost: 4800
# 2025-11-17 16:07:55,621 - INFO - Estimated delivery date: 20-03-25,Thursday:3
# 2025-11-17 16:07:55,621 - INFO - Processing OrderID: 122, Customer: Karthik Iyer, Product: Mouse
# 2025-11-17 16:07:55,621 - INFO - Calculated total cost: 3200
# 2025-11-17 16:07:55,621 - INFO - Estimated delivery date: 15-02-25,Saturday:5
# 2025-11-17 16:07:55,622 - ERROR - Invalid date format for order date: 2025-02-29
# 2025-11-17 16:07:55,622 - WARNING - OrderID: 123 skipped due to invalid date.
# 2025-11-17 16:07:55,622 - INFO - Processing OrderID: 124, Customer: Suhail Ahmed, Product: Monitor
# 2025-11-17 16:07:55,622 - INFO - Calculated total cost: 18000
# 2025-11-17 16:07:55,622 - INFO - Estimated delivery date: 30-11-24,Saturday:5
# 2025-11-17 16:07:55,622 - INFO - Processing OrderID: 125, Customer: Keerthi S, Product: Laptop
# 2025-11-17 16:07:55,622 - INFO - Calculated total cost: 47000
# 2025-11-17 16:07:55,622 - INFO - Estimated delivery date: 19-09-25,Friday:4
# 2025-11-17 16:07:55,622 - WARNING - OrderID: 126 skipped due to invalid quantity.
# 2025-11-17 16:07:55,622 - INFO - Processing OrderID: 127, Customer: Ganesh Rao, Product: Mousepad
# 2025-11-17 16:07:55,622 - INFO - Calculated total cost: 2000
# 2025-11-17 16:07:55,622 - INFO - Estimated delivery date: 10-06-25,Tuesday:1
# 2025-11-17 16:07:55,622 - WARNING - OrderID: 128 skipped due to invalid price.
# 2025-11-17 16:07:55,622 - INFO - Processing OrderID: 129, Customer: Arjun S, Product: SSD
# 2025-11-17 16:07:55,622 - INFO - Calculated total cost: 11400
# 2025-11-17 16:07:55,622 - INFO - Estimated delivery date: 04-01-25,Saturday:5
# 2025-11-17 16:07:55,623 - ERROR - Invalid date format for order date: 2025-04-31
# 2025-11-17 16:07:55,623 - WARNING - OrderID: 130 skipped due to invalid date.
# 2025-11-17 16:07:55,623 - WARNING - OrderID: 131 skipped due to invalid price.
# 2025-11-17 16:07:55,623 - INFO - Processing OrderID: 132, Customer: Manoj Pillai, Product: Webcam
# 2025-11-17 16:07:55,623 - INFO - Calculated total cost: 3600
# 2025-11-17 16:07:55,623 - INFO - Estimated delivery date: 10-02-25,Monday:0
# 2025-11-17 16:07:55,623 - INFO - Processing OrderID: 133, Customer: Sreedevi P, Product: Mouse
# 2025-11-17 16:07:55,623 - INFO - Calculated total cost: 700
# 2025-11-17 16:07:55,623 - INFO - Estimated delivery date: 25-05-23,Thursday:3
# 2025-11-17 16:07:55,623 - INFO - Processing OrderID: 134, Customer: Tanvi Shah, Product: Laptop
# 2025-11-17 16:07:55,623 - INFO - Calculated total cost: 100000
# 2025-11-17 16:07:55,623 - INFO - Estimated delivery date: 30-05-25,Friday:4
# 2025-11-17 16:07:55,623 - WARNING - OrderID: 135 skipped due to invalid quantity.
# 2025-11-17 16:07:55,623 - INFO - Processing OrderID: 136, Customer: Om Prakash, Product: Monitor
# 2025-11-17 16:07:55,623 - INFO - Calculated total cost: 8500
# 2025-11-17 16:07:55,623 - INFO - Estimated delivery date: 15-09-25,Monday:0
# 2025-11-17 16:07:55,624 - INFO - Processing OrderID: 137, Customer: Meghana R, Product: SSD
# 2025-11-17 16:07:55,624 - INFO - Calculated total cost: 6000
# 2025-11-17 16:07:55,624 - INFO - Estimated delivery date: 25-08-25,Monday:0
# 2025-11-17 16:07:55,624 - INFO - Processing OrderID: 138, Customer: Nazim Khan, Product: Mousepad
# 2025-11-17 16:07:55,624 - INFO - Calculated total cost: 1000
# 2025-11-17 16:07:55,624 - INFO - Estimated delivery date: 05-03-25,Wednesday:2
# 2025-11-17 16:07:55,624 - INFO - Processing OrderID: 139, Customer: Riya Sen, Product: Headphones
# 2025-11-17 16:07:55,624 - INFO - Calculated total cost: 2500
# 2025-11-17 16:07:55,624 - INFO - Estimated delivery date: 20-06-25,Friday:4
# 2025-11-17 16:07:55,624 - INFO - Processing OrderID: 140, Customer: Arvind Gupta, Product: Router
# 2025-11-17 16:07:55,624 - INFO - Calculated total cost: 4500
# 2025-11-17 16:07:55,624 - INFO - Estimated delivery date: 06-10-25,Monday:0
# 2025-11-17 16:07:55,624 - WARNING - OrderID: 141 skipped due to invalid quantity.
# 2025-11-17 16:07:55,624 - INFO - Processing OrderID: 142, Customer: Kavya Menon, Product: Keyboard
# 2025-11-17 16:07:55,624 - INFO - Calculated total cost: 3900
# 2025-11-17 16:07:55,624 - INFO - Estimated delivery date: 10-07-25,Thursday:3
# 2025-11-17 16:07:55,625 - INFO - Processing OrderID: 143, Customer: Anoop Krishnan, Product: Laptop
# 2025-11-17 16:07:55,625 - INFO - Calculated total cost: 104000
# 2025-11-17 16:07:55,625 - INFO - Estimated delivery date: 27-03-25,Thursday:3
# 2025-11-17 16:07:55,625 - WARNING - OrderID: 144 skipped due to invalid quantity.
# 2025-11-17 16:07:55,625 - INFO - Processing OrderID: 145, Customer: Swapna Rao, Product: Mouse
# 2025-11-17 16:07:55,625 - INFO - Calculated total cost: 2100
# 2025-11-17 16:07:55,625 - INFO - Estimated delivery date: 05-07-25,Saturday:5
# 2025-11-17 16:07:55,625 - INFO - Processing OrderID: 146, Customer: Niharika S, Product: Router
# 2025-11-17 16:07:55,625 - INFO - Calculated total cost: 4500
# 2025-11-17 16:07:55,625 - INFO - Estimated delivery date: 04-03-25,Tuesday:1
# 2025-11-17 16:07:55,625 - WARNING - Order date 2025-12-15 is in the future.
# 2025-11-17 16:07:55,625 - WARNING - OrderID: 147 skipped due to invalid date.
# 2025-11-17 16:07:55,625 - INFO - Processing OrderID: 148, Customer: Sheela Chacko, Product: Laptop
# 2025-11-17 16:07:55,626 - INFO - Calculated total cost: 102000
# 2025-11-17 16:07:55,626 - INFO - Estimated delivery date: 15-05-25,Thursday:3
# 2025-11-17 16:07:55,626 - INFO - Processing OrderID: 149, Customer: Rohit Shetty, Product: Keyboard
# 2025-11-17 16:07:55,626 - INFO - Calculated total cost: 3300
# 2025-11-17 16:07:55,626 - INFO - Estimated delivery date: 23-05-25,Friday:4
# 2025-11-17 16:07:55,626 - WARNING - Order date 2025-12-20 is in the future.
# 2025-11-17 16:07:55,626 - WARNING - OrderID: 150 skipped due to invalid date.
# 2025-11-17 16:07:55,628 - INFO - Finished order processing script.
# 2025-11-17 16:30:45,856 - INFO - Started order processing script.
# 2025-11-17 16:30:45,864 - INFO - Processing OrderID: 101, Customer: Asha Nair, Product: Laptop
# 2025-11-17 16:30:45,864 - INFO - Calculated total cost: 90000
# 2025-11-17 16:30:45,864 - INFO - Estimated delivery date: 15-01-25,Wednesday:2
# 2025-11-17 16:30:45,864 - INFO - Processing OrderID: 102, Customer: Rahul Menon, Product: Keyboard
# 2025-11-17 16:30:45,864 - INFO - Calculated total cost: 3600
# 2025-11-17 16:30:45,864 - INFO - Estimated delivery date: 20-01-25,Monday:0
# 2025-11-17 16:30:45,864 - WARNING - OrderID: 103 skipped due to invalid quantity.
# 2025-11-17 16:30:45,864 - ERROR - Invalid date format for order date: 2025-02-30
# 2025-11-17 16:30:45,864 - WARNING - OrderID: 104 skipped due to invalid date.
# 2025-11-17 16:30:45,865 - WARNING - Order date 2026-01-01 is in the future.
# 2025-11-17 16:30:45,865 - WARNING - OrderID: 105 skipped due to invalid date.
# 2025-11-17 16:30:45,865 - INFO - Processing OrderID: 106, Customer: Sameer R, Product: Headphones
# 2025-11-17 16:30:45,865 - INFO - Calculated total cost: 2500
# 2025-11-17 16:30:45,865 - INFO - Estimated delivery date: 10-03-25,Monday:0
# 2025-11-17 16:30:45,865 - WARNING - OrderID: 107 skipped due to invalid quantity.
# 2025-11-17 16:30:45,865 - WARNING - OrderID: 108 skipped due to invalid price.
# 2025-11-17 16:30:45,865 - INFO - Processing OrderID: 109, Customer: Lekha Joseph, Product: Printer
# 2025-11-17 16:30:45,865 - INFO - Calculated total cost: 12000
# 2025-11-17 16:30:45,865 - INFO - Estimated delivery date: 06-12-24,Friday:4
# 2025-11-17 16:30:45,865 - INFO - Processing OrderID: 110, Customer: John Daniel, Product: SSD
# 2025-11-17 16:30:45,865 - INFO - Calculated total cost: 10500
# 2025-11-17 16:30:45,865 - INFO - Estimated delivery date: 23-07-25,Wednesday:2
# 2025-11-17 16:30:45,865 - INFO - Processing OrderID: 111, Customer: Vinod Kumar, Product: Router
# 2025-11-17 16:30:45,865 - INFO - Calculated total cost: 4500
# 2025-11-17 16:30:45,865 - INFO - Estimated delivery date: 27-05-25,Tuesday:1
# 2025-11-17 16:30:45,866 - ERROR - Invalid date format for order date: 2025-01-32
# 2025-11-17 16:30:45,866 - WARNING - OrderID: 112 skipped due to invalid date.
# 2025-11-17 16:30:45,866 - ERROR - Invalid date format for order date: 2025-13-10
# 2025-11-17 16:30:45,866 - WARNING - OrderID: 113 skipped due to invalid date.
# 2025-11-17 16:30:45,866 - ERROR - Invalid date format for order date: 2025-00-15
# 2025-11-17 16:30:45,866 - WARNING - OrderID: 114 skipped due to invalid date.
# 2025-11-17 16:30:45,866 - INFO - Processing OrderID: 115, Customer: Kiran Babu, Product: Monitor
# 2025-11-17 16:30:45,866 - INFO - Calculated total cost: 8500
# 2025-11-17 16:30:45,866 - INFO - Estimated delivery date: 10-01-25,Friday:4
# 2025-11-17 16:30:45,866 - WARNING - OrderID: 116 skipped due to invalid quantity.
# 2025-11-17 16:30:45,866 - WARNING - Order date 2027-05-10 is in the future.
# 2025-11-17 16:30:45,866 - WARNING - OrderID: 117 skipped due to invalid date.
# 2025-11-17 16:30:45,866 - INFO - Processing OrderID: 118, Customer: Nithin P, Product: Mousepad
# 2025-11-17 16:30:45,866 - INFO - Calculated total cost: 800
# 2025-11-17 16:30:45,866 - INFO - Estimated delivery date: 10-11-25,Monday:0
# 2025-11-17 16:30:45,867 - INFO - Processing OrderID: 119, Customer: Sachin Patil, Product: Printer
# 2025-11-17 16:30:45,867 - INFO - Calculated total cost: 13000
# 2025-11-17 16:30:45,867 - INFO - Estimated delivery date: 03-11-25,Monday:0
# 2025-11-17 16:30:45,867 - INFO - Processing OrderID: 120, Customer: Roshan George, Product: Laptop
# 2025-11-17 16:30:45,867 - INFO - Calculated total cost: 110000
# 2025-11-17 16:30:45,867 - INFO - Estimated delivery date: 22-04-25,Tuesday:1
# 2025-11-17 16:30:45,867 - INFO - Processing OrderID: 121, Customer: Anu Mathew, Product: Keyboard
# 2025-11-17 16:30:45,867 - INFO - Calculated total cost: 4800
# 2025-11-17 16:30:45,867 - INFO - Estimated delivery date: 20-03-25,Thursday:3
# 2025-11-17 16:30:45,867 - INFO - Processing OrderID: 122, Customer: Karthik Iyer, Product: Mouse
# 2025-11-17 16:30:45,867 - INFO - Calculated total cost: 3200
# 2025-11-17 16:30:45,867 - INFO - Estimated delivery date: 15-02-25,Saturday:5
# 2025-11-17 16:30:45,867 - ERROR - Invalid date format for order date: 2025-02-29
# 2025-11-17 16:30:45,867 - WARNING - OrderID: 123 skipped due to invalid date.
# 2025-11-17 16:30:45,867 - INFO - Processing OrderID: 124, Customer: Suhail Ahmed, Product: Monitor
# 2025-11-17 16:30:45,867 - INFO - Calculated total cost: 18000
# 2025-11-17 16:30:45,867 - INFO - Estimated delivery date: 30-11-24,Saturday:5
# 2025-11-17 16:30:45,868 - INFO - Processing OrderID: 125, Customer: Keerthi S, Product: Laptop
# 2025-11-17 16:30:45,868 - INFO - Calculated total cost: 47000
# 2025-11-17 16:30:45,868 - INFO - Estimated delivery date: 19-09-25,Friday:4
# 2025-11-17 16:30:45,868 - WARNING - OrderID: 126 skipped due to invalid quantity.
# 2025-11-17 16:30:45,868 - INFO - Processing OrderID: 127, Customer: Ganesh Rao, Product: Mousepad
# 2025-11-17 16:30:45,868 - INFO - Calculated total cost: 2000
# 2025-11-17 16:30:45,868 - INFO - Estimated delivery date: 10-06-25,Tuesday:1
# 2025-11-17 16:30:45,868 - WARNING - OrderID: 128 skipped due to invalid price.
# 2025-11-17 16:30:45,868 - INFO - Processing OrderID: 129, Customer: Arjun S, Product: SSD
# 2025-11-17 16:30:45,868 - INFO - Calculated total cost: 11400
# 2025-11-17 16:30:45,868 - INFO - Estimated delivery date: 04-01-25,Saturday:5
# 2025-11-17 16:30:45,868 - ERROR - Invalid date format for order date: 2025-04-31
# 2025-11-17 16:30:45,868 - WARNING - OrderID: 130 skipped due to invalid date.
# 2025-11-17 16:30:45,868 - WARNING - OrderID: 131 skipped due to invalid price.
# 2025-11-17 16:30:45,868 - INFO - Processing OrderID: 132, Customer: Manoj Pillai, Product: Webcam
# 2025-11-17 16:30:45,868 - INFO - Calculated total cost: 3600
# 2025-11-17 16:30:45,868 - INFO - Estimated delivery date: 10-02-25,Monday:0
# 2025-11-17 16:30:45,869 - INFO - Processing OrderID: 133, Customer: Sreedevi P, Product: Mouse
# 2025-11-17 16:30:45,869 - INFO - Calculated total cost: 700
# 2025-11-17 16:30:45,869 - INFO - Estimated delivery date: 25-05-23,Thursday:3
# 2025-11-17 16:30:45,869 - INFO - Processing OrderID: 134, Customer: Tanvi Shah, Product: Laptop
# 2025-11-17 16:30:45,869 - INFO - Calculated total cost: 100000
# 2025-11-17 16:30:45,869 - INFO - Estimated delivery date: 30-05-25,Friday:4
# 2025-11-17 16:30:45,869 - WARNING - OrderID: 135 skipped due to invalid quantity.
# 2025-11-17 16:30:45,869 - INFO - Processing OrderID: 136, Customer: Om Prakash, Product: Monitor
# 2025-11-17 16:30:45,869 - INFO - Calculated total cost: 8500
# 2025-11-17 16:30:45,869 - INFO - Estimated delivery date: 15-09-25,Monday:0
# 2025-11-17 16:30:45,869 - INFO - Processing OrderID: 137, Customer: Meghana R, Product: SSD
# 2025-11-17 16:30:45,869 - INFO - Calculated total cost: 6000
# 2025-11-17 16:30:45,869 - INFO - Estimated delivery date: 25-08-25,Monday:0
# 2025-11-17 16:30:45,869 - INFO - Processing OrderID: 138, Customer: Nazim Khan, Product: Mousepad
# 2025-11-17 16:30:45,869 - INFO - Calculated total cost: 1000
# 2025-11-17 16:30:45,870 - INFO - Estimated delivery date: 05-03-25,Wednesday:2
# 2025-11-17 16:30:45,870 - INFO - Processing OrderID: 139, Customer: Riya Sen, Product: Headphones
# 2025-11-17 16:30:45,870 - INFO - Calculated total cost: 2500
# 2025-11-17 16:30:45,870 - INFO - Estimated delivery date: 20-06-25,Friday:4
# 2025-11-17 16:30:45,870 - INFO - Processing OrderID: 140, Customer: Arvind Gupta, Product: Router
# 2025-11-17 16:30:45,870 - INFO - Calculated total cost: 4500
# 2025-11-17 16:30:45,870 - INFO - Estimated delivery date: 06-10-25,Monday:0
# 2025-11-17 16:30:45,870 - WARNING - OrderID: 141 skipped due to invalid quantity.
# 2025-11-17 16:30:45,870 - INFO - Processing OrderID: 142, Customer: Kavya Menon, Product: Keyboard
# 2025-11-17 16:30:45,870 - INFO - Calculated total cost: 3900
# 2025-11-17 16:30:45,870 - INFO - Estimated delivery date: 10-07-25,Thursday:3
# 2025-11-17 16:30:45,870 - INFO - Processing OrderID: 143, Customer: Anoop Krishnan, Product: Laptop
# 2025-11-17 16:30:45,870 - INFO - Calculated total cost: 104000
# 2025-11-17 16:30:45,870 - INFO - Estimated delivery date: 27-03-25,Thursday:3
# 2025-11-17 16:30:45,870 - WARNING - OrderID: 144 skipped due to invalid quantity.
# 2025-11-17 16:30:45,870 - INFO - Processing OrderID: 145, Customer: Swapna Rao, Product: Mouse
# 2025-11-17 16:30:45,871 - INFO - Calculated total cost: 2100
# 2025-11-17 16:30:45,871 - INFO - Estimated delivery date: 05-07-25,Saturday:5
# 2025-11-17 16:30:45,871 - INFO - Processing OrderID: 146, Customer: Niharika S, Product: Router
# 2025-11-17 16:30:45,871 - INFO - Calculated total cost: 4500
# 2025-11-17 16:30:45,871 - INFO - Estimated delivery date: 04-03-25,Tuesday:1
# 2025-11-17 16:30:45,871 - WARNING - Order date 2025-12-15 is in the future.
# 2025-11-17 16:30:45,871 - WARNING - OrderID: 147 skipped due to invalid date.
# 2025-11-17 16:30:45,871 - INFO - Processing OrderID: 148, Customer: Sheela Chacko, Product: Laptop
# 2025-11-17 16:30:45,871 - INFO - Calculated total cost: 102000
# 2025-11-17 16:30:45,871 - INFO - Estimated delivery date: 15-05-25,Thursday:3
# 2025-11-17 16:30:45,871 - INFO - Processing OrderID: 149, Customer: Rohit Shetty, Product: Keyboard
# 2025-11-17 16:30:45,871 - INFO - Calculated total cost: 3300
# 2025-11-17 16:30:45,871 - INFO - Estimated delivery date: 23-05-25,Friday:4
# 2025-11-17 16:30:45,871 - WARNING - Order date 2025-12-20 is in the future.
# 2025-11-17 16:30:45,871 - WARNING - OrderID: 150 skipped due to invalid date.
# 2025-11-17 16:30:45,873 - INFO - Finished order processing script.
# 2025-11-17 16:37:34,168 - INFO - Started order processing script.
# 2025-11-17 16:37:34,176 - INFO - Processing OrderID: 101, Customer: Asha Nair, Product: Laptop
# 2025-11-17 16:37:34,176 - INFO - Calculated total cost: 90000
# 2025-11-17 16:37:34,176 - INFO - Estimated delivery date: 15-01-25,Wednesday:2
# 2025-11-17 16:37:34,176 - INFO - Processing OrderID: 102, Customer: Rahul Menon, Product: Keyboard
# 2025-11-17 16:37:34,176 - INFO - Calculated total cost: 3600
# 2025-11-17 16:37:34,176 - INFO - Estimated delivery date: 20-01-25,Monday:0
# 2025-11-17 16:37:34,176 - WARNING - OrderID: 103 skipped due to invalid quantity.
# 2025-11-17 16:37:34,176 - ERROR - Invalid date format for order date: 2025-02-30
# 2025-11-17 16:37:34,177 - WARNING - OrderID: 104 skipped due to invalid date.
# 2025-11-17 16:37:34,177 - WARNING - Order date 2026-01-01 is in the future.
# 2025-11-17 16:37:34,177 - WARNING - OrderID: 105 skipped due to invalid date.
# 2025-11-17 16:37:34,177 - INFO - Processing OrderID: 106, Customer: Sameer R, Product: Headphones
# 2025-11-17 16:37:34,177 - INFO - Calculated total cost: 2500
# 2025-11-17 16:37:34,177 - INFO - Estimated delivery date: 10-03-25,Monday:0
# 2025-11-17 16:37:34,177 - WARNING - OrderID: 107 skipped due to invalid quantity.
# 2025-11-17 16:37:34,177 - WARNING - OrderID: 108 skipped due to invalid price.
# 2025-11-17 16:37:34,178 - INFO - Processing OrderID: 109, Customer: Lekha Joseph, Product: Printer
# 2025-11-17 16:37:34,178 - INFO - Calculated total cost: 12000
# 2025-11-17 16:37:34,178 - INFO - Estimated delivery date: 06-12-24,Friday:4
# 2025-11-17 16:37:34,178 - INFO - Processing OrderID: 110, Customer: John Daniel, Product: SSD
# 2025-11-17 16:37:34,178 - INFO - Calculated total cost: 10500
# 2025-11-17 16:37:34,178 - INFO - Estimated delivery date: 23-07-25,Wednesday:2
# 2025-11-17 16:37:34,178 - INFO - Processing OrderID: 111, Customer: Vinod Kumar, Product: Router
# 2025-11-17 16:37:34,178 - INFO - Calculated total cost: 4500
# 2025-11-17 16:37:34,178 - INFO - Estimated delivery date: 27-05-25,Tuesday:1
# 2025-11-17 16:37:34,178 - ERROR - Invalid date format for order date: 2025-01-32
# 2025-11-17 16:37:34,178 - WARNING - OrderID: 112 skipped due to invalid date.
# 2025-11-17 16:37:34,178 - ERROR - Invalid date format for order date: 2025-13-10
# 2025-11-17 16:37:34,178 - WARNING - OrderID: 113 skipped due to invalid date.
# 2025-11-17 16:37:34,178 - ERROR - Invalid date format for order date: 2025-00-15
# 2025-11-17 16:37:34,178 - WARNING - OrderID: 114 skipped due to invalid date.
# 2025-11-17 16:37:34,179 - INFO - Processing OrderID: 115, Customer: Kiran Babu, Product: Monitor
# 2025-11-17 16:37:34,179 - INFO - Calculated total cost: 8500
# 2025-11-17 16:37:34,179 - INFO - Estimated delivery date: 10-01-25,Friday:4
# 2025-11-17 16:37:34,179 - WARNING - OrderID: 116 skipped due to invalid quantity.
# 2025-11-17 16:37:34,179 - WARNING - Order date 2027-05-10 is in the future.
# 2025-11-17 16:37:34,179 - WARNING - OrderID: 117 skipped due to invalid date.
# 2025-11-17 16:37:34,179 - INFO - Processing OrderID: 118, Customer: Nithin P, Product: Mousepad
# 2025-11-17 16:37:34,179 - INFO - Calculated total cost: 800
# 2025-11-17 16:37:34,179 - INFO - Estimated delivery date: 10-11-25,Monday:0
# 2025-11-17 16:37:34,179 - INFO - Processing OrderID: 119, Customer: Sachin Patil, Product: Printer
# 2025-11-17 16:37:34,179 - INFO - Calculated total cost: 13000
# 2025-11-17 16:37:34,179 - INFO - Estimated delivery date: 03-11-25,Monday:0
# 2025-11-17 16:37:34,179 - INFO - Processing OrderID: 120, Customer: Roshan George, Product: Laptop
# 2025-11-17 16:37:34,179 - INFO - Calculated total cost: 110000
# 2025-11-17 16:37:34,180 - INFO - Estimated delivery date: 22-04-25,Tuesday:1
# 2025-11-17 16:37:34,180 - INFO - Processing OrderID: 121, Customer: Anu Mathew, Product: Keyboard
# 2025-11-17 16:37:34,180 - INFO - Calculated total cost: 4800
# 2025-11-17 16:37:34,180 - INFO - Estimated delivery date: 20-03-25,Thursday:3
# 2025-11-17 16:37:34,180 - INFO - Processing OrderID: 122, Customer: Karthik Iyer, Product: Mouse
# 2025-11-17 16:37:34,180 - INFO - Calculated total cost: 3200
# 2025-11-17 16:37:34,180 - INFO - Estimated delivery date: 15-02-25,Saturday:5
# 2025-11-17 16:37:34,180 - ERROR - Invalid date format for order date: 2025-02-29
# 2025-11-17 16:37:34,180 - WARNING - OrderID: 123 skipped due to invalid date.
# 2025-11-17 16:37:34,180 - INFO - Processing OrderID: 124, Customer: Suhail Ahmed, Product: Monitor
# 2025-11-17 16:37:34,180 - INFO - Calculated total cost: 18000
# 2025-11-17 16:37:34,180 - INFO - Estimated delivery date: 30-11-24,Saturday:5
# 2025-11-17 16:37:34,180 - INFO - Processing OrderID: 125, Customer: Keerthi S, Product: Laptop
# 2025-11-17 16:37:34,180 - INFO - Calculated total cost: 47000
# 2025-11-17 16:37:34,180 - INFO - Estimated delivery date: 19-09-25,Friday:4
# 2025-11-17 16:37:34,181 - WARNING - OrderID: 126 skipped due to invalid quantity.
# 2025-11-17 16:37:34,181 - INFO - Processing OrderID: 127, Customer: Ganesh Rao, Product: Mousepad
# 2025-11-17 16:37:34,181 - INFO - Calculated total cost: 2000
# 2025-11-17 16:37:34,181 - INFO - Estimated delivery date: 10-06-25,Tuesday:1
# 2025-11-17 16:37:34,181 - WARNING - OrderID: 128 skipped due to invalid price.
# 2025-11-17 16:37:34,181 - INFO - Processing OrderID: 129, Customer: Arjun S, Product: SSD
# 2025-11-17 16:37:34,181 - INFO - Calculated total cost: 11400
# 2025-11-17 16:37:34,181 - INFO - Estimated delivery date: 04-01-25,Saturday:5
# 2025-11-17 16:37:34,181 - ERROR - Invalid date format for order date: 2025-04-31
# 2025-11-17 16:37:34,181 - WARNING - OrderID: 130 skipped due to invalid date.
# 2025-11-17 16:37:34,181 - WARNING - OrderID: 131 skipped due to invalid price.
# 2025-11-17 16:37:34,181 - INFO - Processing OrderID: 132, Customer: Manoj Pillai, Product: Webcam
# 2025-11-17 16:37:34,181 - INFO - Calculated total cost: 3600
# 2025-11-17 16:37:34,181 - INFO - Estimated delivery date: 10-02-25,Monday:0
# 2025-11-17 16:37:34,182 - INFO - Processing OrderID: 133, Customer: Sreedevi P, Product: Mouse
# 2025-11-17 16:37:34,182 - INFO - Calculated total cost: 700
# 2025-11-17 16:37:34,182 - INFO - Estimated delivery date: 25-05-23,Thursday:3
# 2025-11-17 16:37:34,182 - INFO - Processing OrderID: 134, Customer: Tanvi Shah, Product: Laptop
# 2025-11-17 16:37:34,182 - INFO - Calculated total cost: 100000
# 2025-11-17 16:37:34,182 - INFO - Estimated delivery date: 30-05-25,Friday:4
# 2025-11-17 16:37:34,182 - WARNING - OrderID: 135 skipped due to invalid quantity.
# 2025-11-17 16:37:34,182 - INFO - Processing OrderID: 136, Customer: Om Prakash, Product: Monitor
# 2025-11-17 16:37:34,182 - INFO - Calculated total cost: 8500
# 2025-11-17 16:37:34,182 - INFO - Estimated delivery date: 15-09-25,Monday:0
# 2025-11-17 16:37:34,182 - INFO - Processing OrderID: 137, Customer: Meghana R, Product: SSD
# 2025-11-17 16:37:34,182 - INFO - Calculated total cost: 6000
# 2025-11-17 16:37:34,182 - INFO - Estimated delivery date: 25-08-25,Monday:0
# 2025-11-17 16:37:34,182 - INFO - Processing OrderID: 138, Customer: Nazim Khan, Product: Mousepad
# 2025-11-17 16:37:34,183 - INFO - Calculated total cost: 1000
# 2025-11-17 16:37:34,183 - INFO - Estimated delivery date: 05-03-25,Wednesday:2
# 2025-11-17 16:37:34,183 - INFO - Processing OrderID: 139, Customer: Riya Sen, Product: Headphones
# 2025-11-17 16:37:34,183 - INFO - Calculated total cost: 2500
# 2025-11-17 16:37:34,183 - INFO - Estimated delivery date: 20-06-25,Friday:4
# 2025-11-17 16:37:34,183 - INFO - Processing OrderID: 140, Customer: Arvind Gupta, Product: Router
# 2025-11-17 16:37:34,183 - INFO - Calculated total cost: 4500
# 2025-11-17 16:37:34,183 - INFO - Estimated delivery date: 06-10-25,Monday:0
# 2025-11-17 16:37:34,183 - WARNING - OrderID: 141 skipped due to invalid quantity.
# 2025-11-17 16:37:34,183 - INFO - Processing OrderID: 142, Customer: Kavya Menon, Product: Keyboard
# 2025-11-17 16:37:34,183 - INFO - Calculated total cost: 3900
# 2025-11-17 16:37:34,183 - INFO - Estimated delivery date: 10-07-25,Thursday:3
# 2025-11-17 16:37:34,183 - INFO - Processing OrderID: 143, Customer: Anoop Krishnan, Product: Laptop
# 2025-11-17 16:37:34,183 - INFO - Calculated total cost: 104000
# 2025-11-17 16:37:34,183 - INFO - Estimated delivery date: 27-03-25,Thursday:3
# 2025-11-17 16:37:34,183 - WARNING - OrderID: 144 skipped due to invalid quantity.
# 2025-11-17 16:37:34,184 - INFO - Processing OrderID: 145, Customer: Swapna Rao, Product: Mouse
# 2025-11-17 16:37:34,184 - INFO - Calculated total cost: 2100
# 2025-11-17 16:37:34,184 - INFO - Estimated delivery date: 05-07-25,Saturday:5
# 2025-11-17 16:37:34,184 - INFO - Processing OrderID: 146, Customer: Niharika S, Product: Router
# 2025-11-17 16:37:34,184 - INFO - Calculated total cost: 4500
# 2025-11-17 16:37:34,184 - INFO - Estimated delivery date: 04-03-25,Tuesday:1
# 2025-11-17 16:37:34,184 - WARNING - Order date 2025-12-15 is in the future.
# 2025-11-17 16:37:34,184 - WARNING - OrderID: 147 skipped due to invalid date.
# 2025-11-17 16:37:34,184 - INFO - Processing OrderID: 148, Customer: Sheela Chacko, Product: Laptop
# 2025-11-17 16:37:34,184 - INFO - Calculated total cost: 102000
# 2025-11-17 16:37:34,184 - INFO - Estimated delivery date: 15-05-25,Thursday:3
# 2025-11-17 16:37:34,184 - INFO - Processing OrderID: 149, Customer: Rohit Shetty, Product: Keyboard
# 2025-11-17 16:37:34,184 - INFO - Calculated total cost: 3300
# 2025-11-17 16:37:34,184 - INFO - Estimated delivery date: 23-05-25,Friday:4
# 2025-11-17 16:37:34,185 - WARNING - Order date 2025-12-20 is in the future.
# 2025-11-17 16:37:34,185 - WARNING - OrderID: 150 skipped due to invalid date.
# 2025-11-17 16:37:34,186 - INFO - Finished order processing script.
# 2025-11-17 16:52:28,362 - INFO - Started order processing
# 2025-11-17 16:52:28,372 - INFO - Finished order processing
# Started order processing
# Finished order processing
# Started order processing
# Finished order processing
# Started order processing
# Finished order processing
