# restaurant management
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(title="SpiceHub Restaurant API")

# In-memory data storage
# NOTE: For production, replace in-memory data storage with a persistent database (e.g., PostgreSQL, MongoDB)
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders = []  # Order data storage
next_menu_id = 5  # To generate unique menu IDs
next_order_id = 1  # To generate unique order IDs


# Pydantic models to validate input data

class MenuItem(BaseModel):
    id: int  # Unique ID for the menu item
    name: str  # Name of the dish
    category: str  # Category of the dish (e.g., starter, main_course, dessert)
    price: float  # Price of the dish
    is_available: bool  # Availability status of the dish


class OrderItem(BaseModel):
    menu_item_id: int  # Menu item ID that is part of the order
    quantity: int  # Quantity of the menu item ordered


class Order(BaseModel):
    id: int  # Unique order ID
    order_type: str  # Type of order: dine_in or takeaway
    table_number: Optional[int] = None  # Table number for dine-in orders (not needed for takeaway)
    items: List[OrderItem]  # List of ordered items
    status: str = "pending"  # Initial status of the order
    special_instructions: Optional[str] = None  # Optional special instructions for the order


# Level 1 – Menu CRUD operations

@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: Optional[bool] = False):
    # If the 'only_available' query parameter is true, return only available items
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu  # Return all menu items


@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    # Retrieve a menu item by its ID
    item = next((item for item in menu if item["id"] == id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@app.post("/menu", response_model=MenuItem)
def add_menu_item(item: MenuItem):
    # Add a new menu item to the menu
    global next_menu_id
    item_dict = item.dict()
    item_dict["id"] = next_menu_id  # Assign unique ID
    menu.append(item_dict)  # Add the item to the menu
    next_menu_id += 1  # Increment the menu ID for the next item
    return item_dict


@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    # Update an existing menu item by its ID
    for i, existing_item in enumerate(menu):
        if existing_item["id"] == id:
            menu[i] = item.dict()  # Replace the existing item with the updated item
            menu[i]["id"] = id  # Keep the same ID
            return menu[i]
    raise HTTPException(status_code=404, detail="Menu item not found")


@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    # Delete a menu item by its ID
    item_to_delete = next((item for item in menu if item["id"] == id), None)
    
    if item_to_delete is None:
        # If the item is not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    # Remove the item from the menu list
    menu.remove(item_to_delete)
    return {"detail": "Menu item deleted"}


# Level 2 – Orders (Create + Read)

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    # Create a new order
    global next_order_id

    # Validate order type and table number based on order type
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order type")
    if order.order_type == "dine_in" and order.table_number is None:
        raise HTTPException(status_code=400, detail="Table number is required for dine-in")
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number should be null for takeaway")
    
    # Validate menu item existence and availability
    for order_item in order.items:
        menu_item = next((item for item in menu if item["id"] == order_item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item with id {order_item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

        if order_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be greater than zero")

    # Create the order and add it to the order list
    order_dict = order.dict()
    order_dict["id"] = next_order_id
    order_dict["status"] = "pending"  # Set initial order status to 'pending'
    orders.append(order_dict)
    next_order_id += 1  # Increment the order ID for the next order
    return order_dict


@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[str] = None):
    # Return a list of orders, optionally filtered by status
    if status:
        return [order for order in orders if order["status"] == status]
    return orders  # Return all orders


@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    # Retrieve a specific order by its ID
    order = next((order for order in orders if order["id"] == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# Level 3 – Order status and total

@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status: str):
    # Validate and update the status of an order
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],  # From pending, it can go to in_progress or cancelled
        "in_progress": ["completed", "cancelled"]  # From in_progress, it can go to completed or cancelled
    }

    order = next((order for order in orders if order["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    current_status = order["status"]
    if status not in allowed_transitions.get(current_status, []):
        raise HTTPException(status_code=400, detail="Invalid status transition")
    
    order["status"] = status  # Update the order status
    return order


@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    # Calculate the total amount for an order
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Compute total price for all ordered items
    total = 0.0
    for item in order["items"]:
        # Retrieve menu item and compute the total for that item
        menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item['menu_item_id']} not found")
        total += menu_item["price"] * item["quantity"]

    # Return the total amount for the order
    return {"order_id": id, "total_amount": total}
