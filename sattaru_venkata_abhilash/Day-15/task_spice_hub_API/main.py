from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# In-memory data storage for menu items and orders
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]
orders = []  # List to store order details
next_menu_id = 5  # To generate unique IDs for new menu items
next_order_id = 1  # To generate unique IDs for new orders

# Pydantic models for input validation and response format
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
    table_number: Optional[int] = None  # Optional for dine-in orders
    items: List[OrderItem]
    status: str = "pending"  # Default status is "pending"
    special_instructions: Optional[str] = None

# Menu CRUD API endpoints

# Get all menu items, optionally filter by availability
@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        # Return only available menu items
        return [item for item in menu if item["is_available"]]
    return menu  # Return all menu items

# Get details of a specific menu item by its ID
@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    item = next((item for item in menu if item["id"] == id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

# Add a new menu item
@app.post("/menu", status_code=201, response_model=MenuItem)
def add_menu_item(item: MenuItem):
    global next_menu_id  # Use global variable for ID generation
    item.id = next_menu_id  # Assign the next available ID
    menu.append(item.dict())  # Add the new item to the menu list
    next_menu_id += 1  # Increment the menu item ID counter
    return item  # Return the newly added item

# Update an existing menu item by its ID
@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            menu[idx] = item.dict()  # Update the existing menu item with new data
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

# Delete a menu item by its ID
@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for idx, menu_item in enumerate(menu):
        if menu_item["id"] == id:
            del menu[idx]  # Remove the menu item from the list
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# Orders API endpoints

# Create a new order
@app.post("/orders", status_code=201, response_model=Order)
def create_order(order: Order):
    global next_order_id  # Use global variable for ID generation
    for item in order.items:
        # Check if all items in the order are available
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Item {item.menu_item_id} is unavailable")
    
    order.id = next_order_id  # Assign the next available order ID
    orders.append(order.dict())  # Add the order to the orders list
    next_order_id += 1  # Increment the order ID counter
    return order  # Return the newly created order

# Get all orders, optionally filter by status
@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[str] = None):
    if status:
        # Filter orders by status if provided
        return [order for order in orders if order["status"] == status]
    return orders  # Return all orders

# Get details of a specific order by its ID
@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Update the status of an existing order
@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status: str):
    order = next((order for order in orders if order["id"] == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    # Prevent status change after completion or cancellation
    if order["status"] == "completed" or order["status"] == "cancelled":
        raise HTTPException(status_code=400, detail="Cannot change status after completion or cancellation")

    # Validate status change
    if status not in ["pending", "in_progress", "completed", "cancelled"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    order["status"] = status  # Update the order status
    return order

# Calculate the total bill for a specific order
@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    # Calculate the total amount by multiplying the price of each item with its quantity
    total_amount = 0
    for item in order["items"]:
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if menu_item:
            total_amount += menu_item["price"] * item.quantity
    
    return {"order_id": id, "total_amount": total_amount}  # Return the total amount for the order
