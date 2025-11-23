from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional,Dict
from enum import Enum

app = FastAPI()

# In-memory data storage
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders = []  # list of Order models
next_menu_id = 5
next_order_id = 1

# Enum for order status
class OrderStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

# Pydantic Models
class MenuItem(BaseModel):
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
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.pending  # Using Enum for validation
    special_instructions: Optional[str] = None

# Menu CRUD endpoints
@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    item = next((item for item in menu if item["id"] == id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@app.post("/menu", status_code=201, response_model=MenuItem)
def add_menu_item(item: MenuItem):
    global next_menu_id  
    item.id = next_menu_id
    menu.append(item.dict())  
    next_menu_id += 1  
    return item

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            menu[idx] = item.dict()  # Replace with the dictionary representation of the model
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            del menu[idx]
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# Orders API endpoints
@app.post("/orders", status_code=201, response_model=Order)
def create_order(order: Order):
    global next_order_id  # Declare global before using
    for item in order.items:
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Item {item.menu_item_id} is unavailable")

    order.id = next_order_id
    orders.append(order) 
    next_order_id += 1  
    return order

@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[OrderStatus] = None):
    if status:
        return [order for order in orders if order.status == status]
    return orders

@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Order status update
@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status: OrderStatus):
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.status in [OrderStatus.completed, OrderStatus.cancelled]:
        raise HTTPException(status_code=400, detail="Cannot change status after completion or cancellation")
    order["status"] = status
    return order

# Calculate total bill for an order
@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    total_amount = 0
    for item in order.items:
        menu_item = next((m for m in menu if m.id == item.menu_item_id), None)
        if menu_item:
            total_amount += menu_item.price * item.quantity
    return {"order_id": id, "total_amount": total_amount}
