from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

# Step 1: Initialize FastAPI app
app = FastAPI()

# Step 2: Define data models using Pydantic for validation
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
    status: str = "pending"
    special_instructions: Optional[str] = None

# Step 3: Initialize in-memory data storage
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []
next_menu_id = 5
next_order_id = 1

# Step 4: Menu endpoints (CRUD operations)

# Get all menu items, with optional filter for availability
@app.get("/menu")
def get_menu(only_available: bool = Query(False)):
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu

# Get a single menu item by ID
@app.get("/menu/{id}")
def get_menu_item(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

# Add a new menu item
@app.post("/menu", status_code=201)
def add_menu_item(item: MenuItem):
    global next_menu_id
    new_item = item.dict()
    new_item["id"] = next_menu_id
    menu.append(new_item)
    next_menu_id += 1
    return new_item

# Update an existing menu item
@app.put("/menu/{id}")
def update_menu_item(id: int, item: MenuItem):
    for m in menu:
        if m["id"] == id:
            m.update(item.dict())
            m["id"] = id   # Ensure ID remains unchanged
            return m
    raise HTTPException(status_code=404, detail="Menu item not found")

# Delete a menu item
@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for m in menu:
        if m["id"] == id:
            menu.remove(m)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# Step 5: Order endpoints

# Create a new order with validation rules
@app.post("/orders", status_code=201)
def create_order(order: Order):
    global next_order_id

    # Validate order type
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order_type")

    # Validate dine-in table number
    if order.order_type == "dine_in" and (not order.table_number or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number required for dine_in")

    # Validate takeaway should not have table number
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number must be null for takeaway")

    # Validate each order item
    for item in order.items:
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} not available")
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be > 0")

    # Create new order
    new_order = order.dict()
    new_order["id"] = next_order_id
    new_order["status"] = "pending"
    orders.append(new_order)
    next_order_id += 1
    return new_order

# Get all orders, optionally filter by status
@app.get("/orders")
def get_orders(status: Optional[str] = None):
    if status:
        return [o for o in orders if o["status"] == status]
    return orders

# Get a single order by ID
@app.get("/orders/{id}")
def get_order(id: int):
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")
