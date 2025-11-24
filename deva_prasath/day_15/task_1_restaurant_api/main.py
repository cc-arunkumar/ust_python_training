#  You are building a small REST API for a restaurant called “SpiceHubˮ.
#  The API will help restaurant staff to:
#   Manage the menu (add, view, update, delete dishes).
#   Take orders from customers (dine-in or takeaway).
#   Track order status (pending → in_progress → completed / cancelled).
#   Calculate total bill for an order.
#  Everything is stored in memory (Python lists/dicts)



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI(title="Spice Hub")

# MenuItem model for defining menu items
class MenuItem(BaseModel):
    id:int  # ID of the menu item
    name:str  # Name of the dish
    category:str  # Category of the dish (e.g., starter, main_course, dessert)
    price:float  # Price of the dish
    is_available:bool  # Whether the dish is available or not

# OrderItem model for defining items in an order
class OrderItem(BaseModel):
    menu_item_id:int  # ID of the menu item ordered
    quantity:int  # Quantity of the menu item ordered

# Sample menu data
menu=[
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# Orders and ID tracking variables
orders=[]
next_menu_id=5  # Initial menu ID for new dishes
next_order_id=1  # Initial order ID

@app.get("/menu",response_model=List[MenuItem])
def get_menu(only_available:Optional[bool]=False):
    """
    API to get the entire menu or filter only available items.
    - If `only_available` is True, returns only available items from the menu.
    """
    if only_available:
        available_items=[]
        for item in menu:
            if item["is_available"]:
                available_items.append(item)
        return available_items
    return menu  # Return all menu items if no filter is applied

@app.get("/menu/{id}")
def get_menu_item(id:int):
    """
    API to retrieve a specific menu item by its ID.
    - Returns the menu item details if found, or raises an error if not found.
    """
    item=None
    for menu_it in menu:
        if menu_it["id"]==id:
            item=menu_it
            break
    if item is None:
        raise HTTPException(status_code=404,detail="Menu item not found")

    return item  # Return the found menu item

@app.post("/menu")
def create_menu(item:MenuItem):
    """
    API to add a new menu item.
    - Increments the menu ID and adds the item to the menu list.
    """
    global next_menu_id
    item_data={
        "id":next_menu_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available
    }
    menu.append(item_data)  # Add the new item to the menu
    next_menu_id+=1  # Increment the menu ID for the next item
    
    return item_data  # Return the newly added menu item

@app.put("/menu/{id}")
def update_menu(id:int,updated_item:MenuItem):
    """
    API to update an existing menu item by its ID.
    - Finds the item by ID and updates its details.
    """
    for item in menu:
        if item['id']==id:
            item['name']=updated_item.name
            item['category']=updated_item.category
            item['price']=updated_item.price
            item['is_available']=updated_item.is_available
            return item  # Return the updated item
    raise HTTPException(status_code=404,detail="Menu item not available")  # Item not found


@app.delete("/menu/{id}")
def delete_menu(id:int):
    """
    API to delete a menu item by its ID.
    - Removes the item from the menu if found.
    """
    for item in menu:
        if item["id"] == id:
            menu.remove(item)  # Remove the menu item
            return {"detail": "Menu item deleted"}  # Confirmation message
    
    raise HTTPException(status_code=404, detail="Menu item not found")  # Item not found


# OrderCreate model to handle order creation data
class OrderCreate(BaseModel):
    id:int  # ID of the order
    order_type:str  # Type of order (dine_in or takeaway)
    table_number:Optional[int]=None  # Table number (only for dine_in)
    items:List[OrderItem]  # List of ordered items
    status:str  # Status of the order (pending, in_progress, etc.)
    special_instructions:Optional[str]=None  # Special instructions for the order

@app.post("/orders")
def create_orders(order_data:OrderCreate):
    """
    API to create a new order.
    - Validates the order details, such as order type and items.
    """
    global next_order_id
    # Validate order type
    if order_data.order_type not in ["dine_in","takeaway"]:
        raise HTTPException(status_code=400,detail="order_type must be dine_in or takeaway")
    
    # Validate table number for dine-in orders
    if order_data.order_type=="dine_in":
        if order_data.table_number is None or order_data.table_number<0:
            raise HTTPException(status_code=400,detail="table_number must be a positive integer for dine_in")
    else:
        if order_data.table_number is not None:
            raise HTTPException(status_code=400,detail="takeaway must not have table number")
    
    if len(order_data.items)==0:
        raise HTTPException(status_code=400,detail="Order must contain atleast one item")
    
    # Validate each item in the order
    for item in order_data.items:
        if item.quantity<0:
            raise HTTPException(status_code=400,detail="Quantity must be greater than 0")
        
        menu_item=None
        for m in menu:
            if m["id"]==item.menu_item_id:
                menu_item=m
                break
        
        if menu_item is None:
            raise HTTPException(status_code=400, detail=f"Menu item with id{item.menu_item_id} not found")

        if not menu_item["is_available"]:
            raise HTTPException(status_code=400, detail=f"Menu item '{menu_item['name']}' is not available")
        
        new_order={
            "id":next_order_id,
            "order_type":order_data.order_type,
            "table_number":order_data.table_number,
            "items":[
                {"menu_item_id": item.menu_item_id, "quantity": item.quantity}
            for item in order_data.items
            ],
            "status": "pending",
            "special_instructions": order_data.special_instructions
        }
        orders.append(new_order)  # Add the new order
        next_order_id+=1  # Increment the order ID
        return new_order  # Return the newly created order

@app.get("/orders")
def get_all_orders(status:Optional[str]=None):
    """
    API to get all orders or filter by status.
    - If a status is provided, returns orders with that status.
    """
    if status is not None:
        filtered_orders=[]
        for order in orders:
            if order["status"]==status:
                filtered_orders.append(order)
        return filtered_orders
    return orders  # Return all orders

@app.get("/orders/{id}")
def getidorder(id: int):
    """
    API to retrieve a specific order by its ID.
    - Returns the order if found, or raises an error if not found.
    """
    for order in orders:
        if order['id']==id:
            return orders
    raise HTTPException(status_code=404,detail="Order not found")  # Order not found


# StatusUpdate model for updating order status
class StatusUpdate(BaseModel):
    status: str  # New status of the order

@app.patch("/orders/{id}/status")
def update_order_status(id: int, payload: StatusUpdate):
    """
    API to update the status of an existing order.
    - Validates status transitions based on the current order status.
    """
    order=None
    for o in orders:
        if o["id"]==id:
            order=o
            break
    if order is None:
        raise HTTPException(status_code=404,detail="Order not found")

    new_status=payload.status
    current_status=order["status"]

    # Validate status transitions
    if current_status=="pending" and new_status not in ["in_progress","cancelled"]:
        raise HTTPException(status_code=400,detail="Not allowed")
    
    if current_status == "in_progress" and new_status not in ["completed","cancelled"]:
        raise HTTPException(status_code=400,detail="Not allowed")
    
    if current_status in ["completed", "cancelled"]:
        raise HTTPException(status_code=400,detail=f"Order is already{current_status}.Cannot change status")

    order["status"]=new_status  # Update the order status
    return order  # Return the updated order

@app.get("/orders/{id}/total_amount")
def get_order_total(id:int):
    """
    API to calculate and retrieve the total amount for a specific order.
    - Calculates the total amount based on the items in the order.
    """
    order=None
    for o in orders:
        if o["id"]==id:
            order=o
            break
    if order is None:
        raise HTTPException(status_code=404,detail="Order not found")

    total=0.0
    for item in order['items']:
        menu_item_id=item["menu_item_id"]
        quantity=item["quantity"]
        menu_item=None
        for m in menu:
            if m['id']==menu_item_id:
                menu_item=m
                break
        total+=menu_item["price"]*quantity   # Add item price multiplied by quantity to total
    return{
        "order_id":id,
        "total_amount":round(total,2)  # Return the total amount rounded to 2 decimal places
    }







#Sample output

# Sample Output for Day 15 Testing (Important Test Cases)

# Test 1: Get All Menu Items
## Input:
# GET /menu

# ## Output:
# HTTP Status: 200 OK
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

# # Test 2: Get Single Menu Item by ID
# ## Input:
# GET /menu/1

# ## Output:
# HTTP Status: 200 OK
# {
#   "id": 1,
#   "name": "Tomato Soup",
#   "category": "starter",
#   "price": 99.0,
#   "is_available": true
# }

# # Test 3: Create Menu Item (Add New Dish)
# ## Input:
# POST /menu
# {
#   "name": "Masala Dosa",
#   "category": "main_course",
#   "price": 129.0,
#   "is_available": true
# }

# ## Output:
# HTTP Status: 201 Created
# {
#   "id": 5,
#   "name": "Masala Dosa",
#   "category": "main_course",
#   "price": 129.0,
#   "is_available": true
# }

# # Test 4: Update Menu Item
# ## Input:
# PUT /menu/1
# {
#   "name": "Butter Naan (Large)",
#   "category": "main_course",
#   "price": 69.0,
#   "is_available": true
# }

# ## Output:
# HTTP Status: 200 OK
# {
#   "id": 1,
#   "name": "Butter Naan (Large)",
#   "category": "main_course",
#   "price": 69.0,
#   "is_available": true
# }

# # Test 5: Delete Menu Item
# ## Input:
# DELETE /menu/4

# ## Output:
# HTTP Status: 200 OK
# {
#   "detail": "Menu item deleted"
# }

# # Test 6: Create Dine-in Order
# ## Input:
# POST /orders
# {
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 3, "quantity": 4 }
#   ],
#   "special_instructions": "less spicy"
# }

