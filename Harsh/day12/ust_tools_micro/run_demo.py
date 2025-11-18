from ust_tools_micro.csv_utils import read_csv
from ust_tools_micro.validators import require_fields, to_int
from ust_tools_micro.inventory import Inventory

def main():
    # Load inventory
    inventory = Inventory.from_csv("C:/Users/Administrator/Desktop/Training/ust_python_training/harsh/day12/data/inventory.csv")
    orders = read_csv("C:/Users/Administrator/Desktop/Training/ust_python_training/harsh/day12/data/orders.csv")

    
    for order in orders:
        # Validate required fields
        if not require_fields(order, ["order_id", "item_id", "quantity"]):
            print(f"INVALID ORDER: {order}")
            continue
        
        # Convert quantity to integer
        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print(f"INVALID QUANTITY: {order}")
            continue
        
        item_id = order["item_id"]
        order_id = order["order_id"]
        
        # Try to allocate stock
        if inventory.allocate(item_id, qty):
            print(f"ALLOCATED: {order_id} - {item_id} ({qty})")
        else:
            print(f"FAILED: {order_id} - {item_id} ({qty})")

if __name__ == "__main__":
    main()
