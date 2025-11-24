
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
# For this practice: no date/time fields to keep life simple.
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
# LEVEL 1 – Menu CRUD
# 4.1 GET /menu – list all menu items

# No input body.
# Optional query param: only_available: bool (default false).
# If only_available=true → return only items where is_available == True .
# Else → return all items.
# Example request:
# GET /menu
# Example response:
# [
#  {
#  "id": 1,
#  "name": "Tomato Soup",
#  "category": "starter",
#  "price": 99.0,
#  "is_available": true
#  },
#  ...
# ]
# 4.2 GET /menu/{id} – get single menu item
# Behavior:
# If id exists → return that item.
# If not found → 404 with {"detail": "Menu item not found"} .
# 4.3 POST /menu – add new menu item
# Request body (example):
# {
#  "name": "Masala Dosa",
#  "category": "main_course",
#  "price": 129.0,
# Day 15 4
#  "is_available": true
# }
# Behavior:
# Server assigns id = next_menu_id .
# Appends to menu list.
# Increments next_menu_id .
# Returns created item with 201 status.
# Example response:
# {
#  "id": 5,
#  "name": "Masala Dosa",
#  "category": "main_course",
#  "price": 129.0,
#  "is_available": true
# }
# 4.4 PUT /menu/{id} – update existing menu item (full replace)
# Request body example:
# {
#  "name": "Butter Naan (Large)",
#  "category": "main_course",
#  "price": 69.0,
#  "is_available": true
# }
# Behavior:
# Replace all fields except id .
# If item does not exist → 404.
# Day 15 5
# Return updated item.
# 4.5 DELETE /menu/{id} – delete menu item
# Behavior:
# If item exists → remove from list, return {"detail": "Menu item deleted"} .
# If not found → 404.
# LEVEL 2 – Orders (Create + Read)
# 4.6 POST /orders – create new order
# Request body example (dine-in):
# {
#  "order_type": "dine_in",
#  "table_number": 12,
#  "items": [
#  { "menu_item_id": 1, "quantity": 2 },
#  { "menu_item_id": 3, "quantity": 4 }
#  ],
#  "special_instructions": "less spicy"
# }
# Request body example (takeaway):
# {
#  "order_type": "takeaway",
#  "table_number": null,
#  "items": [
#  { "menu_item_id": 2, "quantity": 1 }
#  ],
#  "special_instructions": ""
# }
# Rules (keep simple but clear):
# Day 15 6
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
# Example response:
# {
#  "id": 1,
#  "order_type": "dine_in",
#  "table_number": 12,
#  "items": [
#  { "menu_item_id": 1, "quantity": 2 },
#  { "menu_item_id": 3, "quantity": 4 }
#  ],
#  "status": "pending",
#  "special_instructions": "less spicy"
# }

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
# Day 15 8
# Find order by id.
# If not found → 404.
# For each OrderItem in items :
# Find corresponding MenuItem by menu_item_id .
# Multiply menu_item.price * quantity .
# Sum all line totals.
# Return JSON:
# {
#  "order_id": 1,
#  "total_amount": 693.0
# }
# (Example number; actual sum depends on data.)

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

# 1. Implement /orders/{id}/status PATCH with allowed transitions.
# 2. Implement /orders/{id}/total-amount GET.
# One sample execution with expected output
# Here is a complete example: creating a dine-in order and the expected JSON
# response.
# Request
# Endpoint: POST /orders
# Body (JSON):
# {
#  "order_type": "dine_in",
#  "table_number": 12,
#  "items": [
#  { "menu_item_id": 1, "quantity": 2 },
#  { "menu_item_id": 3, "quantity": 4 }
#  ],
#  "special_instructions": "less spicy"
# }
# You can send this via:
# Swagger UI ( /docs → POST /orders → “Try it out”), or
# Any REST client (Postman, curl, etc.)
# Expected Response (201 Created)
# {
#  "id": 1,
#  "order_type": "dine_in",
#  "table_number": 12,
# Day 15 10
#  "items": [
#  {
#  "menu_item_id": 1,
#  "quantity": 2
#  },
#  {
#  "menu_item_id": 3,
#  "quantity": 4
#  }
#  ],
#  "special_instructions": "less spicy",
#  "status": "pending"
# }
# You can then call:
# GET /orders/1/total-amount
# Expected output (with current menu prices):
# Tomato Soup (id 1): 99.0 × 2 = 198.0
# Butter Naan (id 3): 49.0 × 4 = 196.0
# Total = 394.0
# Response:
# {
#  "order_id": 1,
#  "total_amount": 394.0


