from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI(title="Spice Hub")

# Pydantic Models
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool

class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str = "pending"
    special_instruction: str = "Nothing"

# In-memory data
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders: List[Order] = []
next_menu_id = 4
next_order_id = 0

# LEVEL 1 – Menu CRUD
@app.get("/menu", response_model=List[MenuItem])
def display_all(flag: bool = False):
    """Display all menu items, filtered by availability if flag is True."""
    if flag:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def search_byid(id: int):
    """Search for a menu item by its ID."""
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem)
def create_new_item(new_item: MenuItem):
    """Create a new menu item."""
    global next_menu_id
    next_menu_id += 1
    new_item.id = next_menu_id
    menu.append(new_item.dict())
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def updating_byid(id: int, new_item: MenuItem):
    """Update an existing menu item."""
    for item in menu:
        if item["id"] == id:
            # Update only fields that are set
            item.update(new_item.dict(exclude_unset=True))
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/menu/{id}")
def deleting_byid(id: int):
    """Delete a menu item by its ID."""
    for item in menu:
        if item["id"] == id:
            menu.remove(item)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# LEVEL 2 – Orders
@app.post("/orders", response_model=Order)
def creating_order(new_order: Order):
    """Create a new order."""
    global next_order_id
    next_order_id += 1

    if new_order.order_type == "dine_in" and (new_order.table_number is None or new_order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number must be provided for dine-in orders.")
    
    # Validate order items
    for order_item in new_order.items:
        if order_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive.")
        if not any(m["id"] == order_item.menu_item_id for m in menu):
            raise HTTPException(status_code=400, detail="Menu item not found in menu.")

    new_order.id = next_order_id
    orders.append(new_order)
    return new_order

@app.get("/orders", response_model=List[Order])
def display_orders(stat: str = None):
    """Display orders, optionally filtered by status."""
    if stat:
        return [order for order in orders if order.status == stat]
    return orders

@app.get("/orders/{id}", response_model=Order)
def display_specific_order(id: int):
    """Get a specific order by its ID."""
    for order in orders:
        if order.id == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# LEVEL 3 – Order Status + Total Amount
@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, change: str):
    """Update the status of an order."""
    for order in orders:
        if order.id == id:
            if order.status == "completed" or order.status == "cancelled":
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
    """Compute the total bill for an order."""
    for order in orders:
        if order.id == id:
            total_amount = sum(
                item.quantity * next(m["price"] for m in menu if m["id"] == item.menu_item_id)
                for item in order.items
            )
            return {"order_id": id, "total_amount": total_amount}

    raise HTTPException(status_code=404, detail="Order not found")
