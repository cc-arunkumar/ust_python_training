from ust_tools_micro import (read_csv, write_csv, require_fields, to_int, Inventory)


path = "C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/data"

load_orders = read_csv(path+"/orders.csv")
load_inventory = read_csv(path+"/inventory.csv")

inventory_obj = Inventory()
inventory_obj.from_csv(path+"/inventory.csv")

field = ["order_id","item_id","quantity"]
for data in load_orders:
    if(require_fields(data,field)):
        if(to_int(data["quantity"])):
            data["quantity"]=to_int(data["quantity"])
            if(inventory_obj.allocate(data["item_id"],data["quantity"])):
                data["quantity"]+=int(inventory_obj.datas[data["item_id"]])
                print(f"ALLOCATED: -> {data}")
            else:
                print(f"FAILED: -> {data}")
    else:
        print(f"INVALID ORDER: -> {data}")
        