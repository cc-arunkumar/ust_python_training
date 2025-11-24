# SpiceHub Restaurant API

# This is a simple REST API for managing a restaurant's menu and handling customer orders.

# Features include:

# 1. Menu CRUD operations (Create, Read, Update, Delete) for dishes.
# 2. Order management (create, view, update status, calculate total).
# 3. In-memory storage for menu items and orders (data is lost on server restart).
# 4. Order status transitions: "pending" -> "in_progress" -> "completed" / "cancelled".
# 5. Calculation of total bill for an order based on the ordered items' prices.



from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Spice Hub")

# Pydantic Models for Data Validation

class MenuItem(BaseModel):
    
    # Pydantic model representing a menu item.
    id: int  # Unique identifier for the menu item
    name: str  # Name of the menu item
    category: str  # Category of the menu item (e.g., 'starter', 'main_course')
    price: float  # Price of the menu item
    is_available: bool  # Availability status of the menu item (True/False)

class OrderItem(BaseModel):
    
    # Pydantic model representing an item in a customer's order.
    menu_item_id: int  # ID of the menu item being ordered
    quantity: int  # Quantity of the menu item ordered

class Order(BaseModel):
    
    # Pydantic model representing a customer order.
    id: int  # Unique identifier for the order
    order_type: str  # Type of order: 'dine_in' or 'take_away'
    table_number: int = None  # Table number for dine-in orders (optional for take-away)
    items: List[OrderItem]  # List of items in the order
    status: str = "pending"  # Status of the order (default is 'pending')
    special_instruction: str = "Nothing"  # Special instructions for the order

# In-memory data (Simulating a database)

menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders: List[Order] = []  # List to store orders
next_menu_id = 4  # Starting ID for the next menu item
next_order_id = 0  # Starting ID for the next order

# LEVEL 1 – Menu CRUD operations

@app.get("/menu", response_model=List[MenuItem])
def display_all(flag: bool = False):
    
# Retrieve all menu items, optionally filtered by availability.
# If flag is True, only return available menu items.
    
    if flag:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def search_byid(id: int):
    
# Retrieve a menu item by its ID.

    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem)
def create_new_item(new_item: MenuItem):

# Create a new menu item and add it to the menu.

    global next_menu_id
    next_menu_id += 1  # Increment the ID for the new item
    new_item.id = next_menu_id  # Assign the new ID to the menu item
    menu.append(new_item.dict())  # Add the new item to the menu list
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def updating_byid(id: int, new_item: MenuItem):

# Update an existing menu item by its ID.

    for item in menu:
        if item["id"] == id:

# Update only fields that are set (exclude unset fields)
            
            item.update(new_item.dict(exclude_unset=True))
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/menu/{id}")
def deleting_byid(id: int):

# Delete a menu item by its ID.

    for item in menu:
        if item["id"] == id:
            menu.remove(item)  # Remove the item from the menu list
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# LEVEL 2 – Order operations

@app.post("/orders", response_model=Order)
def creating_order(new_order: Order):

# Create a new customer order.

    global next_order_id
    next_order_id += 1  # Increment the order ID


# Validate dine-in orders (table number is required)

    if new_order.order_type == "dine_in" and (new_order.table_number is None or new_order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number must be provided for dine-in orders.")
    
# Validate each order item

    for order_item in new_order.items:
        if order_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive.")
        if not any(m["id"] == order_item.menu_item_id for m in menu):
            raise HTTPException(status_code=400, detail="Menu item not found in menu.")

    new_order.id = next_order_id  # Assign the new order ID
    orders.append(new_order)  # Add the new order to the orders list
    return new_order

@app.get("/orders", response_model=List[Order])
def display_orders(stat: str = None):
    
# Retrieve all orders, optionally filtered by their status.
    
    if stat:
        return [order for order in orders if order.status == stat]
    return orders

@app.get("/orders/{id}", response_model=Order)
def display_specific_order(id: int):
    
# Retrieve a specific order by its ID.
    
    for order in orders:
        if order.id == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# LEVEL 3 – Order Status and Total Amount

@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, change: str):

