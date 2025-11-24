from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Hotel Management Console")

# MenuItem model to represent individual menu items
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool

# Sample menu items stored in memory
menu_items: List[MenuItem] = [
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
next_id = 4  # Used for generating new IDs for menu items

# OrderItem model to represent items in a customer order
class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int

# Order model to represent a customer's full order
class Order(BaseModel):
    id: int
    order_type: str  # e.g., "dine-in", "takeaway"
    table_number: int
    items: List[OrderItem]
    value: str = "pending"  # Order status ("pending", "completed", etc.)
    special_instructions: str

# Orders stored in memory
orders: List[Order] = []
next_order_id = 1  # Used for generating new order IDs


# -------------------- API Endpoints --------------------

# -------------------- Get Menu --------------------
@app.get("/hotel")
def get_menu():
    """
    Returns the full menu of items.

    Sample Output:
    {
        "Menu": [
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
    }
    """
    return {"Menu": menu_items}


# -------------------- Get Menu Item by ID --------------------
@app.get("/hotel/{id}")
def get_menu_by_id(id: int):
    """
    Fetches a single menu item by its ID.

    Sample Input: /hotel/1

    Sample Output:
    {
        "Item details": {
            "id": 1,
            "name": "Tomato Soup",
            "category": "starter",
            "price": 99.0,
            "is_available": True
        }
    }

    If item not found:
    {
        "detail": "Menu item not found"
    }
    """
    for item in menu_items:
        if item["id"] == id:
            return {"Item details": item}
    raise HTTPException(status_code=404, detail="Menu item not found")


# -------------------- Add Menu Item --------------------
@app.post("/hotel/addmenu")
def add_menu(m_item: MenuItem):
    """
    Adds a new menu item.

    Sample Input:
    {
        "name": "Chicken Biryani",
        "category": "main_course",
        "price": 299.0,
        "is_available": True
    }

    Sample Output:
    {
        "id": 5,
        "name": "Chicken Biryani",
        "category": "main_course",
        "price": 299.0,
        "is_available": True
    }
    """
    global next_id
    next_id += 1
    m_item.id = next_id
    menu_items.append(m_item)
    return m_item


# -------------------- Update Menu Item --------------------
@app.put("/hotel/update_menu/{id}")
def update_menu(id: int, updated_menu: MenuItem):
    """
    Updates an existing menu item by its ID.

    Sample Input (to update the item with id=1):
    {
        "id": 1,
        "name": "Tomato Soup (Spicy)",
        "category": "starter",
        "price": 109.0,
        "is_available": True
    }

    Sample Output (after update):
    {
        "Item updated": {
            "id": 1,
            "name": "Tomato Soup (Spicy)",
            "category": "starter",
            "price": 109.0,
            "is_available": True
        }
    }

    If item not found:
    {
        "detail": "item not found in menu"
    }
    """
    for data in menu_items:
        if data["id"] == id:
            data["id"] = updated_menu
            return {"Item updated": updated_menu}
    raise HTTPException(status_code=404, detail="Item not found in menu")


# -------------------- Delete Menu Item --------------------
@app.delete("/hotel/delete/menu/{id}")
def delete_item(id: int):
    """
    Deletes an item from the menu by its ID.

    Sample Input: /hotel/delete/menu/4 (to delete item with id=4)

    Sample Output:
    {
        "item deleted": {
            "id": 4,
            "name": "Gulab Jamun",
            "category": "dessert",
            "price": 79.0,
            "is_available": False
        }
    }

    If item not found:
    {
        "detail": "ID not found error"
    }
    """
    for i in range(len(menu_items)):
        if menu_items[i]["id"] == id:
            del_item = menu_items.pop(i)
            return {"item deleted": del_item}
    raise HTTPException(status_code=404, detail="ID not found error")


# -------------------- Create Order --------------------
@app.post("/hotel/order_item")
def order_item(order: Order):
    """
    Creates a new order for a customer.

    Sample Input:
    {
        "id": 1,
        "order_type": "dine-in",
        "table_number": 5,
        "items": [
            {"menu_item_id": 1, "quantity": 2},
            {"menu_item_id": 3, "quantity": 3}
        ],
        "special_instructions": "No onions in the soup"
    }

    Sample Output:
    {
        "id": 1,
        "order_type": "dine-in",
        "table_number": 5,
        "items": [
            {"menu_item_id": 1, "quantity": 2},
            {"menu_item_id": 3, "quantity": 3}
        ],
        "value": "pending",
        "special_instructions": "No onions in the soup"
    }
    """
    global next_order_id
    next_order_id += 1
    orders.append({
        "id": order.id,
        "order_type": order.order_type,
        "table_number": order.table_number,
        "items": order.items,
        "value": order.value,
        "special_instructions": order.special_instructions
    })


# -------------------- Show All Orders --------------------
@app.get("/hotel/orders")
def show_orders():
    """
    Returns a list of all orders.

    Sample Output:
    {
        "orders": [
            {
                "id": 1,
                "order_type": "dine-in",
                "table_number": 5,
                "items": [
                    {"menu_item_id": 1, "quantity": 2},
                    {"menu_item_id": 3, "quantity": 3}
                ],
                "value": "pending",
                "special_instructions": "No onions in the soup"
            }
        ]
    }
    """
    return {"orders": orders}


# -------------------- Get Order By ID --------------------
@app.get("/hotel/order/id")
def get_order_by_id(id: int):
    """
    Fetches an order by its ID.

    Sample Input: /hotel/order/id?id=1

    Sample Output:
    {
        "Order fetched!": 1
    }

    If order not found:
    {
        "detail": "no order id found"
    }
    """
    for i in range(len(orders)):
        if orders[i]["id"] == id:
            return {"Order fetched!": orders[i]["id"]}
    raise HTTPException(status_code=404, detail="No order id found")


# -------------------- Update Order Status --------------------
@app.patch("/orders/{id}/status")
def upd_status(id: int, status: str):
    """
    Updates the status of an order.

    Sample Input:
    /orders/1/status?status=completed

    Sample Output:
    {
        "Order status updated": "completed"
    }
    """
    for i in range(len(orders)):
        if orders[i]["id"] == id:
            orders[i]["value"] = status
            return {"Order status updated": orders[i]["value"]}
    raise HTTPException(status_code=404, detail="Order not found")


# -------------------- Generate Bill --------------------
def find_price(m_id: int):
    """
    Finds the price of a menu item by its ID.

    Sample Output (for m_id=1):
    99.0
    """
    for data in menu_items:
        if data["id"] == m_id:
            return data["price"]

@app.get("/order/bill")
def get_bill(id: int):
    """
    Calculates the total bill amount for an order.

    Sample Input: /order/bill?id=1

    Sample Output:
    {
        "order_id": 1,
        "total bill amount": 1245.0
    }
    """
    amount = 0
    for order in orders:
        if order["id"] == id:
            for item in order["items"]:
                amount += find_price(item["menu_item_id"]) * item["quantity"]
    return {"order_id": id, "total bill amount": amount}
