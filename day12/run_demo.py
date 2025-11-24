# Importing required modules and classes
from ust_tools_micro.inventory import Inventory  # To manage inventory
from ust_tools_micro.utils import read_csv  # To read CSV files
from ust_tools_micro.validators import require_fields, to_int  # For field validation and converting to integers

def run_demo():
    # Load inventory data from 'inventory.csv' into an Inventory object
    inventory = Inventory.from_csv('data/inventory.csv')
    
    # Load orders from 'orders.csv' using the read_csv function
    orders = read_csv('data/orders.csv')

    # Process each order in the orders list
    for order in orders:
        # Validate that the required fields ('order_id', 'item_id', 'quantity') are present in the order
        if not require_fields(order, ['order_id', 'item_id', 'quantity']):
            print(f"Invalid order: {order}")  # If any required fields are missing, print an error message and skip this order
            continue
        
        try:
            # Convert the 'quantity' field from string to integer
            quantity = to_int(order['quantity'])
        except ValueError:
            # If the quantity cannot be converted to an integer, print an error message and skip this order
            print(f"Invalid order: {order}")
            continue
        
        # Attempt to allocate the specified quantity of the item from inventory
        if inventory.allocate(order['item_id'], quantity):
            # If allocation is successful, print the allocation details
            print(f"Allocate: {order['order_id']} -> {order['item_id']} ({quantity})")
        else:
            # If allocation fails (e.g., insufficient stock), print the failure details
            print(f"Failed: {order['order_id']} -> {order['item_id']} ({quantity})")

# Entry point of the program
if __name__ == "__main__":
    run_demo()  # Run the demo function when the script is executed


# Output
# Allocate: O1 -> ITM1 (2)
# Failed: O2 -> ITM1 (4)
# Allocate: O3 -> ITM2 (1)
# Failed: O4 -> ITM999 (1)