from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# MenuItem class to define the structure of menu items (used for request validation)
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool

# OrderItem class to define the structure of items in an order
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Order class to define the structure of a customer's order
class Order(BaseModel):
    id: int
    order_type: str
    table_number: Optional[int]
    items: List[OrderItem]
    status: str
    special_instructions: Optional[str]

# Sample menu data with some initial items
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# A list to store orders
orders = []
next_menu_id = 5  # Incremental id for new menu items
next_order_id = 1  # Incremental id for new orders

# Get the entire menu or just available items based on the query parameter 'only_available'
@app.get("/menu")
def get_menu(only_available: bool = False):
    # If 'only_available' is True, return only available menu items
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu

# Get a specific menu item by id
@app.get("/menu/{id}")
def get_menu_item(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(404, "Menu item not found")

# Create a new menu item, incrementing the next_menu_id
@app.post("/menu", status_code=201)
def create_menu_item(item: dict):
    global next_menu_id

    # Assign the new menu item a unique id
    item["id"] = next_menu_id
    next_menu_id += 1

    menu.append(item)
    return item

# Update an existing menu item by id
@app.put("/menu/{id}")
def update_menu_item(id: int, data: dict):
    for i, item in enumerate(menu):
        if item["id"] == id:
            updated = data.copy()
            updated["id"] = id
            menu[i] = updated
            return updated
    raise HTTPException(404, "Menu item not found")

# Delete a menu item by id
@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for i, item in enumerate(menu):
        if item["id"] == id:
            del menu[i]
            return {"detail": "Menu item deleted"}
    raise HTTPException(404, "Menu item not found")

# Create a new order
@app.post("/orders", status_code=201)
def create_order(order: dict):
    global next_order_id

    # Validate the order type (dine_in or takeaway)
    if order["order_type"] not in ["dine_in", "takeaway"]:
        raise HTTPException(400, "Invalid order_type")

    # Validate table number for dine-in orders
    if order["order_type"] == "dine_in":
        if not isinstance(order["table_number"], int) or order["table_number"] <= 0:
            raise HTTPException(400, "table_number must be positive integer for dine_in")
    else:
        # Validate that table_number is null or 0 for takeaway orders
        if order["table_number"] not in [None, 0]:
            raise HTTPException(400, "table_number must be null or 0 for takeaway")

    # Validate each order item
    for item in order["items"]:
        if item["quantity"] <= 0:
            raise HTTPException(400, "Quantity must be > 0")

        # Find the corresponding menu item
        m = next((x for x in menu if x["id"] == item["menu_item_id"]), None)
        if not m:
            raise HTTPException(400, f"Menu item {item['menu_item_id']} does not exist")

        # Check if the item is available
        if not m["is_available"]:
            raise HTTPException(400, f"Menu item {m['name']} is not available")

    # Create a new order
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

# List all orders, optionally filtered by status
@app.get("/orders")
def list_orders(status: Optional[str] = None):
    if status:
        return [o for o in orders if o["status"] == status]
    return orders

# Get details of a specific order by id
@app.get("/orders/{id}")
def get_order(id: int):
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(404, "Order not found")

# Update the status of an order
@app.patch("/orders/{id}/status")
def update_order_status(id: int, data: dict):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(404, "Order not found")

    new_status = data["status"]
    current = order["status"]

    # Valid transitions for order statuses
    transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }

    # Check if the status transition is valid
    if new_status not in transitions[current]:
        raise HTTPException(400, "Invalid status transition")

    order["status"] = new_status
    return order

# Calculate and return the total amount for a specific order
@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(404, "Order not found")

    total = 0
    # Calculate the total by summing the price of each item multiplied by the quantity
    for item in order["items"]:
        m = next(m for m in menu if m["id"] == item["menu_item_id"])
        total += m["price"] * item["quantity"]

    return {"order_id": id, "total_amount": total}


# ------------------------------------------------------------------------------------

# Sample Output

# 1. GET /menu
# Request:
# GET /menu


# Response:
# [
#   {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#   {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#   {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true},
#   {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false}
# ]



# 2. GET /menu?only_available=true
# Request:
# GET /menu?only_available=true

# Response:
# [
#   {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#   {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#   {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true}
# ]


# 3. POST /orders (create a dine-in order)
# Request body:
# {
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 2, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "special_instructions": "Less spicy"
# }

# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 2, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "special_instructions": "Less spicy",
#   "status": "pending"
# }



# 4. GET /orders
# Request:
# GET /orders

# Response:
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       {"menu_item_id": 2, "quantity": 2},
#       {"menu_item_id": 3, "quantity": 4}
#     ],
#     "special_instructions": "Less spicy",
#     "status": "pending"
#   }
# ]



# 5. PATCH /orders/1/status (update status to in_progress)
# Request body:
# {"status": "in_progress"}

# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 5,
#   "items": [
#     {"menu_item_id": 2, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "special_instructions": "Less spicy",
#   "status": "in_progress"
# }

# 6. GET /orders/1/total-amount
# Request:
# GET /orders/1/total-amount

# Response:
# {
#   "order_id": 1,
#   "total_amount": 694.0
# }

# (Calculation: 2 × 249.0 + 4 × 49.0 = 498 + 196 = 694.0)
