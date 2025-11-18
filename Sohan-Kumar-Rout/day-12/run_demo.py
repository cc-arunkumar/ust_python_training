from ust_tools_micro import read_csv, require_fields
from ust_tools_micro import to_int, Inventory

def main():
    inventory = Inventory.from_csv("data/inventory.csv")

    orders = read_csv("data/order.csv")

    for order in orders:
        if not require_fields(order, ["order_id", "item_id", "quantity"]):
            print(f"Invalid quantity: {order}")
            continue

        try:
            qty = to_int(order["quantity"])
        except ValueError:
            print(f"Invalid quantity: {order}")
            continue

        order_id = order["order_id"]
        item_id = order["item_id"]

        if inventory.allocate(item_id, qty):
            print(f"Allocated: {order_id} -> {item_id} ({qty})")
        else:
            print(f"Failes: {order_id} -- {item_id} ({qty})")

if __name__ == "__main__":
    main()
    
#Output
# Allocated: O1 -> ITM1 (2)
# Failes: O2 -- ITM1 (4)
# Allocated: O3 -> ITM2 (1)
# Failes: O4 -- ITM999 (1)
