from fastapi import FastAPI
from pydantic import  BaseModel
from typing import List
menuitems=[{
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
orders = []
next_menu_id = 5
next_order_id = 1
class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:float 
    is_available:bool=False
Menu: List[MenuItem]=[MenuItem(**e) for e in menuitems]
class OrderItem(BaseModel):
    menu_item_id:int 
    quantity:int
    
class Order(BaseModel):
    id:int
    order_type:str
    table_number:int|None 
    items:List[OrderItem]
    status: str="pending"
    special_instructions:str|None 
    
    
    
app=FastAPI(title="SpiceHub")

@app.get("/menu")
def get_all_menu_items():
    newlis=[]
    for k in Menu:
        if k.is_available==True:
            newlis.append(k)
    if len(newlis)==0:
        return Menu    
    return newlis


@app.get("/menu/{id}",response_model=MenuItem)

def get_item(id:int):
    for k in Menu:
        if k.id==id:
            return k
    return {"detail": "Menu item not found"}
    

@app.post("/menu",response_model=MenuItem)
def add_newmenu_item(menu:MenuItem):
    global next_menu_id
    menu.id=next_menu_id
    Menu.append(menu)
    next_menu_id+=1
    return menu

@app.put("/menu/{id}",response_model=MenuItem)

def update_menu(id:int,menu:MenuItem):
    for k in Menu:
        if k.id==id:
            k.name=menu.name 
            k.category=menu.category
            k.price=menu.price 
            k.is_available=menu.is_available
            return k
    return {"details":"Item dosnot exist"}

@app.delete("/menu/{id}",response_model=MenuItem)
def delete_item(id:int):
    for k in Menu:
        if k.id==id:
            Menu.pop(id-1)
            return {"detail":"Menu Item deleted"}
    return {"detail":"Menu Item not found"}

            