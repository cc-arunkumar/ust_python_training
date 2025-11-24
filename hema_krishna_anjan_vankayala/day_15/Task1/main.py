from typing import List
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel 

# Initialize FastAPI app with title
app = FastAPI(title="SpiceHub")

# Data model for menu items
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float 
    is_available: bool 

# Data model for individual order items
class OrderItem(BaseModel):
    menu_item_id: int 
    quantity: int 

# Data model for complete orders
class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str
    special_instructions: str = None

# In-memory menu and order storage
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]
orders = []  # list of Order dicts
next_menu_id = 5
next_order_id = 1

# ---------------- MENU ENDPOINTS ----------------
# GET /menu → List all menu items (optionally filter by availability)
@app.get('/menu')
def get_all_list_menu(only_available: bool = False):
    # Return all menu items or only available ones if query param is set
    if not only_available:
        return menu 
    else:
        new_li = [item for item in menu if item['is_available']]
        return new_li

# GET /menu/{id} → Retrieve single menu item by ID
@app.get('/men/{id}')
def get_menu_id(id: int):
    # Return menu item by id or 404 if not found
    for li in menu:
        if li['id'] == id:
            return li 
    raise HTTPException(status_code=404, detail='Menu item not found')

# POST /menu → Add new menu item
@app.post('/menu', response_model=MenuItem)
def add_new_item(new_menu_item: MenuItem):
    # Add new menu item with auto-incremented id
    global next_menu_id
    new_menu_item.id = next_menu_id
    next_menu_id += 1 
    menu.append(new_menu_item)
    return new_menu_item 

# PUT /menu/{id} → Update existing menu item
@app.put('/menu/{id}', response_model=MenuItem)
def update_menu_item(id: int, updated_item: MenuItem):
    # Update existing menu item by id or return 404 if not found
    for item in menu:
        if item['id'] == id:
            item['name'] = updated_item.name
            item['category'] = updated_item.category
            item['price'] = updated_item.price
            item['is_available'] = updated_item.is_available
            return updated_item
    raise HTTPException(status_code=404, detail="Item Not Found!")

# DELETE /menu/{id} → Delete menu item
@app.delete('/menu/{id}')
def delete_item(id: int):
    # Delete menu item by id or return 404 if not found
    for item in menu:
        if item['id'] == id:
            menu.pop(id - 1)
            return {'details': 'Menu item deleted'}
    raise HTTPException(status_code=404, detail="Menu Item Not Found")

# ---------------- ORDER ENDPOINTS ----------------

# POST /orders → Create new order (dine-in or takeaway)
@app.post('/orders', response_model=Order)
def create_order(new_order: Order):
    # Create new order with validation for items and availability
    item_id_list = [item['id'] for item in menu]
    for it in new_order.items:
        if it.quantity <= 0:
            raise HTTPException(status_code=400, detail="Invalid Quantity")
        if it.menu_item_id not in item_id_list:
            raise HTTPException(status_code=404, detail="Menu Item not Found!")
        for item in menu:
            if it.menu_item_id == item['id'] and not item['is_available']:
                raise HTTPException(status_code=400, detail="Item is Not Available!")

    global next_order_id 
    if new_order.order_type == 'takeaway':
        # Assign id and save takeaway order
        new_order.id = next_order_id
        next_order_id += 1 
        orders.append(new_order) 
        return new_order
    if new_order.order_type == 'dine_in':
        # Assign id and save dine-in order if table number is valid
        if isinstance(new_order.table_number, int):
            new_order.id = next_order_id
            next_order_id += 1 
            orders.append(new_order)   
            return new_order
        else:
            raise HTTPException(status_code=400, detail="Invalid Table Number")
    else:
        raise HTTPException(status_code=400, detail="Invalid Order Type")

# GET /orders → List all orders (optionally filter by status)
@app.get('/orders', response_model=List[Order])
def get_all_orders(status: str = None):
    # Return all orders or filter by status if provided
    if status is not None:
        return [ord for ord in orders if ord.status == status]
    else:
        return orders

# GET /orders/{id} → Retrieve single order by ID
@app.get('/orders/{id}')
def get_order_id(id: int):
    # Return order by id or 404 if not found
    for ord in orders:
        if ord.id == id:
            return ord 
    raise HTTPException(status_code=404, detail="Order Not Found")

# PATCH /orders/{id}/status → Update order status with allowed transitions
@app.patch('/orders/{id}/status')
def update_status(id: int, payload: dict):
    # Update order status with allowed transitions
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
    
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
    
    if not payload or "status" not in payload:
        raise HTTPException(status_code=400, detail="Missing 'status' in request body")
    
    new_status = payload["status"]
    current_status = order_found.status
    
    allowed_transitions = {
        "pending": ["in_progress", "cancelled"],
        "in_progress": ["completed", "cancelled"],
        "completed": [],
        "cancelled": []
    }
    
    if current_status not in allowed_transitions:
        raise HTTPException(status_code=400, detail=f"Unknown current status: {current_status}")
    
    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(status_code=400, detail=f"Cannot transition from '{current_status}' to '{new_status}'")
    
    order_found.status = new_status
    return order_found

# GET /orders/{id}/total-amount → Calculate total bill for an order
@app.get('/orders/{id}/total-amount')
def get_order_total(id: int):
    # Calculate total bill amount for an order
    order_found = None
    for ord in orders:
        if ord.id == id:
            order_found = ord
            break
    
    if order_found is None:
        raise HTTPException(status_code=404, detail="Order Not Found")
    
    total_amount = 0.0
    for order_item in order_found.items:
        menu_item = None
        for item in menu:
            if item['id'] == order_item.menu_item_id:
                menu_item = item
                break
        
        if menu_item is not None:
            total_amount += menu_item['price'] * order_item.quantity
    
    return {
        "order_id": id,
        "total_amount": total_amount
    }
