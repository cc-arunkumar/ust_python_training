from typing import List, Optional
from fastapi import FastAPI,HTTPException
import datetime

from pydantic import BaseModel

app=FastAPI(title="SpiceHub")
next_menu_id = 5
next_order_id = 1
class MenuItem(BaseModel):
    id: int
    name: str 
    category: str
    price: float 
    is_available: bool =False
    
class OrderItem(BaseModel):
    menu_item_id: int 
    quantity: int
    
class Order(BaseModel):
    id: int
    order_type: str
    table_number: int=None
    items: List[OrderItem]
    status: str="pending"
    special_instructions: str=None
menu = [
 {
 "id": 1,
 "name": "Tomato Soup",
 "category": "starter",
 "price": 99.0,
 "is_available": True
 },

 {
 "id": 2,
 "name": "Paneer Butter Masala",
 "category": "main_course",
 "price": 249.0,
 "is_available": True
 },
 {
 "id": 3,
 "name": "Butter Naan",
 "category": "main_course",
 "price": 49.0,
 "is_available": True
 },
 {
 "id": 4,
 "name": "Gulab Jamun",
 "category": "dessert",
 "price": 79.0,
 "is_available": False
 }
]
orders = [] 

headers=list(menu[0].keys())
@app.get("/menu")
def get_menu(only_available: Optional[bool]=False):
    
    if only_available:
        filtered_menu = [item for item in menu if item['is_available']]
    else:
        filtered_menu = menu

    return filtered_menu

@app.get("/menu/{id}")
def get_menu_by_id(id:int):
    for row in menu:
        if row['id']==id:
            return row
        raise HTTPException(status_code=404,detail="Menu item not found")

@app.post("/menu")
def read_menu(read:MenuItem):
    global next_menu_id
    for row in menu:
        if row[headers[0]]==read.id:
            raise HTTPException(status_code=404,detail="Menu item already exists")
    read.id=next_menu_id
    
    next_menu_id+=1
    menu.append(read)
    return read

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, update: MenuItem):
    for row in menu:
        if row["id"] == id:  
            row["name"] = update.name
            row["category"] = update.category
            row["price"] = update.price
            row["is_available"] = update.is_available
            return row  # Return the updated row from the menu
    raise HTTPException(status_code=404, detail="ID Not Found")

@app.delete("/menu/{id}",response_model=MenuItem)
def delete_menu(id:int):
    for i in range(len(menu)):
        if menu[i]["id"]==id:
            return menu.pop(i)
   
    raise HTTPException(status_code=404, detail="ID Not Found")

@app.post('/orders',response_model=Order)
def create_order(new_order:Order):
    new_list_id=[]
    for item in menu:
        new_list_id.append(item[headers[0]])
    for row in new_order.items:
        if row.quantity<=0:
            raise HTTPException(status_code=400,detail="Invalid Quantity")
        if row.menu_item_id not in new_list_id:
            raise HTTPException(status_code=404,detail="Menu Item not Found!")
        for item in menu:
            if row.menu_item_id == item[headers[0]] and not item[headers[4]]:
                raise HTTPException(status_code=400,detail="Item is Not Available!")
    
    global next_order_id
    if new_order.order_type == 'takeaway':
        new_order.id = next_order_id
        next_order_id += 1
        orders.append(new_order)
        return new_order
    elif new_order.order_type=='dine_in':
        if isinstance(new_order.table_number,int):
            new_order.id = next_order_id
            next_order_id += 1
            orders.append(new_order)  
            return new_order
        else:
            raise HTTPException(status_code=400,detail="Invalid Table Number")
    else:
        raise HTTPException(status_code=400,detail="Invalid Order Type")
@app.get("/orders",response_model=List[Order])
def get_orders(status:Optional[str]="pending"):
    if status is not None:
        new_order_list=[]
        for order in orders:
            if order.status==status:
                new_order_list.append(order)
        return new_order_list
    else:
        return orders

@app.get("/orders/{id}")
def get_order_id(id:int):
    for ord in orders:
        if ord.id == id:
            return ord
    raise HTTPException(status_code=404,detail="Order Not Found")

@app.patch('/orders/{id}/status')
def update_status(id: int, payload: dict):
    # find the order by id
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
   
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
   
    # validate payload has 'status'
    if not payload or "status" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'status' in request body")
   
    new_status = payload["status"]
    current_status = order_found.status
   
    # define allowed transitions
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }
   
    # validate transition is allowed
    if current_status not in allowed_transitions:
        raise HTTPException(status_code=400, detail=f"Unknown current status: {current_status}")
   
    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(status_code=400, detail=f"Cannot transition from '{current_status}' to '{new_status}'")
   
    # update status
    order_found.status = new_status
    return order_found

from typing import List
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
 
app=FastAPI(title="SpiceHub")
 
class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float
    is_available:bool
 
