from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="SpiceHub")

# -----------------------------
# Data Models
# -----------------------------

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
    order_type: str   # "dine_in" or "takeaway"
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: Optional[str] = None

# -----------------------------
# In-memory storage
# -----------------------------
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders: List[Order] = []
next_menu_id = 5
next_order_id = 1

# -----------------------------
# Menu Endpoints
# -----------------------------

@app.get("/menu")
def get_menu(only_available: Optional[bool] = False):
    """
    Get all menu items.
    - Optional filter: only_available=True returns only available items.
    """
    if only_available:
        return [m for m in menu if m["is_available"]]
    return menu


@app.get("/menu/{id}")
def get_menu_by_id(id: int):
    """
    Get a menu item by ID.
    """
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")


@app.post("/menu", status_code=201)
def add_menu(item: MenuItem):
    """
    Add a new menu item.
    """
    global next_menu_id
    new_item = {
        "id": next_menu_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available
    }
    menu.append(new_item)
    next_menu_id += 1
    return new_item


@app.put("/menu/{id}")
def update_menu(id: int, item: MenuItem):
    """
    Update an existing menu item by ID.
    """
    for m in menu:
        if m["id"] == id:
            m.update({
                "name": item.name,
                "category": item.category,
                "price": item.price,
                "is_available": item.is_available
            })
            return m
    raise HTTPException(status_code=404, detail="Menu item not found")


@app.delete("/menu/{id}")
def delete_menu(id: int):
    """
    Delete a menu item by ID.
    """
    for m in menu:
        if m["id"] == id:
            menu.remove(m)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# -----------------------------
# Order Endpoints
# -----------------------------

@app.post("/orders", status_code=201)
def create_order(order: Order):
    """
    Create a new order.
    - Validates order_type ("dine_in" or "takeaway").
    - Validates table_number rules.
    - Validates items and availability.
    """
    global next_order_id

    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order_type")

    if order.order_type == "dine_in":
        if not order.table_number or order.table_number <= 0:
            raise HTTPException(status_code=400, detail="For dine_in, table_number must be positive")
    elif order.order_type == "takeaway":
        if order.table_number not in [None, 0]:
            raise HTTPException(status_code=400, detail="For takeaway, table_number must be null or 0")

    # Validate items
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be > 0")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    new_order = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_number=order.table_number,
        items=order.items,
        special_instructions=order.special_instructions,
        status="pending"
    )
    orders.append(new_order)
    next_order_id += 1
    return new_order


@app.get("/orders")
def get_orders(status: Optional[str] = None):
    """
    Get all orders.
    - Optional filter by status.
    """
    if status:
        return [o for o in orders if o.status == status]
    return orders


@app.get("/orders/{id}")
def get_order_by_id(id: int):
    """
    Get order details by ID.
    """
    for o in orders:
        if o.id == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")


@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: str):
    """
    Update order status.
    - Valid transitions:
      pending -> in_progress/cancelled/completed
      in_progress -> completed/cancelled
    - Completed/cancelled orders cannot be changed further.
    """
    for o in orders:
        if o.id == id:
            if o.status in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="No further changes allowed")
            if o.status == "pending" and status in ["in_progress", "cancelled", "completed"]:
                o.status = status
                return o
            if o.status == "in_progress" and status in ["completed", "cancelled"]:
                o.status = status
                return o
            raise HTTPException(status_code=400, detail="Invalid status transition")
    raise HTTPException(status_code=404, detail="Order not found")


@app.get("/orders/{id}/total-amount")
def get_order_total(id: int):
    """
    Calculate total amount for an order.
    """
    for o in orders:
        if o.id == id:
            total = 0
            for item in o.items:
                menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
                if menu_item:
                    total += menu_item["price"] * item.quantity
            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")

# -----------------------------
# SAMPLE INPUT/OUTPUT SUMMARY
# -----------------------------
# 1. Create Order (POST /orders)
# Request:
# {
#   "id": 0,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "special_instructions": "Less spicy"
# }
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy"
# }

# 2. Get All Orders (GET /orders)
# Response:
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#       {"menu_item_id": 2, "quantity": 1},
#       {"menu_item_id": 3, "quantity": 2}
#     ],
#     "status": "pending",
#     "special_instructions": "Less spicy"
#   }
# ]

# 3. Get Orders by Status (GET /orders?status=pending)
# Response:
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#       {"menu_item_id": 2, "quantity": 1},
#       {"menu_item_id": 3, "quantity": 2}
#     ],
#     "status": "pending",
#     "special_instructions": "Less spicy"
#   }
# ]

# 4. Get Order by ID (GET /orders/1)
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy"
# }

# 5. Update Order Status (PATCH /orders/1/status?status=in_progress)
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "status": "in_progress",
#   "special_instructions": "Less spicy"
# }

# 6. Complete Order (PATCH /orders/1/status?status=completed)
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "status": "completed",
#   "special_instructions": "Less spicy"
# }

# 7. Cancel Order (PATCH /orders/1/status?status=cancelled)
# Response:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     {"menu_item_id": 2, "quantity": 1},
#     {"menu_item_id": 3, "quantity": 2}
#   ],
#   "status": "cancelled",
#   "special_instructions": "Less spicy"
# }

# 8. Get Order Total Amount (GET /orders/1/total-amount)
# Response:
# {
#   "order_id": 1,
#   "total_amount": 347.0
# }