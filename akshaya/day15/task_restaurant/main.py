# restaurant management - spicehub
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="SpiceHub Restaurant API")

# In-memory data storage
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders = [] 
next_menu_id = 5  
next_order_id = 1  


# Pydantic models
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
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: Optional[str] = None


# Level 1 – Menu CRUD operations
@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu


@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    item = next((item for item in menu if item["id"] == id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@app.post("/menu", response_model=MenuItem)
def add_menu_item(item: MenuItem):
    global next_menu_id
    item_dict = item.dict()
    item_dict["id"] = next_menu_id
    menu.append(item_dict)
    next_menu_id += 1
    return item_dict


@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    for i, existing_item in enumerate(menu):
        if existing_item["id"] == id:
            menu[i] = item.dict()
            menu[i]["id"] = id
            return menu[i]
    raise HTTPException(status_code=404, detail="Menu item not found")


@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    # Try to find the item with the given id
    item_to_delete = next((item for item in menu if item["id"] == id), None)
    
    if item_to_delete is None:
        # If not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    # Remove the item from the menu list
    menu.remove(item_to_delete)
    return {"detail": "Menu item deleted"}


# Level 2 – Orders (Create + Read)
@app.post("/orders", response_model=Order)
def create_order(order: Order):
    global next_order_id

    # Validation
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

    # Create the order
    order_dict = order.dict()
    order_dict["id"] = next_order_id
    order_dict["status"] = "pending"
    orders.append(order_dict)
    next_order_id += 1
    return order_dict


@app.get("/orders", response_model=List[Order])
def get_orders(status: Optional[str] = None):
    if status:
        return [order for order in orders if order["status"] == status]
    return orders


@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    order = next((order for order in orders if order["id"] == id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# Level 3 – Order status and total
@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status: str):
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"]
    }

    order = next((order for order in orders if order["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    current_status = order["status"]
    if status not in allowed_transitions.get(current_status, []):
        raise HTTPException(status_code=400, detail="Invalid status transition")
    
    order["status"] = status
    return order

@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    # Find order by id
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Compute bill
    total = 0.0
    for item in order["items"]:
        # item is a dict, so use dict keys
        menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item['menu_item_id']} not found")
        total += menu_item["price"] * item["quantity"]

    # Return JSON
    return {"order_id": id, "total_amount": total}

