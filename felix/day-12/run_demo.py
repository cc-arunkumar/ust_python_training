from ust_tools_micro import (
    csv_utils,
    validators,
    inventory
)

# File paths for inventory and orders CSV files
inventory_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-12/data/inventory.csv"
orders_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-12/data/orders.csv"

# Fields that must be present in each order row
required_fields = ["order_id", "item_id", "quantity"]

# Read orders CSV
data = csv_utils.read_csv(orders_path)

# Validate required fields and convert quantity to integer
for row in data:
    check = validators.required_fields(row, required_fields)

    if check:
        # Convert quantity to int for all items
        for item in data:
            if type(validators.to_int(item["quantity"])) == int:
                # Updating quantity value as integer
                item["quantity"] = validators.to_int(item["quantity"])
    else:
        # If required fields missing in any row
        print(f"INVALID ORDER: {data}")

# Read inventory CSV
inventory_data = csv_utils.read_csv(inventory_path)

# Allocate inventory for each order
for order in data:
    flag = 0  # Flag to track allocation success

    for inv in inventory_data:
        # Try allocating quantity from inventory
        if inventory.Inventory(inv).allocate(inv["item_id"], order["quantity"]):
            flag = 1
            # Print allocation success
            print(f"ALLOCATED : {order['order_id']} -> {inv['item_id']}")
            break

    # If allocation failed for the order
    if flag == 0:
        print(f"FAILED : {order['order_id']} -> {inv['item_id']}")
