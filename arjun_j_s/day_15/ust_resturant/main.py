from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime, time

app = FastAPI(title="SpiceHub")

# Sample menu data
menu_list = [
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
    }
]

orders = []  # list of Order dicts
next_menu_id = 5  # ID for the next menu item
next_order_id = 1  # ID for the next order


# Pydantic models to define data structures
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
    is_available: bool  # Whether the item is available or not


class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int


class Order(BaseModel):
    id: int
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    status: str = "pending"  # Default status is pending
    special_instructions: str = None


class CreateOrder(BaseModel):
    order_type: str
    table_number: int = None
    items: List[OrderItem]
    special_instructions: str = None


# Endpoint to add a new menu item
@app.post("/menu", response_model=MenuItem)
def add_menu_item(menu: CreateMenu):
    global next_menu_id
    
    # Create a new MenuItem object
    new_menu = MenuItem(id=next_menu_id,
                       name=menu.name,
                       category=menu.category,
                       price=menu.price)
    
    menu_list.append(new_menu.__dict__)  # Add the new menu item to the list
    next_menu_id += 1  # Increment the ID for next menu item
    return new_menu


# Endpoint to fetch all menu items, optionally filtered by availability
@app.get("/menu", response_model=List[MenuItem])
def get_all_menu_items(is_available: Optional[bool] = False):
    true_list = []
    if not is_available:  # If no filter is provided, return all items
        return menu_list
    # Filter menu items based on availability
    for data in menu_list:
        if data["is_available"] == is_available:
            true_list.append(data)

    return true_list


# Endpoint to fetch a menu item by its ID
@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item_by_id(id: int):
    for data in menu_list:
        if data["id"] == id:
            return data
    
    raise HTTPException(status_code=404, detail="Menu Not Found")


# Endpoint to update an existing menu item by its ID
@app.put("/menu/{id}", response_model=MenuItem)
def update_menu(id: int, update_menu: UpdateMenu):
    updated = get_menu_item_by_id(id)
    if updated:
        new_changes = MenuItem(
            id=id,
            name=update_menu.name,
            category=update_menu.category,
            price=update_menu.price,
            is_available=update_menu.is_available
        )
        # Update the item in the menu list
        for i in range(len(menu_list)):
            if menu_list[i]["id"] == id:
                menu_list[i] = new_changes.__dict__
                return new_changes
    else:
        raise HTTPException(status_code=404, detail="Not Found")


# Endpoint to delete a menu item by its ID
@app.delete("/menu/{id}", response_model=MenuItem)
def delete_menu(id: int):
    if get_menu_item_by_id(id):
        return menu_list.pop(id - 1)  # Remove the item from the list (ID starts from 1)
    else:
        raise HTTPException(status_code=404, detail="Not Found")


# Endpoint to create a new order
@app.post("/order", response_model=Order)
def add_order(order: CreateOrder):
    # Validation for order type and table number
    if order.order_type == "dine_in" and order.table_number <= 0:
        raise HTTPException(status_code=400, detail="Not valid")
    if order.order_type == "take_away" and order.table_number > 0:
        raise HTTPException(status_code=400, detail="Not valid")
    
    # Ensure all ordered items are available
    for data in order.items:
        if not get_menu_item_by_id(data.menu_item_id)["is_available"]:
            raise HTTPException(status_code=400, detail="Not valid")
    
    global next_order_id
    # Create a new Order object
    new_order = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_number=order.table_number,
        items=order.items,
        special_instructions=order.special_instructions
    )
    orders.append(new_order.__dict__)  # Add the order to the list
    next_order_id += 1  # Increment the order ID for next order
    return new_order


# Endpoint to fetch all orders, optionally filtered by status
@app.get("/orders", response_model=List[Order])
def get_all_orders(status: Optional[str] = "pending"):
    lis = []
    for data in orders:
        if data["status"] == status:  # Filter orders by status
            lis.append(data)
    return lis


# Endpoint to fetch a specific order by ID
@app.get("/orders/{id}", response_model=Order)
def get_orders(id: int):
    for data in orders:
        if data["id"] == id:
            return data
    raise HTTPException(status_code=404, detail="Not Found")


# Endpoint to update the status of an order
@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, status: str):
    if get_orders(id):
        for i in range(len(orders)):
            if orders[i]["id"] == id:
                if orders[i]["status"] == "pending" and status != "completed":
                    orders[i]["status"] = status
                elif orders[i]["status"] == "in_progress" and status != "in_progress":
                    orders[i]["status"] = status
                else:
                    # If the order is already completed or cancelled, return an error
                    if orders[i]["status"] in ["completed", "cancelled"]:
                        raise HTTPException(
                            status_code=400,
                            detail="Already completed Order" if orders[i]["status"] == "completed" else "Already Cancelled"
                        )
        return get_orders(id)


# Endpoint to calculate the total amount of an order
@app.get("/orders/{id}/totalamount")
def calculate_total(id: int):
    if get_orders(id):
        data = get_orders(id)
        total = 0
        for row in data["items"]:
            menu = get_menu_item_by_id(row.menu_item_id)
            total += row.quantity * menu["price"]  # Calculate the total bill
        return {"Total Bill": total}

#Output
# 1) Add a new menu item (POST /menu)
# Input:
# {
#   "name": "Veg Biryani",
#   "category": "main_course",
#   "price": 199.0
# }

# Output:
# {
#   "id": 5,
#   "name": "Veg Biryani",
#   "category": "main_course",
#   "price": 199.0,
#   "is_available": true
# }

# --------------------------------------------------

# 2) Get all menu items (GET /menu)
# Input:
# GET /menu

# Output:
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
#   },
#   {
#     "id": 5,
#     "name": "Veg Biryani",
#     "category": "main_course",
#     "price": 199.0,
#     "is_available": true
#   }
# ]

# --------------------------------------------------

# 3) Create a new order (POST /order)
# Input:
# {
#   "order_type": "dine_in",
#   "table_number": 3,
#   "items": [
#     { "menu_item_id": 2, "quantity": 1 },
#     { "menu_item_id": 3, "quantity": 2 }
#   ],
#   "special_instructions": "Less spicy please"
# }

# Output:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 3,
#   "items": [
#     { "menu_item_id": 2, "quantity": 1 },
#     { "menu_item_id": 3, "quantity": 2 }
#   ],
#   "status": "pending",
#   "special_instructions": "Less spicy please"
# }

# --------------------------------------------------

# 4) Get all pending orders (GET /orders?status=pending)
# Input:
# GET /orders?status=pending

# Output:
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
#     "special_instructions": "Less spicy please"
#   }
# ]

# --------------------------------------------------

# 5) Update order status (PATCH /orders/1/status)
# Input:
# PATCH /orders/1/status?status=in_progress

# Output:
# {
#   "id": 1,
#   "order_type": "dine_in",
#   "table_number": 3,
#   "items": [
#     { "menu_item_id": 2, "quantity": 1 },
#     { "menu_item_id": 3, "quantity": 2 }
#   ],
#   "status": "in_progress",
#   "special_instructions": "Less spicy please"
# }

# --------------------------------------------------

# 6) Calculate total bill (GET /orders/1/totalamount)
# Input:
# GET /orders/1/totalamount

# Output:
# {
#   "Total Bill": 347.0
# }