class OrderItem(BaseModel):
    menu_item_id:int
    quantity:int
 
class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str
    special_instructions: str = None
 
 
menu = [
 {
 "id": 1,
 "name": "Tomato Soup",
 "category": "starter",
 "price": 99.0,
 "is_available": True
 },
{
 "id": 2,
 "name": "Paneer Butter Masala",
 "category": "main_course",
 "price": 249.0,
 "is_available": True
 },
 {
 "id": 3,
 "name": "Butter Naan",
 "category": "main_course",
 "price": 49.0,
 "is_available": True
 },
 {
 "id": 4,
 "name": "Gulab Jamun",
 "category": "dessert",
 "price": 79.0,
 "is_available": False
 }
]
orders = [] # list of Order dicts
next_menu_id = 5
next_order_id = 1
 
 
@app.get('/menu')
def get_all_list_menu(only_available:bool = False):
    if not only_available:
        return menu
    else:
        new_li=[]
        for item in menu:
            if item['is_available'] == True:
                new_li.append(item)
        return new_li
 
@app.get('/men/{id}')
def get_menu_id(id:int):
    for li in menu:
        if li['id']==id:
            return li
    raise HTTPException(status_code=404,detail='Menu item not found')
 
@app.post('/menu',response_model=MenuItem)
def add_new_item(new_menu_item:MenuItem):
    global next_menu_id
    new_menu_item.id = next_menu_id
    next_menu_id += 1
    menu.append(new_menu_item)
    return new_menu_item
 
@app.put('/menu/{id}',response_model=MenuItem)
def update_menu_item(id:int,updated_item:MenuItem):
    for item in menu:
        if item['id']==id:
            item['name']=updated_item.name
            item['category']=updated_item.category
            item['price']=updated_item.price
            item['is_available']=updated_item.is_available
            return updated_item
    raise HTTPException(status_code=404,detail="Item Not Found!")
 
@app.delete('/menu/{id}')
def delete_item(id:int):
    for item in menu:
        if item['id'] == id:
            menu.pop(id-1)
            return {'details':'Menu item deleted'}
    raise HTTPException(status_code=404,detail="Menu Item Not Found")
 
@app.post('/orders',response_model=Order)
def create_order(new_order:Order):
    item_id_list =[]
    for item in menu:
        item_id_list.append(item['id'])
    for it in new_order.items:
        if it.quantity <=0:
            raise HTTPException(status_code=400,detail="Invalid Quantity")
        if it.menu_item_id not in item_id_list:
            raise HTTPException(status_code=404,detail="Menu Item not Found!")
        for item in menu:
            if it.menu_item_id == item['id'] and not item['is_available']:
                raise HTTPException(status_code=400,detail="Item is Not Available!")
 
    global next_order_id
    if new_order.order_type == 'takeaway':
        new_order.id = next_order_id
        next_order_id += 1
        orders.append(new_order)
        return new_order
    if new_order.order_type == 'dine_in':
        if isinstance(new_order.table_number,int):
            new_order.id = next_order_id
            next_order_id += 1
            orders.append(new_order)  
            return new_order
        else:
            raise HTTPException(status_code=400,detail="Invalid Table Number")
    else:
        raise HTTPException(status_code=400,detail="Invalid Order Type")
 
@app.get('/orders',response_model=List[Order])
def get_all_orders(status:str=None):
    if status is not None:
        new_pending_li = []
        for ord in orders:
            if ord.status ==status:
                new_pending_li.append(ord)
        return new_pending_li
    else:
        return orders
 
@app.get('/orders/{id}')
def get_order_id(id:int):
    for ord in orders:
        if ord.id == id:
            return ord
    raise HTTPException(status_code=404,detail="Order Not Found")
 
 
@app.patch('/orders/{id}/status')
def update_status(id: int, payload: dict):
    # find the order by id
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
   
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
   
    # validate payload has 'status'
    if not payload or "status" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'status' in request body")
   
    new_status = payload["status"]
    current_status = order_found.status
   
    # define allowed transitions
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }
   
    # validate transition is allowed
    if current_status not in allowed_transitions:
        raise HTTPException(status_code=400, detail=f"Unknown current status: {current_status}")
   
    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(status_code=400, detail=f"Cannot transition from '{current_status}' to '{new_status}'")
   
    # update status
    order_found.status = new_status
    return order_found
       
@app.get('/orders/{id}/total-amount')
def get_order_total(id: int):
    # find the order by id
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
   
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
   
    # compute total amount
    total_amount = 0.0
    for order_item in order_found.items:
        # find corresponding menu item
        menu_item = None
        for item in menu:
            if item['id'] == order_item.menu_item_id:
                menu_item = item
                break
       
        if menu_item is not None:
            # add line total (price * quantity) to total
            total_amount += menu_item['price'] * order_item.quantity
   
    return {
        "order_id": id,
        "total_amount": total_amount
    }
       
    

