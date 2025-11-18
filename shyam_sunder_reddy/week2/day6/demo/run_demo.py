from ust_tools_micro import csv_utils,inventory,validators
import os,csv

data=csv_utils.read_csv(os.getcwd()+"/data/orders.csv")
# print(data)

invent=csv_utils.read_csv(os.getcwd()+"/data/inventory.csv")
# print(invent)

order_data={}
for row in data:
    ord=validators.Order(row)
    if not ord.validate_order():
        print("Invalid Order:",ord.order_id)
    else:
        order_data[ord.order_id]=ord

inventory_data={}
for row in invent:
    ini=inventory.Inventory(row)
    inventory_data[ini.item_id]=ini
    
for key,value in order_data.items():
    x=value.item_id    
    if x in inventory_data:
        for d,b in inventory_data.items():
            if d==x :
                if b.allocate(d,value.quantity):
                    print(f"ALLOCATED: {key} -> {d} {value.quantity}")
                else:
                    print(f"FAILED: {key} -> {d} {value.quantity}")
    else:
        print("Item doesnt Exist")

# csv_utils.write_csv(os.getcwd()+"/data/inventory.csv",inventory_data.values())