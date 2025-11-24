# 1. Scenario
# You are building a small REST API for a restaurant called “SpiceHub”.
# The API will help restaurant staff to:
# 1. Manage the menu (add, view, update, delete dishes).
# 2. Take orders from customers (dine-in or takeaway).
# 3. Track order status (pending → in_progress → completed / cancelled).
# 4. Calculate total bill for an order.
# Everything is stored in memory (Python lists/dicts).
# No database. If server restarts, data is lost (this is ok for practice).

from typing import List, Optional
from fastapi import FastAPI, HTTPException
import datetime

from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="SpiceHub")

# Global variables for generating IDs
next_menu_id = 5
next_order_id = 1

# Pydantic model for Menu Item
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool = False  # Default is not available

# Pydantic model for Order Item (menu items in an order)
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Pydantic model for Order (an entire order)
class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: str = None

# Sample menu items (in-memory storage)
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# List to store orders (in-memory storage)
orders = []

# Extract headers from the first menu item
headers = list(menu[0].keys())

# Endpoint to get the menu, optionally filtered for only available items
@app.get("/menu")
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        # Filter and return only available items
        filtered_menu = [item for item in menu if item['is_available']]
    else:
        # Return entire menu
        filtered_menu = menu
    return filtered_menu

# Endpoint to get a single menu item by its ID
@app.get("/menu/{id}")
def get_menu_by_id(id: int):
    for row in menu:
        if row['id'] == id:
            return row
    raise HTTPException(status_code=404, detail="Menu item not found")

# Endpoint to add a new menu item
@app.post("/menu")
def read_menu(read: MenuItem):
    global next_menu_id
    for row in menu:
        if row[headers[0]] == read.id:
            raise HTTPException(status_code=404, detail="Menu item already exists")
    read.id = next_menu_id
    next_menu_id += 1
    menu.append(read)
    return read

# Endpoint to update an existing menu item by ID
@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, update: MenuItem):
    for row in menu:
        if row["id"] == id:
            row["name"] = update.name
            row["category"] = update.category
            row["price"] = update.price
            row["is_available"] = update.is_available
            return row  # Return the updated menu item
    raise HTTPException(status_code=404, detail="ID Not Found")

# Endpoint to delete a menu item by ID
@app.delete("/menu/{id}", response_model=MenuItem)
def delete_menu(id: int):
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            return menu.pop(i)
    raise HTTPException(status_code=404, detail="ID Not Found")

# Endpoint to create a new order
@app.post('/orders', response_model=Order)
def create_order(new_order: Order):
    new_list_id = [item[headers[0]] for item in menu]  # Get a list of available menu item IDs
    for row in new_order.items:
        if row.quantity <= 0:
            raise HTTPException(status_code=400, detail="Invalid Quantity")
        if row.menu_item_id not in new_list_id:
            raise HTTPException(status_code=404, detail="Menu Item not Found!")
        for item in menu:
            if row.menu_item_id == item[headers[0]] and not item[headers[4]]:
                raise HTTPException(status_code=400, detail="Item is Not Available!")
    
    global next_order_id
    if new_order.order_type == 'takeaway':
        new_order.id = next_order_id
        next_order_id += 1
        orders.append(new_order)
        return new_order
    elif new_order.order_type == 'dine_in':
        if isinstance(new_order.table_number, int):
            new_order.id = next_order_id
            next_order_id += 1
            orders.append(new_order)
            return new_order
        else:
            raise HTTPException(status_code=400, detail="Invalid Table Number")
    else:
        raise HTTPException(status_code=400, detail="Invalid Order Type")

# Endpoint to get all orders (can filter by status)
@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[str] = "pending"):
    if status is not None:
        # Filter orders based on status
        new_order_list = [order for order in orders if order.status == status]
        return new_order_list
    else:
        # Return all orders
        return orders

# Endpoint to get a specific order by its ID
@app.get("/orders/{id}")
def get_order_id(id: int):
    for ord in orders:
        if ord.id == id:
            return ord
    raise HTTPException(status_code=404, detail="Order Not Found")

# Endpoint to update the status of an order
@app.patch('/orders/{id}/status')
def update_status(id: int, payload: dict):
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break

    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")

    if not payload or "status" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'status' in request body")
    
    new_status = payload["status"]
    current_status = order_found.status

    # Define valid status transitions
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }

    if current_status not in allowed_transitions:
        raise HTTPException(status_code=400, detail=f"Unknown current status: {current_status}")
    
    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(status_code=400, detail=f"Cannot transition from '{current_status}' to '{new_status}'")
    
    # Update the order's status
    order_found.status = new_status
    return order_found

# Endpoint to get the total amount for a specific order
@app.get('/orders/{id}/total-amount')
def get_order_total(id: int):
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
    
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")

    total_amount = 0.0
    for order_item in order_found.items:
        # Find the corresponding menu item and calculate the total
        menu_item = None
        for item in menu:
            if item['id'] == order_item.menu_item_id:
                menu_item = item
                break
        if menu_item is not None:
            total_amount += menu_item['price'] * order_item.quantity

    return {
        "order_id": id,
        "total_amount": total_amount
    }

       
       
# Sample ouput

# **Output for GET /menu**
# If only_available=False (default), output:
# [
#     {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
#     {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
#     {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
#     {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
# ]
# If only_available=True, output:
# [
#     {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
#     {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
#     {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True}
# ]

# **Output for GET /menu/{id}**
# If `id=1`, output:
# {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True}
# If `id=5` (nonexistent), output:
# HTTPException: 404 Not Found - Menu item not found


# **Output for POST /menu**
# Input: 
# {"name": "Veg Biryani", "category": "main_course", "price": 179.0, "is_available": True}
# Output: 
# {"id": 5, "name": "Veg Biryani", "category": "main_course", "price": 179.0, "is_available": True}


# **Output for PUT /menu/{id}**
# If `id=1` and new data is provided:
# Input:
# {"name": "Tomato Soup", "category": "starter", "price": 109.0, "is_available": True}
# Output:
# {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 109.0, "is_available": True}


# **Output for DELETE /menu/{id}**
# If `id=1`, output:
# {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True}
# If `id=5` (nonexistent), output:
# HTTPException: 404 Not Found - ID Not Found


# **Output for POST /orders**
# Input:
# {"order_type": "takeaway", "table_number": null, "items": [{"menu_item_id": 1, "quantity": 2}, {"menu_item_id": 3, "quantity": 1}]}
# Output:
# {"id": 1, "order_type": "takeaway", "table_number": null, "items": [{"menu_item_id": 1, "quantity": 2}, {"menu_item_id": 3, "quantity": 1}], "status": "pending", "special_instructions": null}


# **Output for GET /orders**
# If there are 2 pending orders, output:
# [
#     {"id": 1, "order_type": "takeaway", "table_number": null, "items": [{"menu_item_id": 1, "quantity": 2}], "status": "pending", "special_instructions





