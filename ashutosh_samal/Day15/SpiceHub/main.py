from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date,time

app = FastAPI(title="SpiceHub")

class Menuitem(BaseModel):
    id: int
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
    table_number: int | None = None
    items: List[OrderItem]
    status: str = "Pending"
    special_instructions: str | None = None

menu : List[Menuitem] = [
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

orders = []  # list of Order dicts
next_menu_id = 5
next_order_id = 1

@app.get("/Menu",response_model=List[Menuitem])
def get_menu(is_available: bool | None = None):
    if is_available:
        return [odr for odr in menu if odr['is_available'] == True]
    return menu

@app.get("/Menu/{id}")
def get_menu(id:int):
    try:
        for odr in menu:
            if odr["id"] == id:
                return odr
    except IndexError:
        raise HTTPException(status_code=404,detail="Menu item not found")

@app.post("/Menu")
def add_menu(odr:Menuitem):
    global next_menu_id
    odr.id = next_menu_id
    next_menu_id += 1
    menu.append(odr.model_dump())
    
@app.put("/Menu/{id}")
def update(id: int, odr: Menuitem):
    for e in menu:
        if e["id"] == id:
            e.update({
                "id": e.id,
                "name": e.name,
                "category": e.category,
                "price": e.price, 
                "is_available": e.is_available
            })
            return e
    raise HTTPException(status_code=404, detail="Item does not exist")

@app.delete("/Menu/{id}")
def delete_item(id:int):
    for e in menu:
        if e['id']==id:
            menu.remove(e)
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404,detail="Item not found")


@app.post("/orders", status_code=201)
def create_order(order: Order):
    global next_order_id

    for order_item in order.items:
        menu_item = next((item for item in menu if item["id"] == order_item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item with id {order_item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    if order.order_type == "dine_in" and (order.table_number is None or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number is required for dine-in orders")
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number should be null for takeaway orders")

    order.id = next_order_id
    next_order_id += 1
    orders.append(order.model_dump())
    return order


@app.get("/Order")
def get_order():
    return orders

@app.get("/Orders/{id}")
def get_order(id:int):
    for odr in orders:
        if odr["id"] == id:
            return odr
    raise HTTPException(status_code=404,detail="Order not found")

@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: str):
    valid_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"]
    }

    for order in orders:
        if order["id"] == id:
            if order["status"] == "completed" or order["status"] == "cancelled":
                raise HTTPException(status_code=400, detail="Cannot change status after completion or cancellation")
            if status not in valid_transitions.get(order["status"], []):
                raise HTTPException(status_code=400, detail="Invalid status transition")
            order["status"] = status
            return order
    raise HTTPException(status_code=404, detail="Order not found")


@app.get("/orders/{id}/total-amount")
def calculate_total(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    total_amount = 0
    for item in order["items"]:
        menu_item = next((menu_item for menu_item in menu if menu_item["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item with id {item.menu_item_id} not found")
        total_amount += menu_item["price"] * item.quantity

    return {"order_id": id, "total_amount": total_amount}





