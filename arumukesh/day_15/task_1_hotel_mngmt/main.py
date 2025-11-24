from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app=FastAPI(title="Hotel Management Console")
class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool
menu_items:List[MenuItem]=[
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
next_id=4


class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int 

    
    
class Order(BaseModel):
    id: int 
    order_type: str
    table_number: int
    items: List[OrderItem]
    value:str="pending"
    special_instructions: str
orders:List[Order]=[]
next_order_id=1

@app.get("/hotel")
def get_menu():
    return {"Menu":menu_items}

@app.get("/hotel/{id}")
def get_menu_by_id(id:int):
    for item in menu_items:
        if item["id"]==id:
            return {"Item details":item}
    raise HTTPException(status_code=404,detail="Menu item not found")


@app.post("/hotel/addmenu")
def add_menu(m_item:MenuItem):
    # for row in menu_items:
    #     if row["id"]==m_item["id"]:
    #         raise HTTPException(status_code=404,detail=" Conflict menu ID already exist")
    global next_id
    next_id+=1
    m_item.id=next_id
    menu_items.append(m_item)
    return m_item

# itom={
#  "id": 4,
#  "name": "Jamun",
#  "category": "dessert",
#  "price": 79.0,
#  "is_available": False
#  }

@app.put("/hotel/update_menu/{id}")
def update_menu(id:int,updated_menu:MenuItem):
    for data in menu_items:
        if data["id"]==id:
            data["id"]=updated_menu
            return {"Item updated":updated_menu}
        raise HTTPException(status_code=404,detail="item not found in menu")
    
@app.delete("/hotel/delete/menu/{id}")
def delete_item(id:int):
    for i in range(len(menu_items)):
       if menu_items[i]["id"]==id:
            del_item=menu_items.pop(i)
            return {"item deleted":del_item}
    raise HTTPException(status_code=404,detail="ID not found error")


@app.post("/hotel/order_item")
def order_item(order:Order):
    global next_order_id
    next_order_id+=1
    orders.append({"id":order.id,
    "order_type": order.order_type,
    "table_number":order.table_number,
    "items":order.items,
    "value":order.value,
    "special_instructions": order.special_instructions
    })
    

@app.get("/hotel/orders")
def show_orders():
    return{"orders":orders}

@app.get("/hotel/order/id")
def get_order_by_id(id:int):
    for i in range(len(orders)):
        if orders[i]["id"]==id:
            return {"Order fetched!":orders[i]["id"]}
    raise HTTPException(status_code=404,detail="no order id found")

@app.patch("/orders/{id}/status")
def upd_status(id:int,status:str):
    for i in range(len(orders)):
        if orders[i]["id"]==id:
            orders[i]["value"]=status
        return {"Order status updated":orders[i]["value"]}
def find_price(m_id:int):
    for data in menu_items:
        if data["id"]==m_id:
            price=data=["price"]
            return price
@app.get("/order/bill")
def get_bill(id:int):
    amount=0
    for order in range(len(orders)):
        if order["id"]==id:
            for item in order["items"]:
                amount+=find_price(item["menu_item_id"])*item["quantity"]
    # quantity: int 
    return {"order_id":id,"total bill amount":amount}


# print(add_menu(itom))
# print(update_menu(1,{"id":1,"name": "Butter Naan (Large)",
#  "category": "main_course",
#  "price": 69.0,
#  "is_available": True
# }))


# print(get_menu())
