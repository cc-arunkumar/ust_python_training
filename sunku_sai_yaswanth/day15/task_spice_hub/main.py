from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
from enum import Enum

app = FastAPI()

# In-memory data storage for menu items
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# In-memory data storage for orders
orders = []  
next_menu_id = 5  # Starting ID for new menu items
next_order_id = 1  # Starting ID for new orders

# Enum to define the status of an order
class OrderStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

# Pydantic Models to validate incoming data

class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool

class OrderItem(BaseModel):
    menu_item_id: int  # ID of the item from the menu
    quantity: int  # Quantity of the item ordered

class Order(BaseModel):
    id: int
    order_type: str  # Type of order (e.g., dine-in, takeaway)
    table_number: Optional[int] = None  # Optional table number for dine-in
    items: List[OrderItem]  # List of ordered items
    status: OrderStatus = OrderStatus.pending  # Default status is 'pending'
    special_instructions: Optional[str] = None  # Optional instructions for the order

# Menu CRUD endpoints

@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: Optional[bool] = False):
    """
    Endpoint to retrieve the full menu, with optional filter for only available items.
    """
    if only_available:
        return [item for item in menu if item["is_available"]]  # Filter available items
    return menu  # Return the entire menu

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    """
    Endpoint to retrieve a specific menu item by ID.
    """
    item = next((item for item in menu if item["id"] == id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")  # Item not found
    return item

@app.post("/menu", status_code=201, response_model=MenuItem)
def add_menu_item(item: MenuItem):
    """
    Endpoint to add a new menu item.
    """
    global next_menu_id  
    item.id = next_menu_id  # Assign the next available ID
    menu.append(item.dict())  # Add the new item to the menu
    next_menu_id += 1  # Increment the ID for the next menu item
    return item

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    """
    Endpoint to update an existing menu item by ID.
    """
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            menu[idx] = item.dict()  # Update the item in the menu
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")  # Item not found

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    """
    Endpoint to delete a menu item by ID.
    """
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            del menu[idx]  # Remove the item from the menu
            return {"detail": "Menu item deleted"}  # Return success message
    raise HTTPException(status_code=404, detail="Menu item not found")  # Item not found

# Orders API endpoints

@app.post("/orders", status_code=201, response_model=Order)
def create_order(order: Order):
    """
    Endpoint to create a new order. Validates item availability before adding.
    """
    global next_order_id  # Declare global before using
    for item in order.items:
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Item {item.menu_item_id} is unavailable")  # Item unavailable

    order.id = next_order_id  # Assign the next available order ID
    orders.append(order)  # Add the order to the orders list
    next_order_id += 1  # Increment the order ID for the next order
    return order

@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[OrderStatus] = None):
    """
    Endpoint to retrieve all orders, optionally filtered by status.
    """
    if status:
        return [order for order in orders if order.status == status]  # Filter orders by status
    return orders  # Return all orders

@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    """
    Endpoint to retrieve a specific order by ID.
    """
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")  # Order not found
    return order

# Order status update

@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status: OrderStatus):
    """
    Endpoint to update the status of an existing order by ID.
    """
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")  # Order not found
    if order.status in [OrderStatus.completed, OrderStatus.cancelled]:
        raise HTTPException(status_code=400, detail="Cannot change status after completion or cancellation")  # Invalid status change
    order.status = status  # Update the order status
    return order

# Calculate total bill for an order

@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    """
    Endpoint to calculate and return the total amount for a specific order.
    """
    order = next((order for order in orders if order.id == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")  # Order not found
    total_amount = 0
    for item in order.items:
        menu_item = next((m for m in menu if m.id == item.menu_item_id), None)
        if menu_item:
            total_amount += menu_item.price * item.quantity  # Calculate total price
    return {"order_id": id, "total_amount": total_amount}  # Return total bill

# output
# GET /menu
# [
#     {
#         "id": 1,
#         "name": "Tomato Soup",
#         "category": "starter",
#         "price": 99.0,
#         "is_available": true
#     },
#     {
#         "id": 2,
#         "name": "Paneer Butter Masala",
#         "category": "main_course",
#         "price": 249.0,
#         "is_available": true
#     },
#     {
#         "id": 3,
#         "name": "Butter Naan",
#         "category": "main_course",
#         "price": 49.0,
#         "is_available": true
#     },
#     {
#         "id": 4,
#         "name": "Gulab Jamun",
#         "category": "dessert",
#         "price": 79.0,
#         "is_available": false
#     }
# ]
# GET /menu/1
# {
#     "id": 1,
#     "name": "Tomato Soup",
#     "category": "starter",
#     "price": 99.0,
#     "is_available": true
# }
# POST /menu
# {
#     "name": "Mango Lassi",
#     "category": "drink",
#     "price": 120.0,
#     "is_available": true
# }
# {
#     "id": 5,
#     "name": "Mango Lassi",
#     "category": "drink",
#     "price": 120.0,
#     "is_available": true
# }
