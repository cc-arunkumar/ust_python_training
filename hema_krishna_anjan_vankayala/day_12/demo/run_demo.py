
from ust_tools_micro import read_csv,write_csv,require_fields ,to_int, Inventory

orders_list = []
orders_list = read_csv('data/orders.csv')

inventory_list= []
inventory_list = read_csv('data/inventory.csv')
allocated_list = []
failed_list = []
new_updated_inventory=[]
req_fields = ['order_id' , 'item_id' , 'quantity']

for order in orders_list:
    if require_fields(order,req_fields):
        try:
            quantity  = to_int(order['quantity'])
        except Exception:
            print(f'Invalid Quantity in {order['order_id']} Order ID')
            failed_list.append(order)
            continue
        
        li = Inventory.from_csv('data/inventory.csv',order['item_id'])
        flag = li[0]
        invent = li[1]
        if flag:
            if invent.allocate(order['item_id'],int(order['quantity'])):
                li=read_csv('data/inventory.csv')
                for row in li:
                    if invent['item_id'] == li['item_id']:
                        li['available_stock'] = invent['available_stock']
                write_csv()
                # dic = [invent.__dict__]
                # headers = ['item_id','available_stock']
                # write_csv('data/inventory.csv',dic,headers)
                allocated_list.append(order) 
            else:
                failed_list.append(order)
        else:
            failed_list.append(order)
            print('Invalid Item',order['item_id'])
    else:
        print(f"Req Field is Missing in {order['order_id']}")
print(failed_list)
print(allocated_list)
            
                
            
            
        
        
        
        