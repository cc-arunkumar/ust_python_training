from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException, status, Query
from utils.employee_services import fetch_all_employees, fetch_employee_by_id
from pydantic import BaseModel
from typing import Optional
from database import employees
router = APIRouter(prefix="/employees")

# ---------------------- SEARCH ----------------------
@router.get("/search")
async def search_employees(search: str):
    query = {
        "$or": [
            {"Employee Name": {"$regex": search, "$options": "i"}},
            {"Designation": {"$regex": search, "$options": "i"}},
            {"Primary Technology": {"$regex": search, "$options": "i"}},
            {"Secondary Technology": {"$regex": search, "$options": "i"}},
        ]
    }

    employee_list = list(await employees().find(query))  # Await the query result
    for emp in employee_list:
        emp["_id"] = str(emp["_id"])

    return {"count": len(employee_list), "data": employee_list}

# ---------------------- FILTER ----------------------
class FilterModel(BaseModel):
    employee_type: Optional[str] = None
    skills: Optional[List[str]] = None
    domain: Optional[str] = None
    role: Optional[str] = None
    location: Optional[str] = None
    band: Optional[str] = None

@router.post("/filter")
async def filter_employees(filter: FilterModel):
    query = {}

    if filter.employee_type:
        query["Employment Type"] = filter.employee_type

    if filter.skills:
        query["$or"] = [
            {"Primary Technology": {"$in": filter.skills}},
            {"Secondary Technology": {"$in": filter.skills}},
        ]

    if filter.domain:
        query["Domain"] = filter.domain

    if filter.role:
        query["Designation"] = filter.role

    if filter.location:
        query["City"] = filter.location

    if filter.band:
        query["Band"] = filter.band

    employee_list = list(await employees().find(query))  # Await the query result
    for emp in employee_list:
        emp["_id"] = str(emp["_id"])

    return {"count": len(employee_list), "data": employee_list}

# ---------------------- SORT ----------------------
@router.get("/sort")
async def sort_employees(
    sort_by: str = Query("Employee Name"),
    order: str = Query("asc")
):
    sort_order = 1 if order == "asc" else -1

    employee_list = list(await employees().find().sort(sort_by, sort_order))  # Await the query result
    for emp in employee_list:
        emp["_id"] = str(emp["_id"])

    return {"count": len(employee_list), "data": employee_list}

# ---------------------- LIST ALL ----------------------
@router.get("/employees", response_model=List[Dict[str, Any]])
async def get_employees():
    try:
        employees_list = await fetch_all_employees()  # Await the async function
        return employees_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employees: {str(e)}")

# ---------------------- GET SINGLE EMPLOYEE ----------------------
@router.get("/{employee_id}", response_model=Dict[str, Any])
async def get_employee(employee_id: int):
    try:
        emp = await fetch_employee_by_id(employee_id)  # Await the async function
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employee: {str(e)}")
