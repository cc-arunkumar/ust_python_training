from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# FastAPI app initialization with a title for the application.
app = FastAPI(title="Spice Hub")

# MenuItem class defines the structure for menu items.
# Each item has an ID, name, category, price, and availability status.
class MenuItem(BaseModel):
    id: int  # Unique identifier for the menu item.
    name: str  # Name of the dish/menu item.
    category: str  # Category such as 'starter', 'main_course', or 'dessert'.
    price: float  # Price of the menu item.
    is_available: bool  # Availability status (True or False).

# OrderItem class defines the structure for an order item.
# It connects to a menu item via its ID and stores the quantity ordered.
class OrderItem(BaseModel):
    menu_item_id: int  # ID of the menu item being ordered.
    quantity: int  # Quantity of the menu item in the order.

# Order class defines the structure for an order, including details like
# order type, status, table number, and a list of ordered items.
class Order(BaseModel):
    id: int  # Unique identifier for the order.
    order_type: str  # Type of the order, either 'dine_in' or 'takeaway'.
    table_number: Optional[int] = None  # Optional table number for dine-in orders.
    items: List[OrderItem]  # List of items ordered in this order.
    status: str = "pending"  # Default status is 'pending'.
    special_instructions: Optional[str] = None  # Optional special instructions for the order.

# Sample menu with predefined items.
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

# List to hold the orders in memory.
orders = []
next_menu_id = 5  # ID counter for menu items.
next_order_id = 1  # ID counter for orders.

# Endpoint to get the entire menu.
# Optionally filter to return only available items.
@app.get("/menu")
def get_menu(only_available: bool = False):
    if only_available:
        # Filter menu to return only available items.
        return [item for item in menu if item["is_available"]]
    return menu  # Return full menu if no filter is applied.

# Endpoint to get a specific menu item by its ID.
@app.get("/menu/{id}")
def get_menu_by_id(id: int):
    # Search for the menu item by ID.
    for item in menu:
        if item["id"] == id:
            return item
    # If item is not found, raise a 404 error.
    raise HTTPException(status_code=404, detail="Item not found.")

# Endpoint to add a new menu item.
@app.post("/menu", status_code=201)
def add_menu(item: MenuItem):
    global next_menu_id
    # Convert Pydantic model to dictionary and assign a new ID.
    new_item = item.dict()
    new_item["id"] = next_menu_id
    menu.append(new_item)  # Add the new item to the menu.
    next_menu_id += 1  # Increment the ID for the next item.
    return new_item  # Return the newly added item.

# Endpoint to update an existing menu item by its ID.
@app.put("/menu/{id}")
def update_menu(id: int, item: MenuItem):
    # Find the menu item to update.
    for i, m in enumerate(menu):
        if m["id"] == id:
            updated_item = item.dict()
            updated_item["id"] = id
            menu[i] = updated_item  # Replace the old item with the updated one.
            return updated_item
    # If item is not found, raise a 404 error.
    raise HTTPException(status_code=404, detail="Item Not Found!")

# Endpoint to delete a menu item by its ID.
@app.delete("/menu/{id}")
def delete_menu(id: int):
    # Find and delete the item from the menu.
    for i, m in enumerate(menu):
        if m["id"] == id:
            menu.pop(i)
            return {"detail": "Menu Item deleted successfully."}
    # If item is not found, raise a 404 error.
    raise HTTPException(status_code=404, detail="Item not found.")