# Import required libraries
from fastapi import FastAPI, HTTPException  # FastAPI for API creation, HTTPException for error handling
from pydantic import BaseModel  # Pydantic BaseModel for data validation
from typing import List, Optional  # List for handling arrays and Optional for optional fields
from datetime import date, datetime, time  # Importing datetime utilities (though not used here directly)


# Initialize the FastAPI application
app = FastAPI(title="SpiceHub")  # Title for the API


# In-memory data to store menu items and orders
menu_list = [
    {
        "id": 1,
        "name": "Tomato Soup",
        "category": "starter",
        "price": 99.0,
        "is_available": True  # Whether the item is available
    },
    {
        "id": 2,
        "name": "Paneer Butter Masala",
        "category": "main_course",
        "price": 249.0,
        "is_available": True  # Whether the item is available
    },
    {
        "id": 3,
        "name": "Butter Naan",
        "category": "main_course",
        "price": 49.0,
        "is_available": True  # Whether the item is available
    },
    {
        "id": 4,
        "name": "Gulab Jamun",
        "category": "dessert",
        "price": 79.0,
        "is_available": False  # Not available
    }
]

# List to store orders (in-memory)
orders = []  # List of Order dicts, initially empty

# Auto-incremented IDs for the next menu and order
next_menu_id = 5  # Menu items will start from ID 5
next_order_id = 1  # Orders will start from ID 1


# Pydantic models for data validation and request/response handling

# Model for MenuItem (represents a dish in the menu)
class MenuItem(BaseModel):
    id: int  # Unique identifier for the menu item
    name: str  # Name of the menu item
    category: str  # Category (starter, main_course, etc.)
    price: float  # Price of the item
    is_available: bool = True  # Whether the item is available, defaults to True

# Model for creating a new MenuItem (when adding a new dish)
class CreateMenu(BaseModel):
    name: str  # Name of the menu item
    category: str  # Category of the dish
    price: float  # Price of the dish

# Model for updating an existing MenuItem (when modifying a dish)
class UpdateMenu(BaseModel):
    name: str  # Updated name of the menu item
    category: str  # Updated category
    price: float  # Updated price
    is_available: bool  # Updated availability status


# Model for an order item (an item in the order, with a quantity)
class OrderItem(BaseModel):
    menu_item_id: int  # ID of the menu item being ordered
    quantity: int  # Quantity of the item being ordered


# Model for Order (represents a customer order)
class Order(BaseModel):
    id: int  # Unique order ID
    order_type: str  # Type of order: "dine_in" or "takeaway"
    table_number: int = None  # Only required for "dine_in" orders
    items: List[OrderItem]  # List of items in the order
    status: str = "pending"  # Default order status is "pending"
    special_instructions: str = None  # Special instructions for the order, optional


# Model for creating a new order
class CreateOrder(BaseModel):
    order_type: str  # Type of order: "dine_in" or "takeaway"
    table_number: int = None  # Table number, required for dine-in
    items: List[OrderItem]  # List of items in the order
    special_instructions: str = None  # Optional field for special instructions


