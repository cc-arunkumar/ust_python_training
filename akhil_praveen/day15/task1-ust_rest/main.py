from typing import List,Optional
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI(title="Spice Up")

class MenuItem(BaseModel):
    id: int 
    name: str 
    category: str
    price: float 
    is_available: bool = True
    
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
    menu_item_id : int
    quantity : int
    
class Order(BaseModel):
    id: int 
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str  = "pending"
    special_instructions: str = None
    
class CreateOrder(BaseModel):
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    special_instructions: str = None
    
menu = [
 {
 "id": 1,
 "name": "Tomato Soup",
 "category": "starter",
 "price": 99.0,
 "is_available": True
 },{
 "id": 2,
 "name": "Paneer Butter Masala",
 "category": "main_course",
 "price": 249.0,
 "is_available": True},
{
 "id": 3,
 "name": "Butter Naan",
 "category": "main_course",
 "price": 49.0,
 "is_available": True
 },
{ "id": 4,
 "name": "Gulab Jamun",
 "category": "dessert",
 "price": 79.0,
 "is_available": False}

 ]
orders = [{
        "id":1,
        "order_type": "dine_in",
        "table_number": 12,
        "items": [
        { "menu_item_id": 1, "quantity": 2 },
        { "menu_item_id": 3, "quantity": 4 }
        ],
        "status": "pending",
        "special_instructions": "less spicy"}
          ] 
next_menu_id = 5
next_order_id = 2

@app.post("/menu")
def add_menu_item(item:CreateMenu):
    global next_menu_id
    new_item = MenuItem(
        id=next_menu_id,
        name=item.name,
        category=item.category,
        price=item.price,
    )
    menu.append(new_item)
    next_menu_id+=1
    return new_item

@app.get("/menu")
def get_all_menu_details(is_avail:Optional[bool] = False):
    temp_menu = []
    if is_avail==False:
        return menu
    for item in menu:
        if item["is_available"]==True:
            temp_menu.append(item)
    return temp_menu

@app.get("/menu/{id}",response_model=MenuItem)
def get_menu_byid(id:int):
    
    for item in menu:
        if item["id"]==id:
            return item
    raise HTTPException(status_code=404,detail="Id not found")

@app.put("/menu/{id}")
def update_menu(id:int,item :UpdateMenu):
    updated = get_menu_byid(id)
    if updated:
        new_menu = MenuItem(
        id=id,
        name=item.name,
        category=item.category,
        price=item.price,
        is_available=item.is_available
    )
    for i in range(len(menu)):
        if menu[i]["id"]==id:
            menu[i]= new_menu
            return new_menu
    raise HTTPException(status_code=404,detail="menu not found")

@app.delete("/menu/{id}",response_model=MenuItem)
def delete_student(id:int):
    for i in range(len(menu)):
        if menu[i]["id"]==id:
            removed = menu.pop(i)
            return removed
    raise HTTPException(status_code=404,detail="Menu not found")

@app.post("/orders")
def add_order_item(item:CreateOrder):
    global next_order_id
    if item.order_type == "dine_in" and item.table_number==0:
        raise HTTPException(status_code=400,detail="For dine in , Table should be placed")
    elif item.order_type == "takeaway" and item.table_number>0:
        raise HTTPException(status_code=400,detail="For takeaway , No Table should be placed")
    
    for data in item.items:
        if (get_menu_byid(data.menu_item_id)["is_available"]):
            pass
        else:
            raise HTTPException(status_code=400,detail="Invalid menu item")
    
    new_item = Order(
        id=next_order_id,
        order_type=item.order_type,
        table_number=item.table_number,
        items=item.items,
        special_instructions=item.special_instructions
    )
    orders.append(new_item)
    next_order_id+=1
    return new_item

@app.get("/order")
def get_all_order_details(status:Optional[str] = None):
    temp_orders = []
    if status==None:
        return orders
    for item in orders:
        if item["status"]==status:
            temp_orders.append(item)
    return temp_orders

@app.get("/order/{id}")
def get_order_details(id:int):
    for item in orders:
        if item["id"]==id:
            return item
    raise HTTPException(status_code=404,detail="Order not found")

@app.patch("/order/{id}/status")
def get_order_details(id:int,status:str):
    for item in orders:
        if item["id"]==id:
            if item["status"] == "completed":
                raise HTTPException(status_code=400,detail="Order is already completed")
            elif item["status"] == "cancelled":
                raise HTTPException(status_code=400,detail="Order is already cancelled")
            elif item["status"] == "pending" and status != "completed":
                item["status"]=status
                    
            elif item["status"] == "in_progress" and status != "pending":
                item["status"] = status
            else:
                raise HTTPException(status_code=400,detail="Invalid status")
            return item
    raise HTTPException(status_code=404,detail="Order not found")

@app.get("/orders/{id}/total-amount")
def compute_bill(id:int):
    total = 0
    for item in orders:
        if item["id"]==id:
            for each_items in item["items"]:
                price=0
                for each_menu_items in menu:
                    if each_menu_items["id"]==each_items["menu_item_id"]:
                        price = each_menu_items["price"]
                total+= each_items["quantity"]*price
        return {"order_id":id,"Total":total}
    raise HTTPException(status_code=404,detail="Order not found")