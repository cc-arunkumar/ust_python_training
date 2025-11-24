# problem statement

# 1. Scenario
# You are building a small REST API for a restaurant called “SpiceHub”.
# The API will help restaurant staff to:
# 1. Manage the menu (add, view, update, delete dishes).
# 2. Take orders from customers (dine-in or takeaway).
# 3. Track order status (pending → in_progress → completed / cancelled).
# 4. Calculate total bill for an order.
# Everything is stored in memory (Python lists/dicts).
# No database. If server restarts, data is lost (this is ok for practice).
# 2. Data model (fixed, simple, clearly defined)
# 2.1 MenuItem
# Represents one dish in the restaurant menu.
# Fields:
# id: int — unique, auto-incremented (1,2,3,...)
# name: str — dish name, e.g. "Paneer Butter Masala"
# category: str — e.g. "starter" , "main_course" , "dessert" , "beverage"
# price: float — price per unit, e.g. 249.0
# is_available: bool — true if dish can be ordered now
# 2.2 OrderItem
# Represents one line item inside an order.
# Fields:
# menu_item_id: int — refers to a MenuItem.id
# quantity: int — number of units ordered (e.g. 2 plates)
# 2.3 Order
# Represents a whole customer order.
# Fields:
# id: int — unique order id, auto-incremented
# order_type: str — "dine_in" or "takeaway"
# table_number: int | null
# Required for dine_in
# Must be null for takeaway
# items: List[OrderItem] — list of items in this order
# status: str — "pending" , "in_progress" , "completed" , "cancelled"
# Initial value: "pending"
# special_instructions: str | null — e.g. "less spicy" , can be empty/null
# 3. In-memory data (starting point)
# Participants should start with these in-memory lists & counters in main.py :
# menu = [
#  {
#  "id": 1,
#  "name": "Tomato Soup",
#  "category": "starter",
#  "price": 99.0,
#  "is_available": True
#  },
# Day 15 2
#  {
#  "id": 2,
#  "name": "Paneer Butter Masala",
#  "category": "main_course",
#  "price": 249.0,
#  "is_available": True
#  },
#  {
#  "id": 3,
#  "name": "Butter Naan",
#  "category": "main_course",
#  "price": 49.0,
#  "is_available": True
#  },
#  {
#  "id": 4,
#  "name": "Gulab Jamun",
#  "category": "dessert",
#  "price": 79.0,
#  "is_available": False
#  }
# ]
# orders = [] # list of Order dicts
# next_menu_id = 5
# next_order_id = 1
# 4. Tasks for participants (step-by-step)
# You can give these as “Level 1 / 2 / 3” tasks.
# LEVEL 1 Menu CRUD
# 4.1 GET /menu list all menu items
# 3 No input body.
# Optional query param: only_available: bool (default false).
# If only_available=true → return only items where is_available == True .
# 4.2 GET /menu/{id} – get single menu item
# Behavior:
# If id exists → return that item.
# If not found → 404 with {"detail": "Menu item not found"} .
# 4.3 POST /menu – add new menu items
# Behavior:
# Server assigns id = next_menu_id .
# Appends to menu list.
# Increments next_menu_id .
# Returns created item with 201 status.
# 4.4 PUT /menu/{id} – update existing menu item (full replace)
# Behavior:
# Replace all fields except id .
# If item does not exist → 404.
# Return updated item.
# 4.5 DELETE /menu/{id} – delete menu item
# Behavior:
# If item exists → remove from list, return {"detail": "Menu item deleted"} .
# If not found → 404.
# LEVEL 2 – Orders (Create + Read)
# 4.6 POST /orders – create new order
# Rules (keep simple but clear):
# order_type must be "dine_in" or "takeaway" .
# For "dine_in" : table_number must be a positive integer (e.g. 1,2,3...).
# For "takeaway" : table_number must be null or 0 (you decide; specify clearly).
# Every menu_item_id must exist in menu .
# Items with quantity <= 0 should be rejected.
# If a menu_item_id refers to an item with is_available == false , allow it or reject it?
# → For this task: reject, with 400.
# Behavior:
# If any rule fails → 400 with clear message.
# Otherwise:
# Assign id = next_order_id .
# Set status = "pending" .
# Append to orders .
# Increment next_order_id .
# Return full order.
# 4.7 GET /orders – list all orders
# Optional query param: status
# If provided, return only orders with that status.
# Else, return all.
# Example: GET /orders?status=pending
# Response: array of orders.
# 4.8 GET /orders/{id} – get single order
# If exists → return the order.
# If not → 404 {"detail":"Order not found"} .
# LEVEL 3 – Order status + total (small but realistic)
# 4.9 PATCH /orders/{id}/status – update only status
# Request body:
# { "status": "in_progress" }
# Allowed transitions (to keep logic simple but real):
# "pending" → "in_progress" or "cancelled"
# "in_progress" → "completed" or "cancelled"
# From "completed" or "cancelled" → no further change allowed (return 400).
# Behavior:
# If order not found → 404.
# If status invalid or illegal transition → 400.
# Else update status and return updated order.
# 4.10 GET /orders/{id}/total-amount – compute bill
# Behavior:
# Find order by id.
# If not found → 404.
# For each OrderItem in items :
# Find corresponding MenuItem by menu_item_id .
# Multiply menu_item.price * quantity .
# Sum all line totals.
# Return JSON
# 5. How you can present this as tasks
# You can give them in stages like:
# Task Set 1 – Menu API
# 1. Create MenuItem Pydantic model.
# 2. Implement /menu GET all + GET by id.
# 3. Implement /menu POST, PUT, DELETE.
# 4. Test using /docs with sample data.
# Task Set 2 – Orders API
# 1. Create OrderItem and Order models.
# 2. Implement /orders POST with validation rules.
# 3. Implement /orders GET all + GET by id.
# Task Set 3 – Status & Totals
# Day 15 9
# 1. Implement /orders/{id}/status PATCH with allowed transitions.
# 2. Implement /orders/{id}/total-amount GET.
# One sample execution with expected output
# Here is a complete example: creating a dine-in order and the expected JSON
# response.
# Request
# Endpoint: POST /orders
# Expected output (with current menu prices):
# Tomato Soup (id 1): 99.0 × 2 = 198.0
# Butter Naan (id 3): 49.0 × 4 = 196.0
# Total = 394.0



