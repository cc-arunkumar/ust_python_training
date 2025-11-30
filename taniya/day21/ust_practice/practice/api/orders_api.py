from fastapi import FastAPI,HTTPException,APIRouter
from practice.crud.order_crud import (
    create_orders,
    get_all_orders,
    get_orders_by_id,
    update_orders,
    delete_orders)
from practice.models.order_models import Orders
 

order_router = APIRouter(prefix="/orders")

@order_router.post("/create")
def add_orders(order: Orders):
    try:
        result = create_orders(order)
        return result   
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

    
@order_router.get("")
def get_orders():
    try:
        return get_all_orders()
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@order_router.get("/{id}")
def get_order_id(id:int):
    try:
        return get_orders_by_id(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")  
    
@order_router.put("/update/{id}")
def update_order(id:int,order:Orders):
    try:
        return update_orders(id,order)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
@order_router.delete("/{id}")
def delete_order(id:int):
    try:
        return delete_orders(id)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")