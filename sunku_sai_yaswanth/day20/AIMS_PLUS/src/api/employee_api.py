from fastapi import FastAPI, HTTPException,status,APIRouter,Depends
from typing import List, Optional
from auth.auth_jwt_token import User, get_current_user
from models.employee_model import EmployeeDirectory
from config.db_connection import get_connection
from crud.employee_crud import get_all,get_by_id,insert_emp,update_emp_by_id,delete_emp,search_emp

# app=FastAPI()
employee_router=APIRouter(prefix="/employee")
@employee_router.get("/list", response_model=List[EmployeeDirectory])
def get_emp(status_filter:Optional[str]="",current_user: User = Depends(get_current_user)):
    try:
        rows = get_all(status_filter)
        emp_li=[]
        for row in rows:
            emp_li.append(EmployeeDirectory(**row))
        return emp_li
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"{e}")

@employee_router.get("/search")
def search_by_word(field_type:str,keyword : str,current_user: User = Depends(get_current_user)):
    try:
        data = search_emp(field_type,keyword)
        return data
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Unable to fetch data: {e}")


@employee_router.get("/count")
def count_data(current_user: User = Depends(get_current_user)):
    try:
        data = get_all()
        if data is None:
            raise HTTPException(status_code=404, detail="No employee found.")
        return {"count": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error counting employees: {str(e)}")
 
 

@employee_router.get("/{emp_id}", response_model=EmployeeDirectory)
def get_emp_by_id(emp_id: int,current_user: User = Depends(get_current_user)):
    try:
        rows=get_by_id(emp_id)
        if not rows:
            raise HTTPException(status_code=404,detail="Employee not exists")
        return EmployeeDirectory(**rows)
    except Exception as e:
        raise HTTPException(status_code=400,detail="ID not found")


@employee_router.post('/create',response_model=EmployeeDirectory)
def create_asset(new_emp : EmployeeDirectory,current_user: User = Depends(get_current_user)):
    try:
        insert_emp(new_emp)
        return new_emp
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: {e}")

@employee_router.put("/{emp_id}", response_model=EmployeeDirectory)
def update_details(emp_id: int, update_emp: EmployeeDirectory,current_user: User = Depends(get_current_user)):
    try:
        update_emp_by_id(emp_id, update_emp)
        return update_emp  
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Update failed: {str(e)}")


@employee_router.delete("/{id}")
def delete_asset_by_id(id: int,current_user: User = Depends(get_current_user)):
    try:
        
        if delete_emp(id):
            return {"detail":"employee deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting asset: {str(e)}")


@employee_router.patch("/{emp_id}/status")
def update_vendor_status(emp_id: int, status: str,current_user: User = Depends(get_current_user)):
    try:
        # Fetch the existing vendor by vendor_id
        data = get_by_id(emp_id)
        
        if not data:
            raise HTTPException(status_code=404, detail="Vendor not found")
        
        # Update the active_status field of the vendor
        data['active_status'] = status
        
        # Update the vendor record in the database
        update_emp_by_id(emp_id, EmployeeDirectory(**data))
        
        return {"message": "Vendor status updated successfully", "vendor_id": emp_id, "new_status": status}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating vendor status: {str(e)}")
