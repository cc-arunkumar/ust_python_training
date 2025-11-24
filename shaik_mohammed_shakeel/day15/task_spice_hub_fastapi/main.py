# Importing necessary libraries for type hinting, API creation, and validation
from typing import List, Optional
from fastapi import FastAPI, HTTPException
import datetime
from pydantic import BaseModel

# Initialize FastAPI app with a title
app = FastAPI(title="SpiceHub")

# Global variables to keep track of next menu item and order ID
next_menu_id = 5
next_order_id = 1

# Pydantic model to define the structure for a menu item
class MenuItem(BaseModel):
    id: int  # Unique identifier for the menu item
    name: str  # Name of the menu item
    category: str  # Category like starter, main_course, dessert, etc.
    price: float  # Price of the menu item
    is_available: bool = False  # Availability of the menu item (default is False)

# Pydantic model to define the structure for an order item (menu item and quantity)
class OrderItem(BaseModel):
    menu_item_id: int  # ID of the menu item being ordered
    quantity: int  # Quantity of the menu item being ordered

# Pydantic model to define the structure for an order (list of order items, status, etc.)
class Order(BaseModel):
    id: int  # Unique identifier for the order
    order_type: str  # Type of order: 'takeaway' or 'dine_in'
    table_number: int = None  # Table number (if dine-in)
    items: List[OrderItem]  # List of order items
    status: str = "pending"  # Status of the order, default is "pending"
    special_instructions: str = None  # Optional special instructions for the order

# Sample menu data
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# List to store orders
orders = []

# Get headers from the menu items (used for checking existing menu item IDs)
headers = list(menu[0].keys())

# Route to get the entire menu, optionally filter by availability
@app.get("/menu")
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        # Filter menu to only show available items
        filtered_menu = [item for item in menu if item['is_available']]
    else:
        filtered_menu = menu  # Return entire menu
    return filtered_menu

# Route to get a single menu item by its ID
@app.get("/menu/{id}")
def get_menu_by_id(id: int):
    for row in menu:
        if row['id'] == id:
            return row  # Return the menu item if found
    raise HTTPException(status_code=404, detail="Menu item not found")  # Raise 404 if not found

# Route to add a new menu item
@app.post("/menu")
def read_menu(read: MenuItem):
    global next_menu_id
    for row in menu:
        if row[headers[0]] == read.id:
            raise HTTPException(status_code=404, detail="Menu item already exists")
    read.id = next_menu_id
    next_menu_id += 1  # Increment the menu ID for the next item
    menu.append(read)  # Add the new item to the menu
    return read  # Return the newly added item

# Route to update an existing menu item by its ID
@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, update: MenuItem):
    for row in menu:
        if row["id"] == id:
            row["name"] = update.name
            row["category"] = update.category
            row["price"] = update.price
            row["is_available"] = update.is_available
            return row  # Return the updated item
    raise HTTPException(status_code=404, detail="ID Not Found")  # Raise 404 if ID is not found

# Route to delete a menu item by its ID
@app.delete("/menu/{id}", response_model=MenuItem)
def delete_menu(id: int):
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            return menu.pop(i)  # Remove and return the deleted menu item
    raise HTTPException(status_code=404, detail="ID Not Found")  # Raise 404 if ID is not found

# Route to create a new order
@app.post('/orders', response_model=Order)
def create_order(new_order: Order):
    # Validate the items in the order
    new_list_id = [item[headers[0]] for item in menu]  # Extract menu item IDs
    for row in new_order.items:
        if row.quantity <= 0:
            raise HTTPException(status_code=400, detail="Invalid Quantity")  # Validate quantity
        if row.menu_item_id not in new_list_id:
            raise HTTPException(status_code=404, detail="Menu Item not Found!")
        for item in menu:
            if row.menu_item_id == item[headers[0]] and not item[headers[4]]:
                raise HTTPException(status_code=400, detail="Item is Not Available!")
    
    # Assign ID to the new order and append it to the orders list
    global next_order_id
    if new_order.order_type == 'takeaway':
        new_order.id = next_order_id
        next_order_id += 1
        orders.append(new_order)
        return new_order
    elif new_order.order_type == 'dine_in':
        if isinstance(new_order.table_number, int):  # Validate table number
            new_order.id = next_order_id
            next_order_id += 1
            orders.append(new_order)
            return new_order
        else:
            raise HTTPException(status_code=400, detail="Invalid Table Number")
    else:
        raise HTTPException(status_code=400, detail="Invalid Order Type")

# Route to get all orders or filter by status
@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[str] = "pending"):
    if status is not None:
        return [order for order in orders if order.status == status]
    else:
        return orders  # Return all orders

# Route to get a single order by ID
@app.get("/orders/{id}")
def get_order_id(id: int):
    for ord in orders:
        if ord.id == id:
            return ord
    raise HTTPException(status_code=404, detail="Order Not Found")

