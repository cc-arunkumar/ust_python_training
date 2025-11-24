from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI instance with a custom title
app = FastAPI(title="Spice Up")

# Pydantic models for data validation and serialization
class MenuItem(BaseModel):
    id: int 
    name: str 
    category: str
    price: float 
    is_available: bool = True  # Default is available

class CreateMenu(BaseModel):
    name: str 
    category: str
    price: float 
    
class UpdateMenu(BaseModel): 
    name: str 
    category: str
    price: float 
    is_available: bool

class OrderItem(BaseModel):
    menu_item_id : int  # Menu item being ordered
    quantity : int  # Quantity of the item ordered
    
class Order(BaseModel):
    id: int 
    order_type: str  # e.g., dine_in, takeaway
    table_number: int = None  # Only for dine-in orders
    items: List[OrderItem]
    status: str  = "pending"  # Initial status is 'pending'
    special_instructions: str = None  # Any special instructions from the customer
    
class CreateOrder(BaseModel):
    order_type: str  # e.g., dine_in, takeaway
    table_number: int = None  # Optional for takeaway
    items: List[OrderItem]
    special_instructions: str = None  # Optional special instructions

# Sample menu items stored in a list (typically this would be in a database)
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# Sample orders in the system
orders = [{
    "id": 1,
    "order_type": "dine_in",
    "table_number": 12,
    "items": [{"menu_item_id": 1, "quantity": 2}, {"menu_item_id": 3, "quantity": 4}],
    "status": "pending",
    "special_instructions": "less spicy"
}]
next_menu_id = 5  # ID for the next menu item
next_order_id = 2  # ID for the next order

# Endpoint to add a new menu item
@app.post("/menu")
def add_menu_item(item: CreateMenu):
    global next_menu_id
    new_item = MenuItem(
        id=next_menu_id,
        name=item.name,
        category=item.category,
        price=item.price,
    )
    menu.append(new_item)
    next_menu_id += 1  # Increment to prepare for next menu item ID
    return new_item

# Endpoint to get all menu items, filtered by availability if specified
@app.get("/menu")
def get_all_menu_details(is_avail: Optional[bool] = False):
    temp_menu = []
    if is_avail == False:
        return menu  # Return all menu items if availability filter is not applied
    for item in menu:
        if item["is_available"] == True:
            temp_menu.append(item)
    return temp_menu

