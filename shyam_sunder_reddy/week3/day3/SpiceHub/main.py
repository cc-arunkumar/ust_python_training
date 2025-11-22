from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel

app=FastAPI(title="Spice Hub")

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
    id:int
    order_type:str
    table_number:int=None
    items:List[OrderItem]
    status:str="pending"
    special_instruction:str="Nothing"

menu=[
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

orders:List[Order]=[]
next_menu_id = 4
next_order_id=0

# LEVEL 1 – Menu CRUD
#For giving the whole menu
@app.get("/menu",response_model=List[MenuItem])
def display_all(flag:bool=False):
    if flag:
        new_li=[]
        for item in menu:
            if item["is_available"]==True:
                new_li.append(item)
        return new_li
    return menu

@app.get("/menu/{id}",response_model=MenuItem)
def search_byid(id:int):
    for item in menu:
        if item["id"]==id:
            return item
    raise HTTPException(status_code=404,detail="Menu item not found")

@app.post("/menu",response_model=MenuItem)
def create_new_item(new_item:MenuItem):
    global next_menu_id
    next_menu_id+=1
    new_item.id=next_menu_id
    menu.append(new_item.dict())
    return new_item

@app.put("/menu/{id}",response_model=MenuItem)
def updating_byid(id:int,new_item:MenuItem):
    for item in menu:
        if item["id"]==id:
            item["name"]=new_item.name
            item["category"]=new_item.category
            item["price"]=new_item.price
            item["is_available"]=new_item.is_available
            return item
    raise HTTPException(status_code=404,detail="item does not exist")

@app.delete("/menu/{id}")
def deleting_byid(id:int):
    for item in menu:
        if item["id"]==id:
            menu.remove(item)
            return {"detail":"Menu item deleted"}
    raise HTTPException(status_code=404,detail="Employee ID Not Found")

#LEVEL 2
@app.post("/orders",response_model=Order)
def creating_order(new_order:Order):
    global next_order_id
    next_order_id+=1
    
    if new_order.order_type=="dine_in" :
        if new_order.table_number is None or new_order.table_number<=0 :
            raise HTTPException(status_code=400,detail="table number cannot be negative")
    
    for order_item in new_order.items:
        if order_item.quantity<=0:
                 raise HTTPException(status_code=400, detail="Quantity must be positive")
        if not any(m["id"] == order_item.menu_item_id for m in menu):
            raise HTTPException(status_code=400, detail="Item not in menu")
    
    new_order.id=next_order_id
    orders.append(new_order)
    return new_order

@app.get("/orders",response_model=List[Order])
def display_orders(stat:str=None):
    if stat is None:
        return orders
    new_li=[]
    for order in orders:
        if order["status"]==stat:
            new_li.append(order)
    return new_li

@app.get("/orders/{id}",response_model=Order)
def display_specific_order(id:int):
    for order in orders:
        if order.id==id:
            return order
    raise HTTPException(status_code=404,detail="Order not Found")

# LEVEL 3 – Order status + total (small but realistic)
@app.patch("/orders/{id}/status",response_model=Order)
def update_status(id:int,change:str):
    for order in orders:
        if order.id==id:
            s=order.status
            if change == "cancelled":
                order.status = "cancelled"
            elif s == "pending" and change == "in_progress":
                order.status = "in_progress"
            elif s == "in_progress" and change == "completed":
                order.status = "completed"
            else:
                raise HTTPException(status_code=400, detail="Illegal transition")
            return order
    raise HTTPException(status_code=404,detail="Order Not Found")

@app.get("/orders/{id}/total-amount-compute")
def get_total_bill(id:int):
    for order in orders:
        if order.id==id:
            sum=0
            for order_item in order.items:
                for menu_item in menu:
                    if menu_item["id"]==order_item.menu_item_id:
                        sum+=(menu_item["price"]*order_item.quantity)
            return {"order_id":id,"total_amount":sum}
    
    raise HTTPException(status_code=404,detail="Order Not Found")
