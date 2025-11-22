from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="SpiceHub")

class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float
    is_available:bool = True
    
class MenuItemCreate(BaseModel):
    name:str
    category:str
    price:float
    is_available:bool = True
    
class OrderItem(BaseModel):
    menu_item_id:int
    quantity:int
    
class Order(BaseModel):
    id:int
    order_type:str
    table_no:int
    items:List[OrderItem]
    status:str = "pending"
    special_instructions:str = None
    
class OrderCreate(BaseModel):
    order_type:str
    table_no:int
    items:List[OrderItem]
    status:str = "pending"
    special_instructions:str = None

class Status(BaseModel):
    status:str
    
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

@app.get("/menu-list")
def menu_list(only_available:bool = False):
    menu_items = []
    if only_available:
        for i in menu:
            if i["is_available"]:
                menu_items.append(i)
        return menu_items
    return menu

@app.get("/menu/{id}")
def single_item(id:int):
    for i in menu:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404,detail="Menu item not found")
        
@app.post("/menu")
def add_new_menu_item(menu_item:MenuItemCreate):
    global next_menu_id
    item = MenuItem(
        id=next_menu_id,
        name=menu_item.name,
        category = menu_item.category,
        price=menu_item.price,
        is_available=menu_item.is_available
    )
    menu.append(item.__dict__)
    next_menu_id += 1
    return item

@app.put("/menu/{id}")
def update_menu_item(id:int,menu_item:MenuItemCreate):
    item = MenuItem(
        id=id,
        name=menu_item.name,
        category = menu_item.category,
        price=menu_item.price,
        is_available=menu_item.is_available
    )
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            menu[i] = item.__dict__
            return {"updated: ":menu[i]}
    raise HTTPException(status_code=404,detail="Item not found")

@app.delete("/menu/{id}")
def delete_item(id:int):
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            return menu.pop(i)
    raise HTTPException(status_code=404,detail="Item not found")


@app.post("/orders")
def new_order(order:OrderCreate):
    order_item = order.__dict__
    for i in order_item["items"]:
        if i.quantity<=0:
            raise HTTPException(status_code=400,detail="Quantity is 0")
        for j in menu:
            if j["id"] == i.menu_item_id and j["is_available"] == False:
                raise HTTPException(status_code=400,detail="Item not available")

    global next_order_id
    final = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_no=order.table_no,
        items=order.items,
        status=order.status,
        special_instructions=order.special_instructions
    )
    orders.append(final.__dict__)
    next_order_id += 1
    return {"Item ordered":orders}

@app.get("/orders-list")
def order_list(status:str = "optional"):
    if status == "optional":
        return orders
    else:
        ord = []
        for i in orders:
            if i["status"] == status:
                ord.append(i)
        if ord:
            return ord
    raise HTTPException(status_code=404,detail="No orders found")

@app.get("/order/{id}")
def get_an_order(id:int):
    for i in orders:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404,detail="Order not found")

@app.patch("/order/{id}/status")
def status(id:int,stat:Status):
    for i in orders:
        if i["id"] == id:
            i["status"] = stat.__dict__["status"]
    return stat.__dict__

@app.get("/order/{id}/total-amount")
def total_amount(id:int):
    total = 0
    for i in orders:
        if i["id"] == id:
            for j in i["items"]:
                for k in menu:
                    if j.menu_item_id == k["id"]:
                        total += k["price"] * j.quantity
    if total>0:
        return {"order ID":id,"totla amount":total}
    else:
        raise HTTPException(status_code=404,detail="No order Found")
            
            
        
        
    