# Endpoint to create a new order.
@app.post("/orders", status_code=201)
def create_order(order: Order):
    global next_order_id
    
    # Validate order type (either 'dine_in' or 'takeaway').
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order type.")
    
    # For dine-in orders, ensure table number is provided and valid.
    if order.order_type == "dine_in" and (not order.table_number or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number is required for dine-in orders.")
    
    # Validate ordered items.
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Item quantity must be greater than zero.")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail="Item not found.")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail="Item is not available.")

    # Create a new order and assign it a unique ID.
    new_order = order.dict()
    new_order["id"] = next_order_id
    new_order["status"] = "pending"  # Default order status is 'pending'.
    orders.append(new_order)  # Add the new order to the orders list.
    next_order_id += 1  # Increment the order ID for the next order.
    return new_order  # Return the newly created order.

# Endpoint to fetch all orders, optionally filtered by status.
@app.get("/orders")
def get_order(status: Optional[str] = None):
    if status:
        return [o for o in orders if o["status"] == status]
    return orders  # Return all orders if no filter is applied.

# Endpoint to get details of a specific order by its ID.
@app.get("/orders/{id}/")
def get_order_by_id(id: int):
    for ord in orders:
        if ord["id"] == id:
            return ord
    # If order is not found, raise a 404 error.
    raise HTTPException(status_code=404, detail="Order not found.")

# Endpoint to update the status of an order.
@app.patch("/orders/{id}/status")
def update_status(id: int, status: str):
    for o in orders:
        if o["id"] == id:
            current_status = o["status"]
            
            # Allowed status transitions.
            allowed_changes = {
                "pending": ["in_progress", "cancelled"],
                "in_progress": ["completed", "cancelled"]
            }
            
            # Prevent changing the status after it is completed or cancelled.
            if current_status in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="Cannot modify an already completed or cancelled order.")
            
            # Validate the status transition.
            if status not in allowed_changes.get(current_status, []):
                raise HTTPException(status_code=400, detail="Invalid status transition.")
            
            o["status"] = status  # Update the order status.
            return o  # Return the updated order.
        
    # If order is not found, raise a 404 error.
    raise HTTPException(status_code=404, detail="Order not found.")

# Endpoint to compute the total bill for an order by its ID.
@app.get("/orders/{id}/total_amount")
def compute_bill(id: int):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")
    
    # Calculate the total amount by summing up the price of each item.
    total_amount = 0.0
    for item in order["items"]:
        menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
        if menu_item:
            total_amount += menu_item["price"] * item["quantity"]
    
    return {"orderId": id, "total_amount": total_amount}

# Sample Responses Section:

# 1. Sample response when fetching the entire menu:
# GET /menu
# Request (No query parameters):
# {
#   "only_available": false
# }

# Response:
# [
#   {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#   {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#   {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true},
#   {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false}
# ]

# 2. Sample response when fetching a specific menu item by ID:
# GET /menu/{id}
# Request (ID = 2):
# {
#   "id": 2
# }

# Response:
# {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true}

# 3. Sample response when adding a new menu item:
# POST /menu
# Request Body:
# {
#   "name": "Mushroom Soup",
#   "category": "starter",
#   "price": 109.0,
#   "is_available": true
# }

# Response:
# {
#   "id": 5,
#   "name": "Mushroom Soup",
#   "category": "starter",
#   "price": 109.0,
#   "is_available": true
# }

# 4. Sample response when updating an existing menu item:
# PUT /menu/{id}
# Request (ID = 2):
# {
#   "name": "Paneer Butter Masala",
#   "category": "main_course",
#   "price": 259.0,
#   "is_available": true
# }

# Response:
# {
#   "id": 2,
#   "name": "Paneer Butter Masala",
#   "category": "main_course",
#   "price": 259.0,
#   "is_available": true
# }

# 5. Sample response when deleting a menu item:
# DELETE /menu/{id}
# Request (ID = 4):
# {
#   "id": 4
# }

# Response:
# {"detail": "Menu Item deleted successfully."}

# 6. Sample response when creating a new order:
# POST /orders
# Request Body:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 2, "quantity": 1}
#   ]
# }

# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 2, "quantity": 1}
#   ],
#   "status": "pending",
#   "special_instructions": null
# }

# 7. Sample response when fetching all orders:
# GET /orders
# Request:
# {
#   "status": null
# }

# Response:
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       {"menu_item_id": 1, "quantity": 2},
#       {"menu_item_id": 2, "quantity": 1}
#     ],
#     "status": "pending",
#     "special_instructions": null
#   }
# ]

# 8. Sample response when fetching a specific order by ID:
# GET /orders/{id}
# Request (ID = 1):
# {
#   "id": 1
# }

# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 2, "quantity": 1}
#   ],
#   "status": "pending",
#   "special_instructions": null
# }

# 9. Sample response when updating the status of an order:
# PATCH /orders/{id}/status
# Request (ID = 1, Status = "in_progress"):
# {
#   "status": "in_progress"
# }

# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 2, "quantity": 1}
#   ],
#   "status": "in_progress",
#   "special_instructions": null
# }

# 10. Sample response when calculating the total bill for an order:
# GET /orders/{id}/total_amount
# Request (ID = 1):
# {
#   "id": 1
# }

# Response:
# {
#   "orderId": 1,
#   "total_amount": 497.0
# }
