import sys
import os
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

from ust_tools_micro.csv_utils import csv_reader
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.validators import require_fields,to_int

path1 = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day12\data\orders.csv"
path2 = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day12\data\inventory.csv"

def run_demo():
    # Load inventory and orders from CSV
    inventory = Inventory.from_csv(path2)
    orders = csv_reader(path1)

    for order in orders:
        # Validate required fields in each order
        if not require_fields(order, ['order_id', 'item_id', 'quantity']):
            print(f"INVALID ORDER: {order}")
            continue
        
        # Convert quantity to integer
        try:
            quantity = to_int(order['quantity'])
        except ValueError:
            print(f"INVALID ORDER: {order}")
            continue

        # Attempt to allocate stock
        if inventory.allocate(order['item_id'], quantity):
            print(f"ALLOCATED: {order['order_id']} -> {order['item_id']} ({quantity})")
        else:
            print(f"FAILED: {order['order_id']} -> {order['item_id']} ({quantity})")


if __name__ == "__main__":
    run_demo()
    

#Sample Output
# ALLOCATED: O1 -> ITM1 (2)
# FAILED: O2 -> ITM1 (4)
# ALLOCATED: O3 -> ITM2 (1)
# FAILED: O4 -> ITM999 (1)
 