# ## Output:
# HTTP Status: 201 Created
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 3, "quantity": 4 }
#   ],
#   "status": "pending",
#   "special_instructions": "less spicy"
# }

# # Test 7: Get All Orders
# ## Input:
# GET /orders

# ## Output:
# HTTP Status: 200 OK
# [
#   {
#     "id": 1,
#     "order_type": "dine_in",
#     "table_number": 12,
#     "items": [
#       { "menu_item_id": 1, "quantity": 2 },
#       { "menu_item_id": 3, "quantity": 4 }
#     ],
#     "status": "pending",
#     "special_instructions": "less spicy"
#   }
# ]

# # Test 8: Get Order by ID
# ## Input:
# GET /orders/1

# ## Output:
# HTTP Status: 200 OK
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 3, "quantity": 4 }
#   ],
#   "status": "pending",
#   "special_instructions": "less spicy"
# }

# # Test 9: Update Order Status
# ## Input:
# PATCH /orders/1/status
# {
#   "status": "in_progress"
# }

# ## Output:
# HTTP Status: 200 OK
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 12,
#   "items": [
#     { "menu_item_id": 1, "quantity": 2 },
#     { "menu_item_id": 3, "quantity": 4 }
#   ],
#   "status": "in_progress",
#   "special_instructions": "less spicy"
# }

# # Test 10: Calculate Total Amount for Order
# ## Input:
# GET /orders/1/total-amount

# ## Output:
# HTTP Status: 200 OK
# {
#   "order_id": 1,
#   "total_amount": 394.0
# }