# Endpoint to get a specific menu item by its ID
@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_byid(id: int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Id not found")  # Return error if not found

# Endpoint to update a menu item by its ID
@app.put("/menu/{id}")
def update_menu(id: int, item: UpdateMenu):
    updated = get_menu_byid(id)  # Check if item exists
    if updated:
        new_menu = MenuItem(
            id=id,
            name=item.name,
            category=item.category,
            price=item.price,
            is_available=item.is_available
        )
        for i in range(len(menu)):
            if menu[i]["id"] == id:
                menu[i] = new_menu
                return new_menu
    raise HTTPException(status_code=404, detail="Menu not found")

# Endpoint to delete a menu item by its ID
@app.delete("/menu/{id}", response_model=MenuItem)
def delete_menu(id: int):
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            removed = menu.pop(i)  # Remove item from the list
            return removed
    raise HTTPException(status_code=404, detail="Menu not found")

# Endpoint to add a new order
@app.post("/orders")
def add_order_item(item: CreateOrder):
    global next_order_id
    # Validation for table number based on order type
    if item.order_type == "dine_in" and item.table_number == 0:
        raise HTTPException(status_code=400, detail="For dine in, table should be placed")
    elif item.order_type == "takeaway" and item.table_number > 0:
        raise HTTPException(status_code=400, detail="For takeaway, no table should be placed")
    
    # Check if all items in the order are available
    for data in item.items:
        if not get_menu_byid(data.menu_item_id)["is_available"]:
            raise HTTPException(status_code=400, detail="Invalid menu item")
    
    new_item = Order(
        id=next_order_id,
        order_type=item.order_type,
        table_number=item.table_number,
        items=item.items,
        special_instructions=item.special_instructions
    )
    orders.append(new_item)
    next_order_id += 1  # Increment to prepare for the next order ID
    return new_item

# Endpoint to get all orders, filtered by status if provided
@app.get("/order")
def get_all_order_details(status: Optional[str] = None):
    temp_orders = []
    if status == None:
        return orders
    for item in orders:
        if item["status"] == status:
            temp_orders.append(item)
    return temp_orders

# Endpoint to get details of a specific order by its ID
@app.get("/order/{id}")
def get_order_details(id: int):
    for item in orders:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Order not found")

# Endpoint to update the status of an order by its ID
@app.patch("/order/{id}/status")
def update_order_status(id: int, status: str):
    for item in orders:
        if item["id"] == id:
            if item["status"] == "completed":
                raise HTTPException(status_code=400, detail="Order is already completed")
            elif item["status"] == "cancelled":
                raise HTTPException(status_code=400, detail="Order is already cancelled")
            elif item["status"] == "pending" and status != "completed":
                item["status"] = status
            elif item["status"] == "in_progress" and status != "pending":
                item["status"] = status
            else:
                raise HTTPException(status_code=400, detail="Invalid status")
            return item
    raise HTTPException(status_code=404, detail="Order not found")

# Endpoint to compute the total amount for a specific order
@app.get("/orders/{id}/total-amount")
def compute_bill(id: int):
    total = 0
    for item in orders:
        if item["id"] == id:
            for each_item in item["items"]:
                price = 0
                for each_menu_item in menu:
                    if each_menu_item["id"] == each_item["menu_item_id"]:
                        price = each_menu_item["price"]
                total += each_item["quantity"] * price
            return {"order_id": id, "Total": total}  # Return total amount for the order
    raise HTTPException(status_code=404, detail="Order not found")

# Sample Outputs for all API calls

"""
Sample Output for /menu (POST):
Input: 
{
  "name": "Mango Lassi", 
  "category": "beverage", 
  "price": 99.0 
}
Output:
{
  "id": 5,
  "name": "Mango Lassi",
  "category": "beverage",
  "price": 99.0,
  "is_available": true
}

Sample Output for /menu (GET) when is_avail=False (all items):
Output:
[
  { "id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true },
  { "id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true },
  { "id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true },
  { "id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": false }
]

Sample Output for /menu (GET) when is_avail=True:
Output:
[
  { "id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": true },
  { "id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": true },
  { "id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": true }
]

Sample Output for /menu/{id} (GET):
Input: /menu/1
Output:
{
  "id": 1,
  "name": "Tomato Soup",
  "category": "starter",
  "price": 99.0,
  "is_available": true
}

Sample Output for /menu/{id} (PUT):
Input: /menu/1 (Updated fields: name="Spicy Tomato Soup", price=109.0)
Output:
{
  "id": 1,
  "name": "Spicy Tomato Soup",
  "category": "starter",
  "price": 109.0,
  "is_available": true
}

Sample Output for /menu/{id} (DELETE):
Input: /menu/4
Output:
{
  "id": 4,
  "name": "Gulab Jamun",
  "category": "dessert",
  "price": 79.0,
  "is_available": false
}

Sample Output for /orders (POST):
Input: 
{
  "order_type": "dine_in", 
  "table_number": 10, 
  "items": [{ "menu_item_id": 1, "quantity": 2 }, { "menu_item_id": 3, "quantity": 4 }]
}
Output:
{
  "id": 2,
  "order_type": "dine_in",
  "table_number": 10,
  "items": [
    { "menu_item_id": 1, "quantity": 2 },
    { "menu_item_id": 3, "quantity": 4 }
  ],
  "status": "pending",
  "special_instructions": null
}

Sample Output for /orders/{id}/total-amount:
Input: /orders/1
Output:
{
  "order_id": 1,
  "Total": 876.0
}
"""