# Update the status of an order.
    
    for order in orders:
        if order.id == id:
            if order.status == "completed" or order.status == "cancelled":
                raise HTTPException(status_code=400, detail="Cannot update status for completed or cancelled orders.")
            
# Define valid status transitions
            valid_transitions = {
                "pending": ["in_progress", "cancelled"],
                "in_progress": ["completed", "cancelled"]
            }
            
            if change not in valid_transitions.get(order.status, []):
                raise HTTPException(status_code=400, detail="Illegal status transition.")
            
            order.status = change  # Update the order status
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{id}/total-amount-compute")
def get_total_bill(id: int):
    
    
# Compute the total bill for a specific order.
    
    for order in orders:
        if order.id == id:
            total_amount = sum(
                item.quantity * next(m["price"] for m in menu if m["id"] == item.menu_item_id)
                for item in order.items
            )
            return {"order_id": id, "total_amount": total_amount}
    raise HTTPException(status_code=404, detail="Order not found")





# output:

# 1. GET /menu – Retrieve all menu items

# Request: GET /menu
# Response:
# [
#     {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#     {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#     {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true},
#     {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false}
# ]

# 2. GET /menu?flag=true – Retrieve available menu items

# Request: GET /menu?flag=true
# Response:
    
# [
#     {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#     {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#     {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true}
# ]


# 3. GET /menu/{id} – Retrieve a specific menu item by ID

# Request: GET /menu/2
# Response:

# {
#     "id": 2,
#     "name": "Paneer Butter Masala",
#     "category": "main_course",
#     "price": 249.0,
#     "is_available": true
# }

# 4. POST /menu – Add a new menu item

# Request: POST /menu
# Request Body:
    
# {
#     "name": "Veg Biryani",
#     "category": "main_course",
#     "price": 199.0,
#     "is_available": true
# }

# Response:

# {
#     "id": 5,
#     "name": "Veg Biryani",
#     "category": "main_course",
#     "price": 199.0,
#     "is_available": true
# }

# 5. PUT /menu/{id} – Update an existing menu item

# Request: PUT /menu/5
# Request Body:

# {
#     "name": "Paneer Biryani",
#     "category": "main_course",
#     "price": 220.0,
#     "is_available": false
# }


# Response:

# {
#     "id": 5,
#     "name": "Paneer Biryani",
#     "category": "main_course",
#     "price": 220.0,
#     "is_available": false
# }

# 6. DELETE /menu/{id} – Delete a menu item

# Request: DELETE /menu/5
# Response:

# {
#     "detail": "Menu item deleted"
# }

# 7. POST /orders – Create a new order

# Request: POST /orders
# Request Body:

# {
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#         {"menu_item_id": 1, "quantity": 2},
#         {"menu_item_id": 3, "quantity": 3}
#     ]
# }


# Response:

# {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#         {"menu_item_id": 1, "quantity": 2},
#         {"menu_item_id": 3, "quantity": 3}
#     ],
#     "status": "pending",
#     "special_instruction": "Nothing"
# }

# 8. GET /orders – Retrieve all orders

# Request: GET /orders
# Response:

# [
#     {
#         "id": 1,
#         "order_type": "dine_in",
#         "table_number": 12,
#         "items": [
#             {"menu_item_id": 1, "quantity": 2},
#             {"menu_item_id": 3, "quantity": 3}
#         ],
#         "status": "pending",
#         "special_instruction": "Nothing"
#     }
# ]

# 9. PATCH /orders/{id}/status – Update the status of an order

# Request: PATCH /orders/1/status
# Request Body:
# "in_progress"
# Response:

# {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#         {"menu_item_id": 1, "quantity": 2},
#         {"menu_item_id": 3, "quantity": 3}
#     ],
#     "status": "in_progress",
#     "special_instruction": "Nothing"
# }

# 10. GET /orders/{id}/total-amount-compute – Compute the total amount of an order

# Request: GET /orders/1/total-amount-compute
# Response:

# {
#     "order_id": 1,
#     "total_amount": 698.0
# }


# Summary of Output:
# Menu CRUD: You can view, add, update, and delete menu items. Only available items can be filtered.
# Order CRUD: You can create orders, get details about orders, update their status, and compute the total bill based on ordered items.