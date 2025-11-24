# Import required functions and classes from ust_tools_micro
from ust_tools_micro import (read_csv, write_csv, require_fields, to_int, Inventory)

# Define the path where your CSV files are stored
path = "C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/data"

# Load orders and inventory data from CSV files into Python lists/dictionaries
load_orders = read_csv(path + "/orders.csv")
load_inventory = read_csv(path + "/inventory.csv")

# Create an Inventory object and initialize it with inventory data from CSV
inventory_obj = Inventory()
inventory_obj.from_csv(path + "/inventory.csv")

# Define the required fields that every order must contain
field = ["order_id", "item_id", "quantity"]

# Iterate through each order in the orders list
for data in load_orders:
    # Check if the order contains all required fields
    if(require_fields(data, field)):
        # Check if the 'quantity' field can be converted to an integer
        if(to_int(data["quantity"])):
            # Convert 'quantity' to integer
            data["quantity"] = to_int(data["quantity"])
            
            # Try to allocate inventory for the given item and quantity
            if(inventory_obj.allocate(data["item_id"], data["quantity"])):
                # If allocation succeeds, update the order quantity 
                # by adding the remaining stock of that item
                data["quantity"] += int(inventory_obj.datas[data["item_id"]])
                print(f"ALLOCATED: -> {data}")
            else:
                # If allocation fails (not enough stock), mark as FAILED
                print(f"FAILED: -> {data}")
        else:
            # If quantity is not a valid integer, mark as INVALID
            print(f"INVALID ORDER: -> {data}")
    else:
        # If required fields are missing, mark as INVALID ORDER
        print(f"INVALID ORDER: -> {data}")