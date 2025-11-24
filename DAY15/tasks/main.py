from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI(title="SpiceHub")


class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float
    is_available:bool=True

class MenuCreate(BaseModel):
    name:str
    category:str
    price:float
    is_available:bool=True

class OrderItem(BaseModel):
    menu_item_id:int
    quantity:int

class Order(BaseModel):
    id:int
    order_type:str
    table_number: int | None
    items:list[OrderItem]
    status:str
    special_instructions: str |None
    
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
next_menu_id = len(menu)+1
next_order_id = 1

@app.get("/menu", response_model=list[MenuItem])
def get_menu(avai:bool):
    if avai:
        return [item for item in menu if item["is_available"]]
    
    return menu


@app.get("/menu/{item_id}",response_model=MenuItem)
def get_menuitem(item_id:int):
    for item in menu:
        if item["id"]==item_id:
            return item
    
    raise HTTPException (404, "Menu not found")

@app.post("/menu",response_model=MenuItem,status_code=201)
def add_menu(item: MenuCreate):
    global next_menu_id
    
    added_item={
        "id":next_menu_id,
        "name":item.name,
        "category":item.category,
        "price":item.price,
        "is_available":item.is_available        
    }
    
    menu.append(added_item)
    next_menu_id+=1
    return added_item


@app.put("/menu/{item_id}",response_model=MenuItem)
def update_menu(item_id:int, item:MenuCreate):
    for i in menu:
        if i["id"]==item_id:
            i["name"]=item.name
            i["category"]=item.category
            i["price"]=item.price
            i["is_available"]=item.is_available
            return i
    raise HTTPException(404, "Menu Item not found")
            

@app.delete("/menu/{item_id}")
def delete_item(item_id:int):
    for item in menu:
        if item["id"]==item_id:
            menu.remove(item)
            return {"detail":"Menu item deleted"}
    
    raise HTTPException(404, "No items found")


@app.post("/orders",response_model=Order,status_code=201)
def create_order(order:Order):
    global next_order_id
    
    if order.order_type not in ["dine_in","takeaway"]:
        raise HTTPException(400,"Invalid order type")
    
    if order.order_type=="dine_in" and (order.table_number is None or order.table_number<=0):
        raise HTTPException(400,"Table number required for dine in")
    
    if order.order_type=="takeaway" and order.table_number not in [None,0]:
        raise HTTPException(400,"Table number must be null for takeaway")
    
    for i in order.items:
        if i.quantity<=0:
            raise HTTPException(400,"Quantity must be greater than zero")
        
        found=False
        for m in menu:
            if m["id"]==i.menu_item_id:
                found=True
                if not m["is_available"]:
                    raise HTTPException(400,"Item not available")
        if not found:
            raise HTTPException(400,"Menu item not found")
    
    new_order={
        "id":next_order_id,
        "order_type":order.order_type,
        "table_number":order.table_number,
        "items":order.items,
        "status":"pending",
        "special_instructions":order.special_instructions
    }
    
    orders.append(new_order)
    next_order_id+=1
    return new_order


@app.get("/orders")
def get_orders(status:str=None):
    if status:
        return [o for o in orders if o["status"]==status]
    return orders


@app.get("/orders/{order_id}")
def get_single_order(order_id:int):
    for o in orders:
        if o["id"]==order_id:
            return o
    raise HTTPException(404,"Order not found")


@app.patch("/orders/{order_id}/status")
def update_status(order_id:int, status:str):
    for o in orders:
        if o["id"]==order_id:
            current=o["status"]
            
            if current in ["completed","cancelled"]:
                raise HTTPException(400,"No further changes allowed")
            
            if current=="pending" and status not in ["in_progress","cancelled"]:
                raise HTTPException(400,"Invalid status change")
            
            if current=="in_progress" and status not in ["completed","cancelled"]:
                raise HTTPException(400,"Invalid status change")
            
            o["status"]=status
            return o
            
    raise HTTPException(404,"Order not found")


@app.get("/orders/{order_id}/total-amount")
def total_amount(order_id:int):
    for o in orders:
        if o["id"]==order_id:
            total=0
            for i in o["items"]:
                for m in menu:
                    if m["id"]==i.menu_item_id:
                        total+=m["price"]*i.quantity
            return {"order_id":order_id,"total_amount":total}
    raise HTTPException(404,"Order not found")