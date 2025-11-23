from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
 
app = FastAPI()
 

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
    table_number: Optional[int]
    items: List[OrderItem]
    status: str
    special_instructions: Optional[str]
 

menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]
 
orders = []
next_menu_id = 5
next_order_id = 1
 

@app.get("/menu")
def get_menu(only_available: bool = False):
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu
 
 
@app.get("/menu/{id}")
def get_menu_item(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(404, "Menu item not found")
 
 
@app.post("/menu", status_code=201)
def create_menu_item(item: dict):
    global next_menu_id
 
    item["id"] = next_menu_id
    next_menu_id += 1
 
    menu.append(item)
    return item
 
 
@app.put("/menu/{id}")
def update_menu_item(id: int, data: dict):
    for i, item in enumerate(menu):
        if item["id"] == id:
            updated = data.copy()
            updated["id"] = id
            menu[i] = updated
            return updated
    raise HTTPException(404, "Menu item not found")
 
 
@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for i, item in enumerate(menu):
        if item["id"] == id:
            del menu[i]
            return {"detail": "Menu item deleted"}
    raise HTTPException(404, "Menu item not found")


@app.post("/orders", status_code=201)
def create_order(order: dict):
    global next_order_id
 
    # Validate order_type
    if order["order_type"] not in ["dine_in", "takeaway"]:
        raise HTTPException(400, "Invalid order_type")
 
    # Validate table_number
    if order["order_type"] == "dine_in":
        if not isinstance(order["table_number"], int) or order["table_number"] <= 0:
            raise HTTPException(400, "table_number must be positive integer for dine_in")
    else:
        if order["table_number"] not in [None, 0]:
            raise HTTPException(400, "table_number must be null or 0 for takeaway")
 
    # Validate items
    for item in order["items"]:
        if item["quantity"] <= 0:
            raise HTTPException(400, "Quantity must be > 0")
 
        # Find menu item
        m = next((x for x in menu if x["id"] == item["menu_item_id"]), None)
        if not m:
            raise HTTPException(400, f"Menu item {item['menu_item_id']} does not exist")
 
        # Check availability
        if not m["is_available"]:
            raise HTTPException(400, f"Menu item {m['name']} is not available")
 
    # Create order
    new_order = {
        "id": next_order_id,
        "order_type": order["order_type"],
        "table_number": order["table_number"],
        "items": order["items"],
        "special_instructions": order.get("special_instructions"),
        "status": "pending"
    }
 
    next_order_id += 1
    orders.append(new_order)
    return new_order
 
 
@app.get("/orders")
def list_orders(status: Optional[str] = None):
    if status:
        return [o for o in orders if o["status"] == status]
    return orders
 
 
@app.get("/orders/{id}")
def get_order(id: int):
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(404, "Order not found")
 
 
@app.patch("/orders/{id}/status")
def update_order_status(id: int, data: dict):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(404, "Order not found")
 
    new_status = data["status"]
    current = order["status"]
 
    transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }
 
    if new_status not in transitions[current]:
        raise HTTPException(400, "Invalid status transition")
 
    order["status"] = new_status
    return order
 
 
@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(404, "Order not found")
 
    total = 0
    for item in order["items"]:
        m = next(m for m in menu if m["id"] == item["menu_item_id"])
        total += m["price"] * item["quantity"]
 
    return {"order_id": id, "total_amount": total}

