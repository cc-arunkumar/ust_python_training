from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI()

# ------------------ Data Models ------------------

class MenuItem(BaseModel):
    id: int = 0
    name: str
    category: str
    price: float
    is_available: bool   

class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):   
    id: int = 0
    order_type: str                 # "dine_in" or "takeaway"
    table_number: Optional[int] = None
    items: List[OrderItem]          # List of ordered items
    status: str                     # "pending", "in_progress", etc.
    special_instructions: Optional[str] = None

# ------------------ In-memory Data ------------------

menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders: List[Order] = []
next_menu_id = 5
next_order_id = 0

# ------------------ Menu Endpoints ------------------

@app.get("")
def justtest():
    return "hello from the server side"

@app.get("/menu")
def get_menu_items(is_available: Optional[bool] = None):
    if is_available is not None:
        return [row for row in menu if row["is_available"] == is_available]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    for row in menu:
        if row["id"] == id:
            return row
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu")
def post_menu_item(menu_item: MenuItem):
    menu_item.id = next_menu_id
    next_menu_id += 1
    menu.append(menu_item.model_dump())
    return Response(content='{"detail":"Data has been pushed"}', media_type="application/json", status_code=200)

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, updated_item: MenuItem):
    for index, row in enumerate(menu):
        if row["id"] == id:
            updated_item.id = id 
            menu[index] = updated_item.model_dump()
            return updated_item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for index, row in enumerate(menu):
        if row["id"] == id:
            del menu[index]
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# ------------------ Order Endpoints ------------------

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    # Validate order type
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="order_type must be 'dine_in' or 'takeaway'")

    # Validate table number rules
    if order.order_type == "dine_in":
        if not order.table_number or order.table_number <= 0:
            raise HTTPException(status_code=400, detail="table_number must be positive for dine_in")
    elif order.order_type == "takeaway":
        if order.table_number not in [None, 0]:
            raise HTTPException(status_code=400, detail="table_number must be null or 0 for takeaway")

    # Validate items
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Item quantity must be greater than 0")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} does not exist")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    # Assign ID and status
    order.id = next_order_id
    order.status = "pending"
    next_order_id += 1

    orders.append(order)
    return order

@app.get("/orders")
def get_orders(status: str):
    if status:
        return [row for row in orders]
    return orders

@app.get("/orders/{id}")
def get_orders_by_id(id: int):
    for row in orders:
        if row.id == id:
            return row
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, status_update: dict):
    order = next((o for o in orders if o.id == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    new_status = status_update.get("status")
    if new_status not in ["pending", "in_progress", "completed", "cancelled"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }

    if new_status not in allowed_transitions[order.status]:
        raise HTTPException(status_code=400, detail=f"Illegal transition from {order.status} to {new_status}")

    order.status = new_status
    return order

@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    order = next((o for o in orders if o.id == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    total = 0.0
    for item in order.items:
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} not found")
        total += menu_item["price"] * item.quantity

    return {"order_id": order.id, "total_amount": total}

# ===================sample output========================
# {
#   "menu": [
#     {
#       "id": 1,
#       "name": "Tomato Soup",
#       "category": "starter",
#       "price": 99.0,
#       "is_available": true
#     },
#     {
#       "id": 2,
#       "name": "Paneer Butter Masala",
#       "category": "main_course",
#       "price": 249.0,
#       "is_available": true
#     },
#     {
#       "id": 3,
#       "name": "Butter Naan",
#       "category": "main_course",
#       "price": 49.0,
#       "is_available": true
#     },
#     {
#       "id": 4,
#       "name": "Gulab Jamun",
#       "category": "dessert",
#       "price": 79.0,
#       "is_available": false
#     }
#   ],
#   "new_order": {
#     "id": 0,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       { "menu_item_id": 2, "quantity": 2 },
#       { "menu_item_id": 3, "quantity": 4 }
#     ],
#     "status": "pending",
#     "special_instructions": "Less spicy please"
#   },
#   "order_status_update": {
#     "id": 0,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       { "menu_item_id": 2, "quantity": 2 },
#       { "menu_item_id": 3, "quantity": 4 }
#     ],
#     "status": "in_progress",
#     "special_instructions": "Less spicy please"
#   },
#   "order_total": {
#     "order_id": 0,
#     "total_amount": 794.0
#   },
#   "delete_menu_item": {
#     "detail": "Menu item deleted"
#   }
# }