# Endpoint to add a new menu item to the menu list
@app.post("/menu", response_model=MenuItem)
def add_menu_item(menu: CreateMenu):
    global next_menu_id
    # Create a new menu item based on the input data
    new_menu = MenuItem(id=next_menu_id, name=menu.name, category=menu.category, price=menu.price)
    # Append the new menu item to the menu list
    menu_list.append(new_menu.dict())
    next_menu_id += 1  # Increment the next menu ID for the next item
    return new_menu  # Return the created menu item


# Endpoint to get all menu items, with an optional filter for availability
@app.get("/menu", response_model=List[MenuItem])
def get_all_menu_items(is_available: Optional[bool] = False):
    filtered_list = []
    if is_available is False:
        return menu_list  # If no filter, return all items
    # Filter menu items based on availability
    for data in menu_list:
        if data["is_available"] == is_available:
            filtered_list.append(data)
    return filtered_list  # Return the filtered list based on availability


# Endpoint to get a specific menu item by ID
@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item_by_id(id: int):
    # Loop through menu items and find the one matching the ID
    for data in menu_list:
        if data["id"] == id:
            return data
    # If menu item with the given ID is not found, raise an error
    raise HTTPException(status_code=404, detail="Menu Not Found")


# Endpoint to update an existing menu item by ID
@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, update_menu: UpdateMenu):
    updated = get_menu_item_by_id(id)  # Check if the item exists
    if updated:
        # Create a new MenuItem object with the updated data
        new_changes = MenuItem(
            id=id,
            name=update_menu.name,
            category=update_menu.category,
            price=update_menu.price,
            is_available=update_menu.is_available
        )
        # Loop through the menu list and replace the old menu item with the updated one
        for i in range(len(menu_list)):
            if menu_list[i]["id"] == id:
                menu_list[i] = new_changes.dict()  # Update the existing menu item
                return new_changes  # Return the updated menu item
    else:
        # If menu item not found, raise an error
        raise HTTPException(status_code=404, detail="Not Found")


# Endpoint to delete a menu item by ID
@app.delete("/menu/{id}", response_model=MenuItem)
def delete_menu(id: int):
    if get_menu_item_by_id(id):
        # Remove the menu item from the list
        return menu_list.pop(id - 1)  # Delete the menu item
    else:
        # If menu item not found, raise an error
        raise HTTPException(status_code=404, detail="Not Found")


# Endpoint to create a new order
@app.post("/order", response_model=Order)
def add_order(order: CreateOrder):
    # Validate order based on the order type
    if order.order_type == "dine_in" and order.table_number <= 0:
        raise HTTPException(status_code=400, detail="Table number must be provided for dine-in orders")
    if order.order_type == "takeaway" and order.table_number > 0:
        raise HTTPException(status_code=400, detail="Table number should not be provided for take-away orders")
    
    # Check if each item in the order is available
    for data in order.items:
        if not get_menu_item_by_id(data.menu_item_id)["is_available"]:
            raise HTTPException(status_code=400, detail="Item not available")
    
    global next_order_id
    # Create a new order object based on the input data
    new_order = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_number=order.table_number,
        items=order.items,
        special_instructions=order.special_instructions
    )
    orders.append(new_order.dict())  # Append the new order to the orders list
    next_order_id += 1  # Increment the next order ID for the next order
    return new_order  # Return the created order


# Endpoint to get all orders, with optional filtering by status
@app.get("/orders", response_model=List[Order])
def get_all_orders(status: Optional[str] = "pending"):
    filtered_orders = [data for data in orders if data["status"] == status]
    return filtered_orders  # Return the filtered orders based on the status


# Endpoint to get a specific order by ID
@app.get("/orders/{id}", response_model=Order)
def get_orders(id: int):
    for data in orders:
        if data["id"] == id:
            return data  # Return the order if ID matches
    raise HTTPException(status_code=404, detail="Not Found")  # If not found, raise 404


