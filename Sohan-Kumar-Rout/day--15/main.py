from typing import List , Optional
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException

# Menu item model
class MenuItem(BaseModel):
    id : int
    name : str
    category : str
    price : float
    is_available:bool
    
# Model for creating menu item
class MenuCreateItem(BaseModel):
    name : str
    category : str
    price : float
    is_available:bool
    
# Order item model
class OrderItem(BaseModel):
    menu_item_id: int
    quantity:int

# Order model
class Order(BaseModel):
    id : int
    order_type: str
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: str = "Pending"
    special_instruction : Optional[str] = None
    
# Model for creating order
class OrderCreate(BaseModel):
    order_type:str
    table_number : Optional[int] = None
    items: List[OrderItem]
    special_instruction : Optional[str] = None
    
# Model for updating order status
class OrderStatusUpdate(BaseModel):
    status: str
    
# Sample menu data
menu = [
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
 },
]

# Orders list and counters
order =[]
next_menu_id =5
next_order_id =1

app=FastAPI()

# Get menu items
@app.get("/menu")
def get_menu(only_available : bool = False):
    if only_available:
        available_item=[]
        for item in menu:
            if item["is_available"]:
                available_item.append(item)
        return available_item
    return menu

# Get menu item by id
@app.get("/menu/{id}")
def get_menu_by_id(id : int):
    for item in menu:
        if item["id"]==id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found ")

# Add new menu item
@app.post("/menu")
def add_menu_item(item : MenuCreateItem):
    global next_menu_id
    
    new_item ={
        "id": next_menu_id,
        "name": item.name,
        "category" : item.category,
        "price" : item.price,
        "is_available": item.is_available
    }
    menu.append(new_item)
    next_menu_id+=1
    
    return new_item

# Update menu item
@app.put("/menu/{id}")
def update_menu(id : int , item : MenuCreateItem):
    for m in menu:
        if m["id"] ==id:
            m.update({
                "name": item.name,
                "category": item.category,
                "price": item.price,
                "is_available": item.is_available
            })
            return m
    raise HTTPException(status_code=404, detail="Menu item not found")

# Delete menu item
@app.delete("/menu/{id}")
def delete_menu(id : int):
    for m in menu:
        if m["id"]==id:
            menu.remove(m)
            return {"detail" : "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# Create new order
@app.post("/orders", response_model=Order)
def create_order(order: OrderCreate):
    global next_order_id

    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="order_type must be 'dine_in' or 'takeaway'")
    
    if order.order_type == "dine_in":
        if not order.table_number or order.table_number <= 0:
            raise HTTPException(status_code=400, detail="For dine_in, table_number must be a positive integer")
        
    elif order.order_type == "takeaway":
        if order.table_number not in [None, 0]:
            raise HTTPException(status_code=400, detail="For takeaway, table_number must be null or 0")
        
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail=f"Quantity must be > 0 for menu_item_id {item.menu_item_id}")

        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} does not exist")

        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")
        
    new_order = {
        "id": next_order_id,
        "order_type": order.order_type,
        "table_number": order.table_number,
        "items": order.items,
        "status": "pending",
        "special_instructions": order.special_instructions
    }
    order.append(new_order)
    next_order_id += 1
    return new_order

# List orders
@app.get("/orders", response_model=List[Order])
def list_orders(status: Optional[str] = None):
    if status:
        return [o for o in order if o["status"] == status]
    return order

# Get order by id
@app.get("/orders/{id}", response_model=Order)
def get_order(id: int):
    for o in Order:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")

# Update order status
@app.patch("/orders/{id}/status", response_model=Order)
def update_order_status(id: int, update: OrderStatusUpdate):
    for o in order:
        if o["id"] == id:
            current_status = o["status"]
            new_status = update.status

            if current_status == "pending" and new_status == "in_progress":
                o["status"] = new_status
            elif current_status == "in_progress" and new_status in ["completed", "cancelled"]:
                o["status"] = new_status
            else:
                raise HTTPException(status_code=400, detail=f"Illegal status transition from {current_status} to {new_status}")

            return o

    raise HTTPException(status_code=404, detail="Order not found")

# Get total amount of order
@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    for o in order:
        if o["id"] == id:
            total = 0.0
            for item in o["items"]:
                menu_item = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
                if not menu_item:
                    raise HTTPException(status_code=400, detail=f"Menu item {item['menu_item_id']} not found")
                total += menu_item["price"] * item["quantity"]

            return {"order_id": id, "total_amount": total}

    raise HTTPException(status_code=404, detail="Order not found")

#Output

# GET /menu
# [
#   {
#     "id": 1,
#     "name": "Tomato Soup",
#     "category": "starter",
#     "price": 99.0,
#     "is_available": true
#   },
#   {
#     "id": 2,
#     "name": "Paneer Butter Masala",
#     "category": "main_course",
#     "price": 249.0,
#     "is_available": true
#   },
#   {
#     "id": 3,
#     "name": "Butter Naan",
#     "category": "main_course",
#     "price": 49.0,
#     "is_available": true
#   },
#   {
#     "id": 4,
#     "name": "Gulab Jamun",
#     "category": "dessert",
#     "price": 79.0,
#     "is_available": false
#   }
# ]

# GET /menu/2
# {
#   "id": 2,
#   "name": "Paneer Butter Masala",
#   "category": "main_course",
#   "price": 249.0,
#   "is_available": true
# }

# POST /menu
# {
#   "id": 5,
#   "name": "Veg Biryani",
#   "category": "main_course",
#   "price": 199.0,
#   "is_available": true
# }

# POST /orders
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 3,
#   "items": [
#     { "menu_item_id": 2, "quantity": 1 },
#     { "menu_item_id": 3, "quantity": 2 }
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy"
# }

# GET /orders
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 3,
#     "items": [
#       { "menu_item_id": 2, "quantity": 1 },
#       { "menu_item_id": 3, "quantity": 2 }
#     ],
#     "status": "pending",
#     "special_instructions": "Less spicy"
#   }
# ]

# PATCH /orders/1/status
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 3,
#   "items": [
#     { "menu_item_id": 2, "quantity": 1 },
#     { "menu_item_id": 3, "quantity": 2 }
#   ],
#   "status": "in_progress",
#   "special_instructions": "Less spicy"
# }

# GET /orders/1/total-amount
# {
#   "order_id": 1,
#   "total_amount": 347.0
# }

