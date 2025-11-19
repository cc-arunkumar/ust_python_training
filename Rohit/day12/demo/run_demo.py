import os 
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import required_fileds,to_int

inventory_path = os.path.join(BASE_DIR, 'data', 'inventory.csv')
order_path = os.path.join(BASE_DIR, 'data', 'order.csv')

def run_demo():
    inv = Inventory.from_csv(inventory_path)
    print("Initial stock:", inv.items)

    orders = read_csv(order_path)
    if not required_fileds(orders, ['item_id', 'quantity']):
        print("Order data is missing required fields.")
        return

    for order in orders:
        order_id = order.get("order_id")
        item_id = order.get("item_id")
        qty = to_int(order.get("quantity", "0"))
        
        if qty is None:
            print(f"Invalid quantity for order {order_id}. Skipping.")
            continue
        if inv.allocate(item_id, qty):
            print(f"Order {order_id} for item {item_id} of quantity {qty} allocated successfully.")
        else:
            print(f"Order {order_id} for item {item_id} of quantity {qty} could not be allocated due to insufficient stock.")
            
            
if __name__ == "__main__":
    run_demo()