# Endpoint to update the status of a specific order
@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, status: str):
    if get_orders(id):
        for i in range(len(orders)):
            if orders[i]["id"] == id:
                if orders[i]["status"] == "pending" and status != "completed":
                    orders[i]["status"] = status  # Change status to the new status
                elif orders[i]["status"] == "in_progress" and status != "in_progress":
                    orders[i]["status"] = status  # Change status to the new status
                else:
                    if orders[i]["status"] in ["completed", "cancelled"]:
                        raise HTTPException(status_code=400, detail="Order already completed or cancelled")
        return get_orders(id)  # Return the updated order


# Endpoint to calculate total amount for an order
@app.get("/orders/{id}/totalamount")
def calculate_total(id: int):
    if get_orders(id):
        data = get_orders(id)
        total = 0
        for row in data["items"]:
            menu = get_menu_item_by_id(row.menu_item_id)  # Get menu item by ID
            total += row.quantity * menu["price"]  # Calculate total for each item in the order
        return {"Total Bill": total}  # Return the total bill for the order


#outputs

# 1. POST /menu - Add a New Menu Item
#  Request:
# {
#   "name": "Masala Dosa",
#   "category": "main_course",
#   "price": 129.0
# }
# Response:
# {
#   "id": 5,
#   "name": "Masala Dosa",
#   "category": "main_course",
#   "price": 129.0,
#   "is_available": true
# }

# 2. GET /menu - Get All Menu Items 

# Response:
# [
#   {
#     "id": 1,
#     "name": "Tomato Soup",
#     "category": "starter",
#     "price": 99.0,
#     "is_available": true
#   },
#   {
#     "id": 2,
#     "name": "Paneer Butter Masala",
#     "category": "main_course",
#     "price": 249.0,
#     "is_available": true
#   },
#   {
#     "id": 3,
#     "name": "Butter Naan",
#     "category": "main_course",
#     "price": 49.0,
#     "is_available": true
#   },
#   {
#     "id": 4,
#     "name": "Gulab Jamun",
#     "category": "dessert",
#     "price": 79.0,
#     "is_available": false
#   },
#   {
#     "id": 5,
#     "name": "Masala Dosa",
#     "category": "main_course",
#     "price": 129.0,
#     "is_available": true
#   }
# ]


# 3. GET /menu/{id} - Get Menu Item by ID
# Response:
# {
#   "id": 3,
#   "name": "Butter Naan",
#   "category": "main_course",
#   "price": 49.0,
#   "is_available": true
# }

# 4. PUT /menu/{id} - Update Menu Item by ID
# Request:
# {
#   "name": "Butter Naan (Large)",
#   "category": "main_course",
#   "price": 69.0,
#   "is_available": true
# }
# Response:
# {
#   "id": 3,
#   "name": "Butter Naan (Large)",
#   "category": "main_course",
#   "price": 69.0,
#   "is_available": true
# }

# 5. DELETE /menu/{id} - Delete Menu Item by ID
# Response:
# {
#   "id": 4,
#   "name": "Gulab Jamun",
#   "category": "dessert",
#   "price": 79.0,
#   "is_available": false
# }

# 6. POST /order - Create a New Order
# Request:
# {
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 2, "quantity": 1 }
#   ],
#   "special_instructions": "Less spicy"
# }
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 2, "quantity": 1 }
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy"
# }

# 7. GET /orders - Get All Orders
# Response:
#  [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#       { "menu_item_id": 1, "quantity": 2 },
#       { "menu_item_id": 2, "quantity": 1 }
#     ],
#     "status": "pending",
#     "special_instructions": "Less spicy"
#   }
# ]


# 8. GET /orders/{id} - Get Order by ID
# Response:
#  {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 2, "quantity": 1 }
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy"
# }

# 9. PATCH /orders/{id}/status - Update Order Status
# Request:
# {
#   "status": "in_progress"
# }
# Response:
#  {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 2, "quantity": 1 }
#   ],
#   "status": "in_progress",
#   "special_instructions": "Less spicy"
# }