# Route to update the status of an order
@app.patch('/orders/{id}/status')
def update_status(id: int, payload: dict):
    # Find the order by ID
    order_found = next((ord for ord in orders if ord.id == id), None)
    if not order_found:
        raise HTTPException(status_code=404, detail="Order Not Found")

    # Validate the presence of the 'status' in the payload
    if "status" not in payload:
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

    # Validate that the status transition is allowed
    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(status_code=400, detail=f"Cannot transition from '{current_status}' to '{new_status}'")

    # Update the order status
    order_found.status = new_status
    return order_found

# Route to calculate the total amount of an order
@app.get('/orders/{id}/total-amount')
def get_order_total(id: int):
    # Find the order by ID
    order_found = next((ord for ord in orders if ord.id == id), None)
    if not order_found:
        raise HTTPException(status_code=404, detail="Order Not Found")

    # Calculate the total amount for the order
    total_amount = 0.0
    for order_item in order_found.items:
        menu_item = next((item for item in menu if item['id'] == order_item.menu_item_id), None)
        if menu_item:
            total_amount += menu_item['price'] * order_item.quantity

    return {"order_id": id, "total_amount": total_amount}  # Return the total amount for the order


#sample output
# 1. GET /menu: Retrieve the entire menu or only available items
# Request (URL)
# GET /menu?only_available=true

# Response (JSON)
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
#   }
# ]

# 2. GET /menu/{id}: Retrieve a specific menu item by its ID
# Request (URL)
# GET /menu/1

# Response (JSON)
# {
#   "id": 1,
#   "name": "Tomato Soup",
#   "category": "starter",
#   "price": 99.0,
#   "is_available": true
# }

# 3. POST /menu: Add a new menu item
# Request (JSON Body)
# {
#   "id": 5,
#   "name": "Mango Lassi",
#   "category": "drink",
#   "price": 89.0,
#   "is_available": true
# }

# Response (JSON)
# {
#   "id": 5,
#   "name": "Mango Lassi",
#   "category": "drink",
#   "price": 89.0,
#   "is_available": true
# }

# 4. PUT /menu/{id}: Update an existing menu item by ID
# Request (URL)
# PUT /menu/3

# Request (JSON Body)
# {
#   "id": 3,
#   "name": "Butter Naan",
#   "category": "main_course",
#   "price": 59.0,
#   "is_available": true
# }

# Response (JSON)
# {
#   "id": 3,
#   "name": "Butter Naan",
#   "category": "main_course",
#   "price": 59.0,
#   "is_available": true
# }

# 5. DELETE /menu/{id}: Delete a menu item by ID
# Request (URL)
# DELETE /menu/4

# Response (JSON)
# {
#   "id": 4,
#   "name": "Gulab Jamun",
#   "category": "dessert",
#   "price": 79.0,
#   "is_available": false
# }

# 6. POST /orders: Create a new order
# Request (JSON Body)
# {
#   "order_type": "takeaway",
#   "items": [
#     {
#       "menu_item_id": 1,
#       "quantity": 2
#     },
#     {
#       "menu_item_id": 2,
#       "quantity": 1
#     }
#   ]
# }

# Response (JSON)
# {
#   "id": 1,
#   "order_type": "takeaway",
#   "table_number": null,
#   "items": [
#     {
#       "menu_item_id": 1,
#       "quantity": 2
#     },
#     {
#       "menu_item_id": 2,
#       "quantity": 1
#     }
#   ],
#   "status": "pending",
#   "special_instructions": null
# }

# 7. GET /orders: Retrieve all orders or filter by status
# Request (URL)
# GET /orders?status=pending

# Response (JSON)
# [
#   {
#     "id": 1,
#     "order_type": "takeaway",
#     "table_number": null,
#     "items": [
#       {
#         "menu_item_id": 1,
#         "quantity": 2
#       },
#       {
#         "menu_item_id": 2,
#         "quantity": 1
#       }
#     ],
#     "status": "pending",
#     "special_instructions": null
#   }
# ]

# 8. GET /orders/{id}: Get a single order by its ID
# Request (URL)
# GET /orders/1

# Response (JSON)
# {
#   "id": 1,
#   "order_type": "takeaway",
#   "table_number": null,
#   "items": [
#     {
#       "menu_item_id": 1,
#       "quantity": 2
#     },
#     {
#       "menu_item_id": 2,
#       "quantity": 1
#     }
#   ],
#   "status": "pending",
#   "special_instructions": null
# }

# 9. PATCH /orders/{id}/status: Update the status of an order
# Request (URL)
# PATCH /orders/1/status

# Request (JSON Body)
# {
#   "status": "in_progress"
# }

# Response (JSON)
# {
#   "id": 1,
#   "order_type": "takeaway",
#   "table_number": null,
#   "items": [
#     {
#       "menu_item_id": 1,
#       "quantity": 2
#     },
#     {
#       "menu_item_id": 2,
#       "quantity": 1
#     }
#   ],
#   "status": "in_progress",
#   "special_instructions": null
# }

# 10. GET /orders/{id}/total-amount: Calculate the total amount of an order
# Request (URL)
# GET /orders/1/total-amount

# Response (JSON)
# {
#   "order_id": 1,
#   "total_amount": 447.0
# }

