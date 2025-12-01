from fastapi import APIRouter,HTTPException,Depends,status
from empl_model import EntityRequest
from dotenv import load_dotenv
import os
from empl_model import LoginRequest,User,Token
from datetime import timedelta
from auth import get_current_user,create_access_token
load_dotenv(os.path.join(os.path.dirname(__file__), "cred.env"))


from empl_crud import(
    create_rec,
    get_all,
    get_by_id,
    update_rec,
    update_patch,
    delete_rec
)


training_router=APIRouter(prefix="/api/v1/training-requests")



@training_router.post("/create")
def create_emp(ob:EntityRequest,current_user:dict=Depends(get_current_user)):
    try:
        create_rec(ob)
        return ob
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  

@training_router.get("/all")
def list_all(current_user:dict=Depends(get_current_user)):
    try:
        tr=get_all()
        return tr
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  


@training_router.get("/all/{id}")
def get_tr(id:int,current_user:dict=Depends(get_current_user)):
    try:
            tr=get_by_id(id)
            if not tr:
                raise HTTPException(status_code=404, detail="Detail not found")  
            return tr
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 

@training_router.put("/edit/{id}")
def put_id(id:int,ob:EntityRequest,current_user:dict=Depends(get_current_user)):
    try:
        update_rec(id,ob)
        return ob
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  
@training_router.patch("edit_name/{id}")
def patch_name(employee_name:str,id:int,current_user:dict=Depends(get_current_user)):
    try:
        update_patch(id,employee_name)
        return {"message": "Name updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    
@training_router.delete("delete/{id}")
def delete_tr(id:int,current_user:dict=Depends(get_current_user)):
    try:
        delete_rec(id)
        return {"message": "Deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))  