from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Initialize FastAPI app with a title
app = FastAPI(title="Spice Hub")

# -------------------------------
# Pydantic Models (Data Schemas)
# -------------------------------

class MenuItem(BaseModel):
    """Represents a menu item in the restaurant."""
    id: int
    name: str
    category: str   # e.g., starter, main_course, dessert
    price: float
    is_available: bool   # Availability flag

class OrderItem(BaseModel):
    """Represents a single item in an order."""
    menu_item_id: int    # Reference to MenuItem by ID
    quantity: int        # Number of units ordered

class Order(BaseModel):
    """Represents a customer order."""
    id: int
    order_type: str      # e.g., 'dine_in' or 'takeaway'
    table_number: int = None   # Required for dine-in orders
    items: List[OrderItem]     # List of ordered items
    status: str = "pending"    # Default status
    special_instruction: str = "Nothing"   # Optional notes

# -------------------------------
# In-memory Data Storage
# -------------------------------

# Menu items (mock database)
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders: List[Order] = []   # Stores all orders
next_menu_id = 4           # Tracks last menu item ID
next_order_id = 0          # Tracks last order ID

# -------------------------------
# LEVEL 1 – Menu CRUD Operations
# -------------------------------

@app.get("/menu", response_model=List[MenuItem])
def display_all(flag: bool = False):
    """
    Display all menu items.
    If 'flag' is True, only return items that are available.
    """
    if flag:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def search_byid(id: int):
    """
    Search for a menu item by its ID.
    Raises 404 if not found.
    """
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem)
def create_new_item(new_item: MenuItem):
    """
    Create a new menu item.
    Automatically assigns a new ID.
    """
    global next_menu_id
    next_menu_id += 1
    new_item.id = next_menu_id
    menu.append(new_item.dict())
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def updating_byid(id: int, new_item: MenuItem):
    """
    Update an existing menu item by ID.
    Only updates fields provided in request.
    """
    for item in menu:
        if item["id"] == id:
            item.update(new_item.dict(exclude_unset=True))
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/menu/{id}")
def deleting_byid(id: int):
    """
    Delete a menu item by its ID.
    Raises 404 if not found.
    """
    for item in menu:
        if item["id"] == id:
            menu.remove(item)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# -------------------------------
# LEVEL 2 – Orders
# -------------------------------

