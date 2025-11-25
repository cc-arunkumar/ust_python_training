from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app with a title
app = FastAPI(title="SPICEHUB")

# ------------------ MODELS ------------------

# Menu item schema
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool = True

# Order item schema (links to menu item)
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Order schema
class Order(BaseModel):
    id: int
    order_type: str  # "dine_in" or "takeaway"
    table_number: Optional[int] = None
    items: List[OrderItem]
    status: str = "pending"
    special_instruction: Optional[str] = None

# ------------------ DATA ------------------

# Initial menu data
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []          # Store orders
next_menu_id = 5     # Auto-increment menu IDs
next_order_id = 1    # Auto-increment order IDs

# ------------------ MENU ENDPOINTS ------------------

@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: bool = False):
    # Return all menu items or only available ones
    if only_available:
        return [item for item in menu if item["is_available"]]
    return menu

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    # Find menu item by ID
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem)
def add_new_menu(item: MenuItem):
    # Add new menu item with auto ID
    global next_menu_id
    new_item = {
        "id": next_menu_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available,
    }
    menu.append(new_item)
    next_menu_id += 1
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, item: MenuItem):
    # Update existing menu item
    for m in menu:
        if m["id"] == id:
            m["name"] = item.name
            m["category"] = item.category
            m["price"] = item.price
            m["is_available"] = item.is_available
            return m
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    # Delete menu item by ID
    for index, m in enumerate(menu):
        if m["id"] == id:
            del menu[index]
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")

# ------------------ ORDER ENDPOINTS ------------------

@app.post("/orders", response_model=Order)
def create_order(order: Order):
    global next_order_id
    # Validate order type
    if order.order_type not in ["dine_in", "takeaway"]:
        raise HTTPException(status_code=400, detail="Invalid order_type")
    # Dine-in requires table number
    if order.order_type == "dine_in":
        if not order.table_number or order.table_number <= 0:
            raise HTTPException(status_code=400, detail="Table number required for dine_in")
    # Takeaway must not have table number
    if order.order_type == "takeaway" and order.table_number is not None:
        raise HTTPException(status_code=400, detail="Table number must be null for takeaway")

    # Validate items
    for item in order.items:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be > 0")
        menu_item = next((m for m in menu if m["id"] == item.menu_item_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Menu item {item.menu_item_id} not found")
        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item {menu_item['name']} is not available")

    # Save order
    order.id = next_order_id
    order.status = "pending"
    orders.append(order.dict())
    next_order_id += 1
    return order

@app.get("/orders")
def list_orders(status: Optional[str] = None):
    # List all orders or filter by status
    if status:
        return [o for o in orders if o["status"] == status]
    return orders

@app.get("/orders/{id}")
def get_order(id: int):
    # Get order by ID
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")

@app.patch("/orders/{id}/status")
def update_order_status(id: int, status: str):
    # Update order status with rules
    for o in orders:
        if o["id"] == id:
            if o["status"] in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="No further changes allowed")
            if o["status"] == "pending" and status not in ["in_progress", "cancelled"]:
                raise HTTPException(status_code=400, detail="Invalid transition")
            if o["status"] == "in_progress" and status not in ["completed", "cancelled"]:
                raise HTTPException(status_code=400, detail="Invalid transition")
            o["status"] = status
            return o
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/orders/{id}/total-amount")
def get_total_amount(id: int):
    # Calculate total bill for an order
    for o in orders:
        if o["id"] == id:
            total = 0
            for item in o["items"]:
                found = next((m for m in menu if m["id"] == item["menu_item_id"]), None)
                if found:
                    total += found["price"] * item["quantity"]
            return {"order_id": id, "total_amount": total}
    raise HTTPException(status_code=404, detail="Order not found")

# Output
# {
#   "menu_all": [
#     {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true},
#     {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true},
#     {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true},
#     {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false}
#   ],

#   "menu_single": {
#     "id": 2,
#     "name": "Paneer Butter Masala",
#     "category": "main_course",
#     "price": 249.0,
#     "is_available": true
#   },

#   "menu_added": {
#     "id": 5,
#     "name": "Veg Biryani",
#     "category": "main_course",
#     "price": 199.0,
#     "is_available": true
#   },

#   "menu_updated": {
#     "id": 1,
#     "name": "Spicy Tomato Soup",
#     "category": "starter",
#     "price": 109.0,
#     "is_available": true
#   },

#   "menu_deleted": {
#     "detail": "Menu item deleted"
#   },

#   "order_created": {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       {"menu_item_id": 1, "quantity": 2},
#       {"menu_item_id": 3, "quantity": 4}
#     ],
#     "status": "pending",
#     "special_instruction": "Less spicy"
#   },

#   "orders_list": [
#     {
#       "id": 1,
#       "order_type": "dine_in",
#       "table_number": 5,
#       "items": [
#         {"menu_item_id": 1, "quantity": 2},
#         {"menu_item_id": 3, "quantity": 4}
#       ],
#       "status": "pending",
#       "special_instruction": "Less spicy"
#     }
#   ],

#   "order_single": {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       {"menu_item_id": 1, "quantity": 2},
#       {"menu_item_id": 3, "quantity": 4}
#     ],
#     "status": "pending",
#     "special_instruction": "Less spicy"
#   },

#   "order_status_updated": {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 5,
#     "items": [
#       {"menu_item_id": 1, "quantity": 2},
#       {"menu_item_id": 3, "quantity": 4}
#     ],
#     "status": "in_progress",
#     "special_instruction": "Less spicy"
#   },

#   "order_total_amount": {
#     "order_id": 1,
#     "total_amount": 394.0
#   }
# }