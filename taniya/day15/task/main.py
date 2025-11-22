from typing import List
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app =FastAPI(title="SPICEHUB")

class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float
    is_availabe:bool="True"
    
class OrderItem(BaseModel):
    menu_item_id:int
    quantity:int
    
class Order(BaseModel): 
    id:int
    order_type:str
    table_number:int=None
    item:List[OrderItem]
    status:str="pending"
    special_instruction:str=None  
    
menu = [
    {"id": 1, "name": "Tomato Soup", "category": "starter", "price": 99.0, "is_available": True},
    {"id": 2, "name": "Paneer Butter Masala", "category": "main_course", "price": 249.0, "is_available": True},
    {"id": 3, "name": "Butter Naan", "category": "main_course", "price": 49.0, "is_available": True},
    {"id": 4, "name": "Gulab Jamun", "category": "dessert", "price": 79.0, "is_available": False},
]

orders = []
next_menu_id = 5
next_order_id = 1
    
@app.get("/menu",response_model=MenuItem)
def get_menu(only_avaialble:bool=False):
    if only_avaialble:
        available_items =[]
        for item in menu:
            if item["is_available"]:
                available_items.append(item)
        return available_items
    else:
        return menu
    
@app.get("/menu/{id}",response_model=MenuItem)
def get_menu_item(id:int):
    for item in menu:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404,detail="Menu item not found")
new_menu={}
@app.post("/menu",response_model=MenuItem)
def add_new_menu(item:MenuItem):
       new_item = {
        "id": next_menu_id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "is_available": item.is_available
    }
       menu.append(new_item)
       next_menu_id +=1
       return new_item

@app.put("/menu/{id}",response_model=MenuItem)
def update_menu_item(id:int,item:MenuItem):
    for m in menu:
        if m["id"] == id:
            m["name"] = item.name
            m["category"]=item.category
            m["price"] =item.price
            m["is_available"] =item.is_availabe
            return m
    raise HTTPException(status_code=404,detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id:int):
    for m in menu:
        if m["id"] == id:
            del menu[m]
            return {"detail":"Menu item deleted"}
    raise HTTPException(status_code=404,detail="Menu item not found")
