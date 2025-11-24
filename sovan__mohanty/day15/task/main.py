#Task Restaurant Ordering System
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="SpiceHub")

# In-memory data
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders = []  
next_menu_id = 5
next_order_id = 1

# --- Models ---
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
    status: str
    special_instructions: Optional[str] = None

class UpdateStatus(BaseModel):
    status: str

# --- Endpoints ---

@app.get("/menu", response_model=List[MenuItem])
def get_all_menu(only_available: bool = Query(False)):
    # Return all menu items; filter only available if query param is true
    if only_available:
        return [MenuItem(**item) for item in menu if item["is_available"]]
    return [MenuItem(**item) for item in menu]

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_by_id(id: int):
    # Return a single menu item by ID, 404 if not found
    item = next((m for m in menu if m["id"] == id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu not found")
    return MenuItem(**item)

@app.post("/menu", response_model=MenuItem, status_code=201)
def create_menu_item(new_item: MenuItem):
    # Create a new menu item with auto-incremented ID
    global next_menu_id
    new_item.id = next_menu_id
    menu.append(new_item.dict())
    next_menu_id += 1
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, updated_item: MenuItem):
    # Update an existing menu item by ID
    item = next((m for m in menu if m["id"] == id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu not found")
    item.update(updated_item.dict())
    return MenuItem(**item)

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    # Delete a menu item by ID
    item = next((m for m in menu if m["id"] == id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Menu not found")
    menu.remove(item)
    return {"detail": "Menu item deleted"}

@app.post("/orders", response_model=Order, status_code=201)
def create_order(order: Order):
    # Create a new order; validate order_type, table_number, items, and availability
    global next_order_id

    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="order_type must be 'dine_in' or 'takeaway'")

    if order.order_type == "dine_in":
        if not order.table_number or order.table_number <= 0:
            raise HTTPException(status_code=400, detail="For dine_in, table_number must be positive")
    elif order.order_type == "takeaway":
        if order.table_number not in [None, 0]:
            raise HTTPException(status_code=400, detail="For takeaway, table_number must be null or 0")

    if not order.items or len(order.items) == 0:
        raise HTTPException(status_code=400, detail="Order must contain at least one item")

    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Item quantity must be greater than 0")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} does not exist")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    new_order = {
        "id": next_order_id,
        "order_type": order.order_type,
        "table_number": order.table_number,
        "items": [item.dict() for item in order.items],
        "status": "pending",
        "special_instructions": order.special_instructions
    }
    orders.append(new_order)
    next_order_id += 1
    return Order(**new_order)

@app.get("/orders", response_model=List[Order])
def list_orders(status: Optional[str] = Query(None)):
    # List all orders; filter by status if provided
    if status:
        return [Order(**o) for o in orders if o["status"] == status]
    return [Order(**o) for o in orders]

@app.get("/orders/{id}", response_model=Order)
def get_order_by_id(id: int):
    # Return a single order by ID, 404 if not found
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return Order(**order)

@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, req: UpdateStatus):
    # Update order status with allowed transitions
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    current_status = order["status"]
    new_status = req.status

    if new_status not in ["pending", "in_progress", "completed", "cancelled"]:
        raise HTTPException(status_code=400, detail="Invalid status value")

    allowed = False
    if current_status == "pending" and new_status in ["in_progress", "cancelled"]:
        allowed = True
    elif current_status == "in_progress" and new_status in ["completed", "cancelled"]:
        allowed = True
    if current_status in ["completed", "cancelled"]:
        raise HTTPException(status_code=400, detail="No further status changes allowed")

    if not allowed:
        raise HTTPException(status_code=400, detail=f"Illegal transition from {current_status} to {new_status}")

    order["status"] = new_status
    return Order(**order)

@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    # Calculate total amount for an order by summing price × quantity
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    total = 0.0
    for item in order["items"]:
        menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item['menu_item_id']} not found")
        total += menu_item["price"] * item["quantity"]

    return {"order_id": id, "total_amount": total}


#Sample Execution

# GET /menu
# [
#   {"id":1,"name":"Tomato Soup","category":"starter","price":99.0,"is_available":true},
#   {"id":2,"name":"Paneer Butter Masala","category":"main_course","price":249.0,"is_available":true},
#   {"id":3,"name":"Butter Naan","category":"main_course","price":49.0,"is_available":true},
#   {"id":4,"name":"Gulab Jamun","category":"dessert","price":79.0,"is_available":false}
# ]

# GET /menu/2
# {"id":2,"name":"Paneer Butter Masala","category":"main_course","price":249.0,"is_available":true}

# POST /menu
# {"id":5,"name":"Veg Biryani","category":"main_course","price":199.0,"is_available":true}

# PUT /menu/3
# {"id":3,"name":"Butter Naan","category":"main_course","price":59.0,"is_available":true}

# DELETE /menu/4
# {"detail":"Menu item deleted"}

# POST /orders
# {
#   "id":1,
#   "order_type":"dine_in",
#   "table_number":12,
#   "items":[{"menu_item_id":2,"quantity":2},{"menu_item_id":3,"quantity":4}],
#   "status":"pending",
#   "special_instructions":"Less spicy"
# }

# GET /orders
# [
#   {
#     "id":1,
#     "order_type":"dine_in",
#     "table_number":12,
#     "items":[{"menu_item_id":2,"quantity":2},{"menu_item_id":3,"quantity":4}],
#     "status":"pending",
#     "special_instructions":"Less spicy"
#   }
# ]

#  GET /orders/1
# {
#   "id":1,
#   "order_type":"dine_in",
#   "table_number":12,
#   "items":[{"menu_item_id":2,"quantity":2},{"menu_item_id":3,"quantity":4}],
#   "status":"pending",
#   "special_instructions":"Less spicy"
# }


# PATCH /orders/1/status
# {
#   "id":1,
#   "order_type":"dine_in",
#   "table_number":12,
#   "items":[{"menu_item_id":2,"quantity":2},{"menu_item_id":3,"quantity":4}],
#   "status":"in_progress",
#   "special_instructions":"Less spicy"
# }

# GET /orders/1/total-amount
# {"order_id":1,"total_amount":794.0}