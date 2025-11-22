from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional
from datetime import date,datetime,time

app = FastAPI(title="SpiceHub")

menu_list = [
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


class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool =True

class CreateMenu(BaseModel):
    name: str
    category: str
    price: float

class UpdateMenu(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool 


class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str = "pending" 
    special_instructions: str = None

class CreateOrder(BaseModel):
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    special_instructions: str = None

@app.post("/menu",response_model=MenuItem)
def add_menu_item(menu:CreateMenu):
    
    global next_menu_id
    
    new_menu = MenuItem(id=next_menu_id,
                       name=menu.name,
                       category=menu.category,
                       price=menu.price
                            )
    menu_list.append(new_menu.__dict__)
    next_menu_id+=1
    return new_menu

@app.get("/menu",response_model=List[MenuItem])
def get_all_menu_items(is_available:Optional[bool]=False):
    true_list=[]
    if(is_available==False):
        return menu_list
    for data in menu_list:
        if(data["is_available"]==is_available):
            true_list.append(data)

    return true_list

@app.get("/menu/{id}",response_model=MenuItem)
def get_menu_item_by_id(id:int):
    for data in menu_list:
        if(data["id"]==id):
            return data
    
    raise HTTPException(status_code=404,detail="Menu Not Found")

@app.put("/menu/{id}",response_model=MenuItem)
def update_menu(id:int,update_menu:UpdateMenu):
    updated = get_menu_item_by_id(id)
    if(updated):
        new_changes = MenuItem(
            id=id,
            name=update_menu.name,
            category=update_menu.category,
            price=update_menu.price,
            is_available=update_menu.is_available
        )
        for i in range(len(menu_list)):
            if(menu_list[i]["id"]==id):
                menu_list[i]=new_changes.__dict__
                return new_changes
    else:
        raise HTTPException(status_code=404,detail="Not Found")
    
@app.delete("/menu/{id}",response_model=MenuItem)
def delete_menu(id:int):
    if(get_menu_item_by_id(id)):
        return menu_list.pop(id-1)
    else:
        raise HTTPException(status_code=404,detail="Not Found")
    
@app.post("/order",response_model=Order)
def add_order(order:CreateOrder):
    if(order.order_type=="dine_in" and order.table_number<=0):
        raise HTTPException(status_code=400,detail="Not valid")
    if(order.order_type=="take_away" and order.table_number>0):
        raise HTTPException(status_code=400,detail="Not valid")
    for data in order.items:
        if(get_menu_item_by_id(data.menu_item_id)["is_available"]):
            pass
        else:
            raise HTTPException(status_code=400,detail="Not valid")
    global next_order_id
    new_order = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_number=order.table_number,
        items=order.items,
        special_instructions=order.special_instructions
    )
    orders.append(new_order.__dict__)
    next_order_id+=1
    return new_order

@app.get("/orders",response_model=List[Order])
def get_all_orders(status:Optional[str]="pending"):
    lis=[]
    for data in orders:
        if(data["status"]==status):
            lis.append(data)
    return lis

@app.get("/orders/{id}",response_model=Order)
def get_orders(id:int):
    for data in orders:
        if(data["id"]==id):
            return data
    raise HTTPException(status_code=404,detail="Not Found")

@app.patch("/orders/{id}/status",response_model=Order)
def update_status(id:int,status:str):
    if(get_orders(id)):
        for i in range(len(orders)):
            if(orders[i]["id"]==id):
                if(orders[i]["status"]=="pending" and status!="completed"):
                    orders[i]["status"]=status
                elif(orders[i]["status"]=="in_progress" and status!="in_progress"):
                    orders[i]["status"]=status
                else:
                    if(orders[i]["status"] in ["completed","cancelled"]):
                        raise HTTPException(status_code=400,detail="Already completed Order" if orders[i]["status"]=="completed" else "Already Cancelled")
        return get_orders(id)
    
@app.get("/orders/{id}/totalamount")
def calculate_total(id:int):
    if(get_orders(id)):
        data = get_orders(id)
        total=0
        for row in data["items"]:
            menu = get_menu_item_by_id(row.menu_item_id)
            total+=row.quantity*menu["price"]
        return {"Total Bill" :total}
    
                

        


