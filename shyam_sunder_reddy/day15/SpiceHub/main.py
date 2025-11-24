from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI(title="Spice Hub")

# -----------------------------
# Data Models (Schemas)
# -----------------------------

class MenuItem(BaseModel):
    """Schema for a menu item in the restaurant."""
    id: int
    name: str
    category: str
    price: float
    is_available: bool


class OrderItem(BaseModel):
    """Schema for an item inside an order."""
    menu_item_id: int
    quantity: int


class Order(BaseModel):
    """Schema for a customer order."""
    id: int
    order_type: str   # "dine_in" or "takeaway"
    table_number: int = None
    items: List[OrderItem]
    status: str = "pending"
    special_instruction: str = "Nothing"


# -----------------------------
# In-Memory Storage (Mock DB)
# -----------------------------

menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

orders: List[Order] = []
next_menu_id = 4
next_order_id = 0


# -----------------------------
# LEVEL 1 – Menu CRUD
# -----------------------------

@app.get("/menu", response_model=List[MenuItem])
def display_all(flag: bool = False):
    """
    Get all menu items.
    If flag=True, return only available items.

    Sample Output:
    GET /menu
    [
      {"id":1,"name":"Tomato Soup","category":"starter","price":99.0,"is_available":true},
      {"id":2,"name":"Paneer Butter Masala","category":"main_course","price":249.0,"is_available":true},
      {"id":3,"name":"Butter Naan","category":"main_course","price":49.0,"is_available":true},
      {"id":4,"name":"Gulab Jamun","category":"dessert","price":79.0,"is_available":false}
    ]
    """
    if flag:
        return [item for item in menu if item["is_available"]]
    return menu


@app.get("/menu/{id}", response_model=MenuItem)
def search_byid(id: int):
    """
    Get a menu item by ID.

    Sample Output:
    GET /menu/2
    {"id":2,"name":"Paneer Butter Masala","category":"main_course","price":249.0,"is_available":true}
    """
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")


@app.post("/menu", response_model=MenuItem)
def create_new_item(new_item: MenuItem):
    """
    Add a new menu item.

    Sample Output:
    POST /menu
    {
      "id": 5,
      "name": "Veg Biryani",
      "category": "main_course",
      "price": 199.0,
      "is_available": true
    }
    """
    global next_menu_id
    next_menu_id += 1
    new_item.id = next_menu_id
    menu.append(new_item.dict())
    return new_item


@app.put("/menu/{id}", response_model=MenuItem)
def updating_byid(id: int, new_item: MenuItem):
    """
    Update an existing menu item by ID.

    Sample Output:
    PUT /menu/3
    {
      "id":3,
      "name":"Garlic Naan",
      "category":"main_course",
      "price":59.0,
      "is_available":true
    }
    """
    for item in menu:
        if item["id"] == id:
            item.update(new_item.dict())
            return item
    raise HTTPException(status_code=404, detail="item does not exist")


@app.delete("/menu/{id}")
def deleting_byid(id: int):
    """
    Delete a menu item by ID.

    Sample Output:
    DELETE /menu/4
    {"detail":"Menu item deleted"}
    """
    for item in menu:
        if item["id"] == id:
            menu.remove(item)
            return {"detail": "Menu item deleted"}
    raise HTTPException(status_code=404, detail="Menu item not found")


# -----------------------------
# LEVEL 2 – Orders
# -----------------------------

@app.post("/orders", response_model=Order)
def creating_order(new_order: Order):
    """
    Create a new order.

    Sample Output:
    POST /orders
    {
      "id": 1,
      "order_type": "dine_in",
      "table_number": 5,
      "items": [
        {"menu_item_id": 2, "quantity": 1},
        {"menu_item_id": 3, "quantity": 2}
      ],
      "status": "pending",
      "special_instruction": "Less spicy"
    }
    """
    global next_order_id
    next_order_id += 1

    if new_order.order_type == "dine_in":
        if new_order.table_number is None or new_order.table_number <= 0:
            raise HTTPException(status_code=400, detail="table number cannot be negative")

    for order_item in new_order.items:
        if order_item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Quantity must be positive")
        if not any(m["id"] == order_item.menu_item_id for m in menu):
            raise HTTPException(status_code=400, detail="Item not in menu")

    new_order.id = next_order_id
    orders.append(new_order)
    return new_order


@app.get("/orders", response_model=List[Order])
def display_orders(stat: str = None):
    """
    Get all orders or filter by status.

    Sample Output:
    GET /orders
    [
      {
        "id": 1,
        "order_type": "dine_in",
        "table_number": 5,
        "items": [
          {"menu_item_id": 2, "quantity": 1},
          {"menu_item_id": 3, "quantity": 2}
        ],
        "status": "pending",
        "special_instruction": "Less spicy"
      }
    ]
    """
    if stat is None:
        return orders
    return [order for order in orders if order["status"] == stat]


@app.get("/orders/{id}", response_model=Order)
def display_specific_order(id: int):
    """
    Get a specific order by ID.

    Sample Output:
    GET /orders/1
    {
      "id": 1,
      "order_type": "dine_in",
      "table_number": 5,
      "items": [
        {"menu_item_id": 2, "quantity": 1},
        {"menu_item_id": 3, "quantity": 2}
      ],
      "status": "pending",
      "special_instruction": "Less spicy"
    }
    """
    for order in orders:
        if order.id == id:
            return order
    raise HTTPException(status_code=404, detail="Order Not Found")


# -----------------------------
# LEVEL 3 – Status + Billing
# -----------------------------

@app.patch("/orders/{id}/status", response_model=Order)
def update_status(id: int, change: str):
    """
    Update order status.

    Sample Output:
    PATCH /orders/1/status?change=in_progress
    {
      "id": 1,
      "order_type": "dine_in",
      "table_number": 5,
      "items": [
        {"menu_item_id": 2, "quantity": 1},
        {"menu_item_id": 3, "quantity": 2}
      ],
      "status": "in_progress",
      "special_instruction": "Less spicy"
    }
    """
    for order in orders:
        if order.id == id:
            current_status = order.status
            if change == "cancelled":
                order.status = "cancelled"
            elif current_status == "pending" and change == "in_progress":
                order.status = "in_progress"
            elif current_status == "in_progress" and change == "completed":
                order.status = "completed"
            else:
                raise HTTPException(status_code=400, detail="Illegal transition")
            return order
    raise HTTPException(status_code=404, detail="Order Not Found")

@app.get("/orders/{id}/total-amount-compute")
def get_total_bill(id: int):
    """
    Compute the total bill for a given order ID.
    - Iterates through all orders to find the matching order.
    - For each item in the order, multiplies menu price × quantity.
    - Returns the total amount for the order.
    - Raises 404 if order not found.

    Sample Output:
    GET /orders/1/total-amount-compute
    {
      "order_id": 1,
      "total_amount": 347.0
    }

    Error Case:
    GET /orders/99/total-amount-compute
    Response: 404 {"detail":"Order Not Found"}
    """
    for order in orders:
        if order.id == id:
            total = 0
            # Calculate total by iterating over order items
            for order_item in order.items:
                for menu_item in menu:
                    if menu_item["id"] == order_item.menu_item_id:
                        total += (menu_item["price"] * order_item.quantity)
            return {"order_id": id, "total_amount": total}

    # If no order matches the given ID
    raise HTTPException(status_code=404, detail="Order Not Found")
