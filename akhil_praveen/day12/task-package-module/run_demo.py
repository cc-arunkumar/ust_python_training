# from csv_utils  import read_csv
# from validation import required_fields
from ust_tool_micro import (read_csv,required_fields,Inventory)
current = "C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/task-package-module/data"

inventory_obj = Inventory()

try:
    
    orders_file,order_header = read_csv(current+"/orders.csv")
    inventory_obj.from_csv(current+"/inventory.csv")
    for row in orders_file: 
        condition = required_fields(row,order_header)
        if condition:
            inventory_obj.allocate(row[order_header[1]],int(row[order_header[2]]))

except Exception as e:
    print(str(e))