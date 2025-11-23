from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Spice Hub")

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
    
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []
next_menu_id = 5
next_order_id = 1

@app.get("/menu")
def get_menu(only_available : bool = False):
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}")
def get_menu_by_id(id : int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found.")

@app.post("/menu", status_code=201)
def add_menu(item : MenuItem):
    global next_menu_id
    new_item = item.model_dump()
    new_item["id"] = next_menu_id
    menu.append(new_item)
    next_menu_id += 1
    return new_item

@app.put("/menu/{id}")
def update_menu(id : int, item : MenuItem):
    for i, m in enumerate(menu):
        if m["id"] == id:
            updated_item = item.model_dump()
            updated_item["id"] = id
            menu[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item Not Found!")

@app.delete("/menu/{id}")
def delete_menu(id : int):
    for i, m in enumerate(menu):
        if m["id"] == id:
            menu.pop(i)
            return {"detail" : "Menu Item Detail."}
    raise HTTPException(status_code=404, detail="Item not found.")


@app.post("/orders", status_code=201)
def create_order(order : Order):
    global next_order_id
    if order.order_type not in ["dine_in" or "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order type")
    
    if order.order_type == "dine_in" and (not order.table_number or order.table_number <= 0):
        raise HTTPException(status_code=400, detail="table number required.")
    
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Item cannot be empty.")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail="Item not found.")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail="Item is not available.")
    
    new_order = order.model_dump()
    new_order["id"] = next_order_id
    new_order["status"] = "pending"
    orders.append(new_order)
    next_order_id += 1
    return new_order

@app.get("/orders")
def get_order(status : Optional[str] = None):
    if status:
        return [o for o in orders if o["status"] == status]
    return orders

@app.get("/orders/{id}/")
def get_order_by_id(id : int):
    for ord in orders:
        if ord["id"] == id:
            return ord
    raise HTTPException(status_code=404, detail="Order with that id not found.")


@app.patch("/orders/{id}/status")
def update_status(id: int, status: str):
    for o in orders:
        if o["id"] == id:
            current_status = o["status"]
            
            allowed_changes = {
                "pending" : ["in_progress", "cancelled"],
                "in_progress" : ["completed", "cancelled"]
            }
            
            if current_status == "completed" or current_status == "cancelled":
                raise HTTPException(status_code=400, detail="Cannot be modified more.")
            
            if status not in allowed_changes.get(current_status, []):
                raise HTTPException(status_code=400, detail="Invalid status transition.")
            
            o["status"] = status
            return o
        
    raise HTTPException(status_code=404, detail="Order not found.")
    
@app.get("/orders/{id}/total_amount")
def compute_bill(id: int):
    order = next((o for o in orders if o["id"] == id), None)
    if not order:
        raise HTTPException(status_code=404, detail="order not found.")
    
    total_amount = 0.0
    for item in order["items"]:
        menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
        if menu_item:
            total_amount += menu_item["price"] * menu_item["quantity"]
    
    return {"orderId" :id, "total_amount" : total_amount}

                  