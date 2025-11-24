from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, time

# Initialize FastAPI application
app = FastAPI(title="SpiceHub")

# Pydantic model for Menu item (defining the structure of each menu item)
class Menuitem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool
    
# Pydantic model for OrderItem (menu item in the order along with quantity)
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Pydantic model for Order (structure of an order including multiple order items)
class Order(BaseModel):
    id: int
    order_type: str  # Either "dine_in" or "takeaway"
    table_number: int | None = None  # Optional table number (only needed for dine-in)
    items: List[OrderItem]  # List of items in the order
    status: str = "Pending"  # Default status for orders
    special_instructions: str | None = None  # Optional special instructions for the order
    
# Pydantic model for updating the order status
class OrderStatusUpdate(BaseModel):
    status: str

# Sample menu data to be used in the app
menu: List[Menuitem] = [
    {
        "id": 1,
        "name": "Tomato Soup",
        "category": "starter",
        "price": 99.0,
        "is_available": True
    },
    {
        "id": 2,
        "name": "Paneer Butter Masala",
        "category": "main_course",
        "price": 249.0,
        "is_available": True
    },
    {
        "id": 3,
        "name": "Butter Naan",
        "category": "main_course",
        "price": 49.0,
        "is_available": True
    },
    {
        "id": 4,
        "name": "Gulab Jamun",
        "category": "dessert",
        "price": 79.0,
        "is_available": False
    }
]

# Orders list to store all placed orders
orders = []  
next_menu_id = 5  # Next available menu item ID
next_order_id = 1  # Next available order ID

# Get all menu items, with an optional filter for availability
@app.get("/Menu", response_model=List[Menuitem])
def get_menu(is_available: bool | None = None):
    if is_available:
        return [odr for odr in menu if odr['is_available'] == True]  # Filter available items
    return menu  # Return all menu items

# Get a specific menu item by its ID
@app.get("/Menu/{id}")
def get_menu(id: int):
    try:
        for odr in menu:
            if odr["id"] == id:
                return odr  # Return the menu item if found
    except IndexError:
        raise HTTPException(status_code=404, detail="Menu item not found")

# Add a new menu item
@app.post("/Menu")
def add_menu(odr: Menuitem):
    global next_menu_id
    odr.id = next_menu_id  # Assign a new ID to the menu item
    next_menu_id += 1  # Increment the menu ID for the next item
    menu.append(odr.model_dump())  # Convert the Pydantic model to a dictionary and append it to the menu

# Update an existing menu item by ID
@app.put("/Menu/{id}")
def update(id: int, odr: Menuitem):
    for e in menu:
        if e["id"] == id:
            e.update({
                "id": e.id,
                "name": e.name,
                "category": e.category,
                "price": e.price,
                "is_available": e.is_available
            })
            return e  # Return the updated item
    raise HTTPException(status_code=404, detail="Item does not exist")  # Item not found

# Delete a menu item by ID
@app.delete("/Menu/{id}")
def delete_item(id: int):
    for e in menu:
        if e['id'] == id:
            menu.remove(e)  # Remove the item from the menu list
            return {"detail": "Item deleted"}  # Confirmation of deletion
    raise HTTPException(status_code=404, detail="Item not found")  # Item not found

# Create a new order
@app.post("/orders", status_code=201)
def create_order(order: Order):
    global next_order_id

    # Validate the menu items in the order
    for order_item in order.items:
        menu_item = next((item for item in menu if item["id"] == order_item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item with id {order_item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    # Validate order type details
    if order.order_type == "dine_in" and (order.table_number is None or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number is required for dine-in orders")
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number should be null for takeaway orders")

    order.id = next_order_id  # Assign a new order ID
    next_order_id += 1  # Increment the order ID for the next order
    orders.append(order.model_dump())  # Add the order to the orders list
    return order  # Return the created order

# Get a list of all orders
@app.get("/Order")
def get_order():
    return orders  # Return all orders

# Get a specific order by its ID
@app.get("/Orders/{id}")
def get_order(id: int):
    for odr in orders:
        if odr["id"] == id:
            return odr  # Return the order if found
    raise HTTPException(status_code=404, detail="Order not found")  # Order not found

# Update the status of an existing order
@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, update: OrderStatusUpdate):
    for o in orders:
        if o["id"] == id:
            current_status = o["status"]
            new_status = update.status

            # Handle valid status transitions
            if current_status == "Pending" and new_status == "in_progress":
                o["status"] = new_status
            elif current_status == "in_progress" and new_status in ["completed", "cancelled"]:
                o["status"] = new_status
            else:
                raise HTTPException(status_code=400, detail=f"Illegal status transition from {current_status} to {new_status}")

            return o  # Return the updated order

    raise HTTPException(status_code=404, detail="Order not found")  # Order not found

# Calculate the total amount of an order
@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    for o in orders:
        if o["id"] == id:
            total = 0.0
            for item in o["items"]:
                menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
                if not menu_item:
                    raise HTTPException(status_code=400, detail=f"Menu item {item['menu_item_id']} not found")
                total += menu_item["price"] * item["quantity"]

            return {"order_id": id, "total_amount": total}  # Return the total amount for the order

    raise HTTPException(status_code=404, detail="Order not found")  # Order not found






