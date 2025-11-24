from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory data to simulate a simple menu and orders list
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []  # List to store orderszczxczxc
next_menu_id = 5  # Next ID for adding a new menu item
next_order_id = 1  # Next ID for adding a new order

# Pydantic model for menu item data validation
class MenuItem(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool

# Pydantic model for order item data validation
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Pydantic model for the entire order data validation
class Order(BaseModel):
    order_type: str
    table_number: Optional[int] = None  # Optional field for dine-in orders
    items: List[OrderItem]
    status: str = "pending"  # Default status for new orders
    special_instructions: Optional[str] = None  # Optional special instructions for the order

# Endpoint to get the full menu, with an option to filter for available items only
@app.get("/menu")
def get_menu(only_available: bool = False):
    if only_available:
        return [item for item in menu if item["is_available"]]  # Filter out unavailable items
    return menu

# Endpoint to get a specific menu item by its ID
@app.get("/menu/{id}")
def get_menu_item(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")  # Raise error if item not found

# Endpoint to add a new menu item
@app.post("/menu")
def add_menu_item(item: MenuItem):
    global next_menu_id
    item_data = item.dict()  # Convert Pydantic model to dictionary
    item_data["id"] = next_menu_id  # Assign a new unique ID
    menu.append(item_data)  # Add the new item to the menu
    next_menu_id += 1  # Increment the next ID for future items
    return item_data

# Endpoint to update an existing menu item by ID
@app.put("/menu/{id}")
def update_menu_item(id: int, item: MenuItem):
    for idx, existing_item in enumerate(menu):
        if existing_item["id"] == id:
            menu[idx] = {**existing_item, **item.dict()}  # Merge existing item with updated data
            return menu[idx]
    raise HTTPException(status_code=404, detail="Menu item not found")  # Item not found

# Endpoint to delete a menu item by ID
@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    global menu
    menu = [item for item in menu if item["id"] != id]  # Remove the item with the specified ID
    return {"detail": "Menu item deleted"}

# Endpoint to create a new order
@app.post("/orders")
def create_order(order: Order):
    global next_order_id
    # Validate order type
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order type")
    
    # Ensure table number is provided for dine-in, and not for takeaway
    if order.order_type == "dine_in" and not order.table_number:
        raise HTTPException(status_code=400, detail="Table number required for dine-in")
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number must be null for takeaway")
    
    # Check if all ordered items are available
    for order_item in order.items:
        menu_item = None
        for item in menu:
            if item["id"] == order_item.menu_item_id:
                menu_item = item
                break
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail="Item not available")

    # Create the order and assign an ID
    order_data = order.dict()
    order_data["id"] = next_order_id
    orders.append(order_data)  # Add order to the orders list
    next_order_id += 1  # Increment next order ID
    return order_data

# Endpoint to get all orders, optionally filtering by status
@app.get("/orders")
def get_orders(status: Optional[str] = None):
    if status:
        return [order for order in orders if order["status"] == status]  # Filter orders by status
    return orders

# Endpoint to get a specific order by its ID
@app.get("/orders/{id}")
def get_order(id: int):
    for order in orders:
        if order["id"] == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")  # Order not found

# Endpoint to update the status of an order
@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: dict):
    for order in orders:
        if order["id"] == id:
            if order["status"] == "completed" or order["status"] == "cancelled":
                raise HTTPException(status_code=400, detail="Cannot update completed or cancelled orders")
            if status["status"] not in ["in_progress", "completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="Invalid status transition")
            order["status"] = status["status"]  # Update the status of the order
            return order
    raise HTTPException(status_code=404, detail="Order not found")  # Order not found

# Endpoint to calculate the total amount for a given order ID
@app.get("/orders/{id}/total-amount")
def calculate_total(id: int):
    for order in orders:
        if order["id"] == id:
            total = 0
            # Calculate total amount based on ordered items and their quantities
            for order_item in order["items"]:
                menu_item = None
                for item in menu:
                    if item["id"] == order_item.menu_item_id:
                        menu_item = item
                        break
                if menu_item:
                    total += menu_item["price"] * order_item.quantity  # Add item price times quantity
            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")  # Order not found
