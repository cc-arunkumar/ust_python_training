from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="SpiceHub")


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

menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders: List[Order] = []
next_menu_id = 5
next_order_id = 1

@app.get("/menu")
def get_menu(only_available: Optional[bool] = False):
    if only_available:
        result=[]
        for m in menu:
            if m["is_available"]:
                result.append(m)
        return result
    return menu

@app.get("/menu/{id}")
def get_menu_by_id(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", status_code=201)
def add_menu(item: MenuItem):
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
    for m in menu:
        if m["id"] == id:
            menu.remove(m)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/orders", status_code=201)
def create_order(order: Order):
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
    if status:
        return [o for o in orders if o.status == status]
    return orders

@app.get("/orders/{id}")
def get_order_by_id(id: int):
    for o in orders:
        if o.id == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: str):
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
    for o in orders:
        if o.id == id:
            total = 0
            for item in o.items:
                menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
                if menu_item:
                    total += menu_item["price"] * item.quantity
            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")
