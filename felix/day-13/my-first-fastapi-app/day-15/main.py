from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="SpiceHub")

"""
 Pydantic Models
"""

# ------------ Menu Item (Full Model) ------------
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool = True


# ------------ MenuItemCreate (Input Model) ------------
# Used when adding or updating menu items; excludes ID field
class MenuItemCreate(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool = True


# ------------ Order Item Model ------------
class OrderItem(BaseModel):
    menu_item_id: int      # reference to MenuItem.id
    quantity: int          # must be > 0 (validated in route)


# ------------ Complete Order Model ------------
class Order(BaseModel):
    id: int
    order_type: str
    table_no: int
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: str = None


# ------------ OrderCreate (Input Model) ------------
class OrderCreate(BaseModel):
    order_type: str
    table_no: int
    items: List[OrderItem]
    status: str = "pending"
    special_instructions: str = None


# ------------ Status Update Model ------------
class Status(BaseModel):
    status: str


# Initial menu items (list of dictionaries)
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
    }
]

orders = []              # stores orders (each order is a dictionary)
next_menu_id = 5         # auto-increment for menu items
next_order_id = 1        # auto-increment for orders


"""
MENU ROUTES
"""

# ------------ Get all menu items ------------
@app.get("/menu-list")
def menu_list(only_available: bool = False):
    """
    Returns full menu.
    If only_available=True → returns items where is_available=True.
    """
    if only_available:
        return [item for item in menu if item["is_available"]]

    return menu


# ------------ Get single menu item by ID ------------
@app.get("/menu/{id}")
def single_item(id: int):
    """
    Fetch a menu item by its ID.
    Raises 404 if not found.
    """
    for i in menu:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail="Menu item not found")


# ------------ Add a new menu item ------------
@app.post("/menu")
def add_new_menu_item(menu_item: MenuItemCreate):
    """
    Adds a new menu item.
    ID is auto-generated.
    """
    global next_menu_id

    # Create full MenuItem object
    item = MenuItem(
        id=next_menu_id,
        name=menu_item.name,
        category=menu_item.category,
        price=menu_item.price,
        is_available=menu_item.is_available
    )

    menu.append(item.__dict__)
    next_menu_id += 1
    return item


# ------------ Update a menu item by ID ------------
@app.put("/menu/{id}")
def update_menu_item(id: int, menu_item: MenuItemCreate):
    """
    Updates an existing menu item using its ID.
    Replaces entire object.
    """
    updated_item = MenuItem(
        id=id,
        name=menu_item.name,
        category=menu_item.category,
        price=menu_item.price,
        is_available=menu_item.is_available
    )

    # Search for item and update
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            menu[i] = updated_item.__dict__
            return {"updated": menu[i]}

    raise HTTPException(status_code=404, detail="Item not found")


# ------------ Delete a menu item ------------
@app.delete("/menu/{id}")
def delete_item(id: int):
    """
    Deletes a menu item by ID.
    """
    for i in range(len(menu)):
        if menu[i]["id"] == id:
            return menu.pop(i)

    raise HTTPException(status_code=404, detail="Item not found")


"""
ORDER ROUTES
"""

# ------------ Create a new order ------------
@app.post("/orders")
def new_order(order: OrderCreate):
    """
    Creates a new order.
    Validations:
    - Quantity must be > 0
    - Menu item must be available
    """

    # Validate order items
    order_dict = order.__dict__

    for item in order_dict["items"]:
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

        # Check if ordered item is available
        for m in menu:
            if m["id"] == item.menu_item_id and not m["is_available"]:
                raise HTTPException(status_code=400, detail="Item not available")

    global next_order_id

    new_order_obj = Order(
        id=next_order_id,
        order_type=order.order_type,
        table_no=order.table_no,
        items=order.items,
        status=order.status,
        special_instructions=order.special_instructions
    )

    orders.append(new_order_obj.__dict__)
    next_order_id += 1

    return {"Order placed": orders}


# ------------ Get list of orders (optional status filter) ------------
@app.get("/orders-list")
def order_list(status: str = "optional"):
    """
    Returns all orders.
    If status is given → filters by status.
    """
    if status == "optional":
        return orders

    filtered_orders = [o for o in orders if o["status"] == status]

    if filtered_orders:
        return filtered_orders

    raise HTTPException(status_code=404, detail="No orders found")


# ------------ Get a single order by ID ------------
@app.get("/order/{id}")
def get_an_order(id: int):
    """
    Returns a single order by ID.
    """
    for o in orders:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")


# ------------ Update order status ------------
@app.patch("/order/{id}/status")
def status(id: int, stat: Status):
    """
    Updates order status (e.g., pending → completed).
    """
    for o in orders:
        if o["id"] == id:
            o["status"] = stat.status
            return {"updated_status": stat.status}

    raise HTTPException(status_code=404, detail="Order not found")


# ------------ Calculate total amount for an order ------------
@app.get("/order/{id}/total-amount")
def total_amount(id: int):
    """
    Calculates total order amount by adding:
    price × quantity for each ordered item.
    """
    total = 0

    for order in orders:
        if order["id"] == id:

            for item in order["items"]:
                for m in menu:
                    if item.menu_item_id == m["id"]:
                        total += m["price"] * item.quantity

            return {"order_id": id, "total_amount": total}

    raise HTTPException(status_code=404, detail="No order found")
