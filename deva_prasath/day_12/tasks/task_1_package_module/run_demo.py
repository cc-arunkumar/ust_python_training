import sys
import os
#importing from other files
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.validators import require_fields,to_int


#to know the current directory
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
#defining paths
path1 = r"deva_prasath\day_12\data\orders.csv"
path2 = r"deva_prasath\day_12\data\inventory.csv"

def run_demo():
    # Load inventory and orders from CSV
    inventory = Inventory.from_csv(path2)
    orders = read_csv(path1)
    for order in orders:
        # Validate required fields in each order
        if not require_fields(order,['order_id','item_id','quantity']):
            print(f"INVALID ORDER:{order}")
            continue
        # Convert quantity to integer
        try:
            quantity = to_int(order['quantity'])
        except ValueError:
            print(f"INVALID ORDER:{order}")
            continue
        # Attempt to allocate stock
        if inventory.allocate(order['item_id'],quantity):
            print(f"ALLOCATED:{order['order_id']}->{order['item_id']}({quantity})")
        else:
            print(f"FAILED:{order['order_id']}->{order['item_id']}({quantity})") 
if __name__ == "__main__":
    run_demo()
 