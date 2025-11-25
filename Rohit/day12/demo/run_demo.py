import os 
import sys

# BASE_DIR is set to the parent directory of the current file’s directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add BASE_DIR to Python’s module search path so ust_tools_micro can be imported
sys.path.append(BASE_DIR)

# Import custom modules from ust_tools_micro package
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import required_fileds, to_int

# Define paths to inventory and order CSV files
inventory_path = os.path.join(BASE_DIR, 'data', 'inventory.csv')
order_path = os.path.join(BASE_DIR, 'data', 'order.csv')

def run_demo():
    # Load inventory from CSV into Inventory object
    inv = Inventory.from_csv(inventory_path)
    print("Initial stock:", inv.items)

    # Read orders from CSV file
    orders = read_csv(order_path)

    # Validate that required fields exist in orders
    if not required_fileds(orders, ['item_id', 'quantity']):
        print("Order data is missing required fields.")
        return

    # Process each order
    for order in orders:
        order_id = order.get("order_id")
        item_id = order.get("item_id")
        qty = to_int(order.get("quantity", "0"))   # Convert quantity to integer safely
        
        # Skip invalid quantities
        if qty is None:
            print(f"Invalid quantity for order {order_id}. Skipping.")
            continue

        # Try to allocate stock
        if inv.allocate(item_id, qty):
            print(f"Order {order_id} for item {item_id} of quantity {qty} allocated successfully.")
        else:
            print(f"Order {order_id} for item {item_id} of quantity {qty} could not be allocated due to insufficient stock.")
            
            
# Entry point of the script
if __name__ == "__main__":
    run_demo()
