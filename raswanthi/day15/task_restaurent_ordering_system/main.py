from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
#importing essential modules from Fastapi, pydantic and typing
app = FastAPI(title="SpiceHub")

# Models
class MenuItem(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool

class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

class Order(BaseModel):
    order_type: str
    table_number: Optional[int] = None
    items: List[OrderItem]
    special_instructions: Optional[str] = None

# In-memory storage
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []


@app.get("/menu")
def menu_items(available: bool = False):
    if available:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}")
def get_menu_item(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", status_code=201)
def add_menu(item: MenuItem):
    new_id = len(menu) + 1
    new_item = {
        "id": new_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available,
    }
    menu.append(new_item)
    return new_item

@app.put("/menu/{id}")
def update_item(id: int, item: MenuItem):
    for menu_item in menu:
        if menu_item["id"] == id:
            menu_item["name"] = item.name
            menu_item["category"] = item.category
            menu_item["price"] = item.price
            menu_item["is_available"] = item.is_available
            return menu_item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_item(id: int):
    for menu_item in menu:
        if menu_item["id"] == id:
            menu.remove(menu_item)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/orders", status_code=201)
def create_order(order: Order):
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order_type")

    if order.order_type == "dine_in" and (order.table_number is None or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="Table number must be positive for dine_in")

    if order.order_type == "takeaway" and order.table_number not in [None, 0]:
        raise HTTPException(status_code=400, detail="Table number must be null or 0 for takeaway")

    for li in order.items:
        if li.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive")
        menu_item = None
        for m in menu:
            if m["id"] == li.menu_item_id:
                menu_item = m
                break
        if not menu_item or not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {li.menu_item_id} not available")

    new_id = len(orders) + 1
    new_order = {
        "id": new_id,
        "order_type": order.order_type,
        "table_number": order.table_number,
        "items": [{"menu_item_id": li.menu_item_id, "quantity": li.quantity} for li in order.items],
        "special_instructions": order.special_instructions,
        "status": "pending",
    }
    orders.append(new_order)
    return new_order

@app.get("/orders")
def list_orders(status: Optional[str] = None):
    if status:
        return [ord for ord in orders if ord["status"] == status]
    return orders

@app.get("/orders/{id}")
def get_order(id: int):
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")


@app.patch("/orders/{id}/status")
def update_order_status(id: int, body: dict = Body(...)):
    new_status = body.get("status")
    allowed_statuses = ["pending", "in_progress", "completed", "cancelled"]

    if new_status not in allowed_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")

    for order in orders:
        if order["id"] == id:
            current_status = order["status"]

            if current_status == "pending" and new_status in ["in_progress", "cancelled"]:
                order["status"] = new_status
                return order
            elif current_status == "in_progress" and new_status in ["completed", "cancelled"]:
                order["status"] = new_status
                return order
            elif current_status in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="No further changes allowed")
            else:
                raise HTTPException(status_code=400, detail="Illegal transition")

    raise HTTPException(status_code=404, detail="Order not found")


@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    for order in orders:
        if order["id"] == id:
            total = 0.0
            for item in order["items"]:
                menu_item = None
                for m in menu:
                    if m["id"] == item["menu_item_id"]:
                        menu_item = m
                        break
                if not menu_item:
                    raise HTTPException(status_code=404, detail=f"Menu item {item['menu_item_id']} not found")
                total += menu_item["price"] * item["quantity"]

            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")
