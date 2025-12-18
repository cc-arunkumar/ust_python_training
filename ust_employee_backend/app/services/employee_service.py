from sqlalchemy.orm import Session
# package-relative imports
from models.employee import EmployeeDB
from schemas.employee import EmployeeCreate

def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = EmployeeDB(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session, skip: int = 0, limit: int | None = 10):
    """
    Return a paginated list of employees.

    Args:
        db: SQLAlchemy Session
        skip: number of records to skip (offset)
        limit: maximum number of records to return. If None, returns all after skip.

    Returns:
        list[EmployeeDB]
    """
    query = db.query(EmployeeDB).offset(skip)
    if limit is not None and limit > 0:
        query = query.limit(limit)
    return query.all()

def get_employee_by_id(db: Session, emp_id: int):
    return db.query(EmployeeDB).filter(EmployeeDB.emp_id == emp_id).first()

def update_employee(db: Session, emp_id: int, employee: EmployeeCreate):
    db_employee = get_employee_by_id(db, emp_id)
    if not db_employee:
        return None

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = get_employee_by_id(db, emp_id)
    if not db_employee:
        return False

    db.delete(db_employee)
    db.commit()
    return True
