inventorypath="D:/ust_python_training/arun_reddy/day12/data/inventory.csv"
orderspath="D:/ust_python_training/arun_reddy/day12/data/orders.csv"

from ust_tools_micro import(
    read_csv,
    Inventory,
    write_csv,
    require_fields,
    to_int
)
content=read_csv(orderspath)
inventorylis=read_csv(inventorypath)  
required_fields=["order_id","item_id","quantity"]
for item in content:
    valid=require_fields(item,required_fields)
    if valid:
        print("All the items are present")
    else:
        print("Invalid Items")
allocatedlist=[]
failedlist=[]
it=Inventory(inventorylis)
for item in content:
    if it.allocate(item["item_id"],int(item["quantity"])):
        allocatedlist.append(item)
    else:
        failedlist.append([item,"Invalid Order"])

print(f"allocatedlist:{len(allocatedlist)}")
print(f"failedlsit:{len(failedlist)}")
for item in failedlist:
    print(item)
    
    
#sample execution
# All the items are present
# All the items are present
# All the items are present
# All the items are present
# allocatedlist:2
# failedlsit:2
# [{'order_id': 'O2', 'item_id': 'ITM1', 'quantity': '4'}, 'Invalid Order']
# [{'order_id': 'O4', 'item_id': 'ITM999', 'quantity': '1'}, 'Invalid Order']