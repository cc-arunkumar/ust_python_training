from fastapi import APIRouter, HTTPException, Depends
from models.emp_model import Employee
from services.employee_services import create_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee, get_all_employees_for_admin, get_emploee_by_id
from services.user_services import update_user_role, create_User, get_User_by_id
from models.user_model import UpdateRole,UserModel
from auth.jwt_auth import get_current_user

emp_router = APIRouter()

@emp_router.post("/employees",tags=["Employees"])
def create_new_employee(employee: Employee):
    try:
        # emp_id = int(user)
    
        # auth_user = get_User_by_id(emp_id)
        # if not auth_user:
        #     raise HTTPException(status_code=401, detail="User not found")

        # # role stored as comma-separated string; allow creation only for admins
        # roles = auth_user.role
        # print("Roles of auth user:", roles)
        # if "admin" not in roles:
        #     raise HTTPException(status_code=403, detail="Forbidden: admin role required to create employees")

        new_emp = create_employee(employee)
        if new_emp is None:
            raise HTTPException(status_code=500, detail="Employee creation failed")
        return new_emp
    except Exception as e:
        raise Exception(f"Error creating employee: {e}")
@emp_router.get("/employees/admin",tags=["Employees"])
def get_employees_for_admin(user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
    
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # role stored as comma-separated string; allow creation only for admins
        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "admin" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: admin role required to view all employees")

        return get_all_employees_for_admin()
    except Exception as e:
        raise Exception(f"Error fetching employees for admin: {e}")

@emp_router.get("/employees/{manager_id}",tags=["Employees"])
def get_employee(manager_id: int,user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
   
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # role stored as comma-separated string; allow creation only for admins
        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "manager" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: manager role required to view employees")

        return get_all_employees(manager_id)
    except Exception as e:
        raise Exception(f"Error fetching employees: {e}")

@emp_router.get("/employee_by_id/{emp_id}",tags=["Employees"])
def get_employee_by_id_endpoint(emp_id: int):
    try:
        return get_emploee_by_id(emp_id)
    except Exception as e:
        raise Exception(f"Error fetching employee by ID: {e}")

@emp_router.get("/employees/{manager_id}/{emp_id}",tags=["Employees"])
def get_one_employee(emp_id: int,manager_id: int,user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
    
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # role stored as comma-separated string; allow creation only for admins
        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "manager" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: manager role required to view employees")

        return get_employee_by_id(emp_id,manager_id)
    except Exception as e:
        raise Exception(f"Error fetching employee: {e}")


@emp_router.put("/employees/{manager_id}/{emp_id}",tags=["Employees"])
def update_existing_employee(emp_id: int, manager_id: int, updated_data: Employee,user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)

        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # role stored as comma-separated string; allow creation only for admins
        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "admin" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: admin role required to update employees")

        updated_emp = update_employee(emp_id, manager_id, updated_data)
        if updated_emp is None:
            raise HTTPException(status_code=500, detail="Employee update failed")
        return updated_emp
    except Exception as e:
        raise Exception(f"Error updating employee: {e}")


@emp_router.delete("/employees/{manager_id}/{emp_id}",tags=["Employees"])
def delete_existing_employee(emp_id: int, manager_id: int,user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
    
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        # role stored as comma-separated string; allow creation only for admins
        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "admin" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: admin role required to delete employees")

        result = delete_employee(emp_id, manager_id)
        if not result:
            raise HTTPException(status_code=500, detail="Employee deletion failed")
        return {"detail": "Employee deleted successfully"}
    except Exception as e:
        raise Exception(f"Error deleting employee: {e}")

# @emp_router.put("/users/{emp_id}/role",tags=["Users"])
# def update_user_role_endpoint(emp_id: int, role_update: UpdateRole):
#     updated_user = update_user_role(emp_id, role_update.role)
#     if updated_user is None:
#         raise HTTPException(status_code=500, detail="User role update failed")
#     return updated_user
# @emp_router.post("/users",tags=["Users"])
# def create_new_user(user_data: UserModel):
#     new_user = create_User(user_data)
#     if new_user is None:
#         raise HTTPException(status_code=500, detail="User creation failed")
#     return new_user