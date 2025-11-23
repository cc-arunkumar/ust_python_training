from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Data storage
next_menu_id = 5
next_order_id = 1

# Menu item model
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool = False

# Sample menu data
Menu: List[MenuItem] = [
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

# FastAPI app instance
app = FastAPI(title="SpiceHub")

# =========================== Menu Endpoints ============================
@app.get("/menu")
def get_all_menu_items(only_available: bool = False):
    # Filter available items if 'only_available' is True
    if only_available:
        return [item for item in Menu if item["is_available"]]
    return Menu

@app.get("/menu/{id}", response_model=MenuItem)
def get_item(id: int):
    # Find and return the menu item with the given id
    for item in Menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem)
def add_newmenu_item(menu: MenuItem):
    global next_menu_id
    menu.id = next_menu_id
    next_menu_id += 1
    Menu.append(menu.dict())
    return menu

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, menu: MenuItem):
    for item in Menu:
        if item["id"] == id:
            item.update(menu.dict(exclude={"id"}))  # Update excluding ID
            return item
    raise HTTPException(status_code=404, detail="Item does not exist")

@app.delete("/menu/{id}")
def delete_item(id: int):
    global Menu
    for i in range(len(Menu)):
        if Menu[i]["id"] == id:
            del Menu[i]
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# =========================== Order Endpoints ============================
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):
    id: int
    order_type: str
    table_number: int | None = 0
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: str | None = ""

orders = []

@app.post("/orders", response_model=Order)
def add_order(order: Order):
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Invalid quantity")
        menu_item = next((menu for menu in Menu if menu["id"] == item.menu_item_id), None)
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail="Invalid menu_id or item not available")
    
    global next_order_id
    order.id = next_order_id
    next_order_id += 1
    orders.append(order.dict())
    return order

@app.get("/orders")
def get_all_orders(status: str = ""):
    if status:
        return [order for order in orders if order["status"] == status]
    return orders

@app.get("/orders/{id}")
def get_order(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: str):
    order = next((order for order in orders if order["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order["status"] == "completed" or order["status"] == "cancelled":
        raise HTTPException(status_code=400, detail="Cannot update status from completed or cancelled")

    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"]
    }

    if status in allowed_transitions.get(order["status"], []):
        order["status"] = status
        return order
    raise HTTPException(status_code=400, detail="Invalid status transition")

@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    total_amount = 0
    for order_item in order["items"]:
        menu_item = next((menu for menu in Menu if menu["id"] == order_item.menu_item_id), None)
        if menu_item:
            total_amount += menu_item["price"] * order_item.quantity
    return {"order_id": id, "total_amount": total_amount}