@app.post("/orders", response_model=Order)
def creating_order(new_order: Order):
    """
    Create a new order.
    - Validates dine-in orders must have a table number.
    - Validates item quantities and menu existence.
    """
    global next_order_id
    next_order_id += 1

    # Validation for dine-in orders
    if new_order.order_type == "dine_in" and (new_order.table_number is None or new_order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number must be provided for dine-in orders.")
    
    # Validate order items
    for order_item in new_order.items:
        if order_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive.")
        if not any(m["id"] == order_item.menu_item_id for m in menu):
            raise HTTPException(status_code=400, detail="Menu item not found in menu.")

    # Assign ID and save order
    new_order.id = next_order_id
    orders.append(new_order)
    return new_order

@app.get("/orders", response_model=List[Order])
def display_orders(stat: str = None):
    """
    Display all orders.
    Optionally filter by status (e.g., 'pending', 'completed').
    """
    if stat:
        return [order for order in orders if order.status == stat]
    return orders

@app.get("/orders/{id}", response_model=Order)
def display_specific_order(id: int):
    """
    Get a specific order by its ID.
    Raises 404 if not found.
    """
    for order in orders:
        if order.id == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# -------------------------------
# LEVEL 3 – Order Status + Billing
# -------------------------------

@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, change: str):
    """
    Update the status of an order.
    - Prevents updates if already 'completed' or 'cancelled'.
    - Enforces valid status transitions:
        pending -> in_progress / cancelled
        in_progress -> completed / cancelled
    """
    for order in orders:
        if order.id == id:
            if order.status in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="Cannot update status for completed or cancelled orders.")
            
            valid_transitions = {
                "pending": ["in_progress", "cancelled"],
                "in_progress": ["completed", "cancelled"]
            }
            
            if change not in valid_transitions.get(order.status, []):
                raise HTTPException(status_code=400, detail="Illegal status transition.")
            
            order.status = change
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{id}/total-amount-compute")
def get_total_bill(id: int):
    """
    Compute the total bill for an order.
    Multiplies item quantity by menu price.
    """
    for order in orders:
        if order.id == id:
            total_amount = sum(
                item.quantity * next(m["price"] for m in menu if m["id"] == item.menu_item_id)
                for item in order.items
            )
            return {"order_id": id, "total_amount": total_amount}

    raise HTTPException(status_code=404, detail="Order not found")



# Sample Requests and Expected Outputs
# 1. Get all menu items
# Request:
# GET /menu
# Response:
# [
#   {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#   {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#   {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true},
#   {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false}
# ]
# 2. Get only available menu items
# Request:
# GET /menu?flag=true
# Response:
# [
#   {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#   {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#   {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true}
# ]
# 3. Search menu item by ID
# Request:
# GET /menu/2
# Response:
# {
#   "id": 2,
#   "name": "Paneer Butter Masala",
#   "category": "main_course",
#   "price": 249.0,
#   "is_available": true
# }
# 4. Create new menu item
# POST /menu
# Body:
# {
#   "id": 0,
#   "name": "Veg Biryani",
#   "category": "main_course",
#   "price": 199.0,
#   "is_available": true
# }
# Response:
# {
#   "id": 5,
#   "name": "Veg Biryani",
#   "category": "main_course",
#   "price": 199.0,
#   "is_available": true
# }
# 5. Update menu item
# Request:
# PUT /menu/3
# Body:
# {
#   "id": 3,
#   "name": "Garlic Naan",
#   "category": "main_course",
#   "price": 59.0,
#   "is_available": true
# }
# Response:
# {
#   "id": 3,
#   "name": "Garlic Naan",
#   "category": "main_course",
#   "price": 59.0,
#   "is_available": true
# }
# 6. Delete menu item
# Request:
# DELETE /menu/4
# Response:
# {"detail": "Menu item deleted"}
# LEVEL 2 – Orders
# 1. Create new order
# Request:
# POST /orders
# {
#   "id": 0,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "special_instruction": "Extra butter on naan"
# }
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "status": "pending",
#   "special_instruction": "Extra butter on naan"
# }
# 2. Get all orders
# Request:
# GET /orders
# Response:
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#       {"menu_item_id": 1, "quantity": 2},
#       {"menu_item_id": 3, "quantity": 4}
#     ],
#     "status": "pending",
#     "special_instruction": "Extra butter on naan"
#   }
# ]
# 3. Get specific order
# Request:
# GET /orders/1
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "status": "pending",
#   "special_instruction": "Extra butter on naan"
# }
# LEVEL 3 – Status + Billing
# 1. Update order status
# Request:
# PATCH /orders/1/status?change=in_progress
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 1, "quantity": 2},
#     {"menu_item_id": 3, "quantity": 4}
#   ],
#   "status": "in_progress",
#   "special_instruction": "Extra butter on naan"
# }
# 2. Compute total bill
# Request:
# GET /orders/1/total-amount-compute
# Response:
# {
#   "order_id": 1,
#   "total_amount": 394.0
# }