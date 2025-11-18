from ust_tools_micro import(
    csv_utils,
    validators,
    inventory
)

inventory_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix\day-12/data/inventory.csv"
orders_path = "C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-12/data/orders.csv"

required_fields = [ "order_id" , "item_id" , "quantity"]

data = csv_utils.read_csv(orders_path)

for i in data:
    check = validators.required_fields(i,required_fields)

    if check:
        for item in data:
            if type(validators.to_int(item["quantity"])) == int:
                item["quantity"] = validators.to_int(item["quantity"])
                # print("Quantity type changed")
    else:
        print(f"INVALID ORDER: {data}")

inventory_data = csv_utils.read_csv(inventory_path)

for item in data:
    flag = 0
    for i in inventory_data:
        if inventory.Inventory(i).allocate(i["item_id"],item["quantity"]):
            flag=1
            # inventory.Inventory(item).release(i["quantity"])
            print(f"ALLOCATED : {item["order_id"]} -> {i["item_id"]}")
            break
    if flag==0:
        print(f"FAILD : {item["order_id"]} -> {i["item_id"]}")
    
    

