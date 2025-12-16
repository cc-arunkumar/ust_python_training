from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.sql import get_sql_db
from app.db.mongo import get_mongo_db
from app.services.employee_service import EmployeeService
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut
from app.core.dependencies import require_admin, AuthUser

router = APIRouter(prefix="/api/employees", tags=["employees"])

@router.get("/", response_model=list[EmployeeOut])
def list_employees(
    _: AuthUser = Depends(require_admin),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = EmployeeService(db_sql, db_mongo)
    return service.list()

@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee(
    emp_id: int,
    _: AuthUser = Depends(require_admin),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = EmployeeService(db_sql, db_mongo)
    emp = service.get(emp_id)
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return emp

@router.post("/", response_model=EmployeeOut)
def create_employee(
    body: EmployeeCreate,
    current_user: AuthUser = Depends(require_admin),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = EmployeeService(db_sql, db_mongo)
    return service.create(body.dict(), actor_id=current_user["sub"])

@router.put("/{emp_id}", response_model=EmployeeOut)
def update_employee(
    emp_id: int,
    body: EmployeeUpdate,
    current_user: AuthUser = Depends(require_admin),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = EmployeeService(db_sql, db_mongo)
    try:
        return service.update(emp_id, body.dict(), actor_id=current_user["sub"])
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{emp_id}")
def delete_employee(
    emp_id: int,
    current_user: AuthUser = Depends(require_admin),
    db_sql: Session = Depends(get_sql_db),
    db_mongo=Depends(get_mongo_db)
):
    service = EmployeeService(db_sql, db_mongo)
    ok = service.delete(emp_id, actor_id=current_user["sub"])
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return {"deleted": True}
