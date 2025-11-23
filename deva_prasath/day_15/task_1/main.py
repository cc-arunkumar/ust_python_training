#  You are building a small REST API for a restaurant called “SpiceHubˮ.
#  The API will help restaurant staff to:
#   Manage the menu (add, view, update, delete dishes).
#   Take orders from customers (dine-in or takeaway).
#   Track order status (pending → in_progress → completed / cancelled).
#   Calculate total bill for an order.
#  Everything is stored in memory Python lists/dicts)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI(title="Hotel API")

# MenuItem model for defining menu items
class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float
    is_available:bool

# OrderItem model for defining items in an order
class OrderItem(BaseModel):
    menu_item_id:int
    quantity:int

# Sample menu data
menu=[
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False}
]

# Orders and ID tracking variables
orders=[]
next_menu_id=5
next_order_id=1


@app.get("/menu",response_model=List[MenuItem])
def get_menu(only_available:Optional[bool]=False):
    if only_available:
        available_items=[]
        for item in menu:
            if item["is_available"]:
                available_items.append(item)
        return available_items
    return menu

@app.get("/menu/{id}")
def get_menu_item(id:int):
    item=None
    for menu_it in menu:
        if menu_it["id"]==id:
            item=menu_it
            break
    if item is None:
        raise HTTPException(status_code=404,detail="Menu item not found")

    return item

@app.post("/menu")
def create_menu(item:MenuItem):
    global next_menu_id
    item_data={
        "id":next_menu_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available
    }
    menu.append(item_data)
    next_menu_id+=1
    
    return item_data

@app.put("/menu/{id}")
def update_menu(id:int,updated_item:MenuItem):
    for item in menu:
        if item['id']==id:
            item['name']=updated_item.name
            item['category']=updated_item.category
            item['price']=updated_item.price
            item['is_available']=updated_item.is_available
            return item
    raise HTTPException(status_code=404,detail="Menu item not available")
            


@app.delete("/menu/{id}")
def delete_menu(id:int):
    for item in menu:
        if item["id"] == id:
            menu.remove(item)                
            return {"detail": "Menu item deleted"}
    
    raise HTTPException(status_code=404, detail="Menu item not found")


# OrderCreate model to handle order creation data
class OrderCreate(BaseModel):
    id:int
    order_type:str
    table_number:Optional[int]=None
    items:List[OrderItem]
    status:str
    special_instructions:Optional[str]=None
    

@app.post("/orders")
def create_orders(order_data:OrderCreate):
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
        orders.append(new_order)
        next_order_id+=1
        return new_order

@app.get("/orders")
def get_all_orders(status:Optional[str]=None):
    if status is not None:
        filtered_orders=[]
        for order in orders:
            if order["status"]==status:
                filtered_orders.append(order)
        return filtered_orders
    return orders

@app.get("/orders/{id}")
def getidorder(id: int):
    for order in orders:
        if order['id']==id:
            return orders
    raise HTTPException(status_code=404,detail="Order not found")


# StatusUpdate model for updating order status
class StatusUpdate(BaseModel):
    status: str


@app.patch("/orders/{id}/status")
def update_order_status(id: int, payload: StatusUpdate):
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

    order["status"]=new_status
    return order

@app.get("/orders/{id}/total_amount")
def get_order_total(id:int):
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
        total+=menu_item["price"]*quantity   
    return{
        "order_id":id,
        "total_amount":round(total,2)
    }
