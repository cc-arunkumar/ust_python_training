# run_demo.py
from ust_tools_micro.inventory import Inventory
from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int

def run_demo():
    inventory = Inventory.from_csv('data/inventory.csv')
    orders = read_csv('data/orders.csv')

    for order in orders:
        if not require_fields(order, ['order_id', 'item_id', 'quantity']):
            print(f"Invalid order: {order}")
            continue
        
        try:
            quantity=to_int(order['quantity'])
        except ValueError:
            print(f"Invalid order: {order}")
            continue
        
        if inventory.allocate(order['item_id'], quantity):
            print(f"Allocate: {order['order_id']} -> {order['item_id']} ({quantity})")
        else:
            print(f"Failed: {order['order_id']} -> {order['item_id']} ({quantity})")

if __name__=="__main__":
    run_demo()


# Output
# Allocate: O1 -> ITM1 (2)
# Failed: O2 -> ITM1 (4)
# Allocate: O3 -> ITM2 (1)
# Failed: O4 -> ITM999 (1)