from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory data
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []
next_menu_id = 5
next_order_id = 1

class MenuItem(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool

class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):
    order_type: str
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: Optional[str] = None

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
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu")
def add_menu_item(item: MenuItem):
    global next_menu_id
    item_data = item.dict()
    item_data["id"] = next_menu_id
    menu.append(item_data)
    next_menu_id += 1
    return item_data

@app.put("/menu/{id}")
def update_menu_item(id: int, item: MenuItem):
    for idx, existing_item in enumerate(menu):
        if existing_item["id"] == id:
            menu[idx] = {**existing_item, **item.dict()}
            return menu[idx]
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    global menu
    menu = [item for item in menu if item["id"] != id]
    return {"detail": "Menu item deleted"}

@app.post("/orders")
def create_order(order: Order):
    global next_order_id
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order type")
    if order.order_type == "dine_in" and not order.table_number:
        raise HTTPException(status_code=400, detail="Table number required for dine-in")
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number must be null for takeaway")
    
    # Check menu items with explicit loop
    for order_item in order.items:
        menu_item = None
        for item in menu:
            if item["id"] == order_item.menu_item_id:
                menu_item = item
                break
        
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail="Item not available")

    order_data = order.dict()
    order_data["id"] = next_order_id
    orders.append(order_data)
    next_order_id += 1
    return order_data

@app.get("/orders")
def get_orders(status: Optional[str] = None):
    if status:
        return [order for order in orders if order["status"] == status]
    return orders

@app.get("/orders/{id}")
def get_order(id: int):
    for order in orders:
        if order["id"] == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: dict):
    for order in orders:
        if order["id"] == id:
            if order["status"] == "completed" or order["status"] == "cancelled":
                raise HTTPException(status_code=400, detail="Cannot update completed or cancelled orders")
            if status["status"] not in ["in_progress", "completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="Invalid status transition")
            order["status"] = status["status"]
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{id}/total-amount")
def calculate_total(id: int):
    for order in orders:
        if order["id"] == id:
            total = 0
            for order_item in order["items"]:
                menu_item = None
                for item in menu:
                    if item["id"] == order_item.menu_item_id:
                        menu_item = item
                        break
                if menu_item:
                    total += menu_item["price"] * order_item.quantity
            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")
