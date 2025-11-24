# from csv_utils  import read_csv
# from validation import required_fields
import os   # Import OS module for file path handling
from ust_tool_micro import (read_csv,required_fields,Inventory)   # Import custom utilities

# Build path to data directory
current = os.getcwd() + "\\akhil_praveen\\day12\\task-package-module\\data"

inventory_obj = Inventory()   # Create Inventory object

try:
    # Read orders file (returns rows and header)
    orders_file,order_header = read_csv(current+"/orders.csv")
    
    # Load inventory data from CSV
    inventory_obj.from_csv(current+"/inventory.csv")
    
    # Process each order row
    for row in orders_file: 
        condition = required_fields(row,order_header)   # Validate required fields
        if condition:
            # Allocate inventory based on product and quantity
            inventory_obj.allocate(row[order_header[1]],int(row[order_header[2]]))

except Exception as e:
    print(str(e))   # Print error message if exception occurs
