from ust_tools_micro import csv_utils

inventory_file_path="task1_custom_packages/data/inventory.csv"
orders_file_path="task1_custom_packages/data/orders.csv"


readed_list=csv_utils.read_csv(orders_file_path)
print(readed_list)
