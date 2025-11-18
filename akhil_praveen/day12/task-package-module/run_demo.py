# from csv_utils  import read_csv
# from validation import required_fields
from ust_tool_micro import (read_csv,required_fields)

try:
    
    orders_file,order_header = read_csv("/orders.csv")
    condition = required_fields(orders_file,order_header)
    
    
except Exception as e:
    print(e)