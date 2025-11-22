from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI(title="madhan CRUD(In-Memory)")

class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    is_available: bool

menu: List[MenuItem] = [
    MenuItem(id=1, name="Tomato Soup", category="starter", price=99.0, is_available=True),
    MenuItem(id=2, name="Paneer Butter Masala", category="main_course", price=249.0, is_available=True),
    MenuItem(id=3, name="Butter Naan", category="main_course", price=49.0, is_available=True),
    MenuItem(id=4, name="Gulab Jamun", category="dessert", price=79.0, is_available=False),
]

@app.get("/menu", response_model=List[MenuItem])
def get_menu(only_available: bool = False):
    if only_available:
        return [item for item in menu if item.is_available]
    return menu

next_menu_id = 5

class MenuItemCreate(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool

@app.get("/menu/{id}", response_model=MenuItem)
def get_menu_item(id: int):
    for item in menu:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.post("/menu", response_model=MenuItem, status_code=201)
def create_menu_item(item: MenuItemCreate):
    global next_menu_id
    new_item = MenuItem(id=next_menu_id, **item.dict())
    menu.append(new_item)
    next_menu_id += 1
    return new_item

@app.put("/menu/{id}", response_model=MenuItem)
def update_menu_item(id: int, updated: MenuItem):
    for index, existing in enumerate(menu):
        if existing.id == id:
            menu[index] = MenuItem(
                id=id,
                name=updated.name,
                category=updated.category,
                price=updated.price,
                is_available=updated.is_available,
            )
            return menu[index]
    raise HTTPException(status_code=404, detail="Menu item not found")

@app.delete("/menu/{id}")
def delete_menu_item(id: int):
    for index, existing in enumerate(menu):
        if existing.id == id:
            deleted = menu.pop(index)
            return {"deleted": deleted}
    raise HTTPException(status_code=404, detail="Menu item not found")
