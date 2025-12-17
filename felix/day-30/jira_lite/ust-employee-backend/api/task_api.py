from fastapi import APIRouter, HTTPException, Depends
from models.task_model import TaskUpdate, TaskCreate, TaskRemarksUpdate, TaskStatusUpdate
from services.task_services import (
    create_task, get_all_tasks_by_employee, get_all_tasks_by_manager,
    update_task, update_task_remarks, update_task_status,
    get_all_tasks, get_tasks_by_id
)
from auth.jwt_auth import get_current_user
from services.user_services import get_User_by_id  

task_router = APIRouter()

@task_router.get("/tasks", tags=["Tasks"])
def get_all_tasks_endpoint(user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "admin" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: admin role required to view all tasks")

        all_tasks = get_all_tasks()
        tasks_list = []
        for task in all_tasks:
            task['_id'] = str(task['_id'])
            tasks_list.append(task)
        return tasks_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.get("/tasks/{task_id}", tags=["Tasks"])
def get_task_by_id(task_id: str, user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if not any(r in roles for r in ["admin", "manager", "developer"]):
            raise HTTPException(status_code=403, detail="Forbidden: role required to view task")

        task = get_tasks_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task['_id'] = str(task['_id'])
        return task
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.post("/create_tasks", tags=["Tasks"])
def create_new_task(task: TaskCreate, user: str = Depends(get_current_user)):
    try:
        print("Creating new task",task)
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if not any(r in roles for r in ["admin", "manager"]):
            raise HTTPException(status_code=403, detail="Forbidden: admin or manager role required to create tasks")

        task_id = create_task(task)
        if not task_id:
            raise HTTPException(status_code=500, detail="Failed to create task")
        return {"id": task_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.get("/tasks/employee", tags=["Tasks"])
def get_tasks_of_employee(id: int, user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "developer" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: developer role required to view employee tasks")

        all_tasks = get_all_tasks_by_employee(emp_id)
        tasks_list = []
        for task in all_tasks:
            task['_id'] = str(task['_id'])
            tasks_list.append(task)
        return tasks_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.get("/tasks/manager", tags=["Tasks"])
def get_tasks_of_manager( user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if "manager" not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: manager role required to view manager tasks")

        all_tasks = get_all_tasks_by_manager(emp_id)
        tasks_list = []
        for task in all_tasks:
            task['_id'] = str(task['_id'])
            tasks_list.append(task)
        return tasks_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.put("/update_one_tasks/{task_id}", tags=["Tasks"])
def update_one_task(task_id: str, task_update: TaskUpdate, user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if not any(r in roles for r in ["admin", "manager"]):
            raise HTTPException(status_code=403, detail="Forbidden: admin or manager role required to update tasks")

        updated_fields = task_update.__dict__
        modified_count = update_task(task_id, updated_fields)
        if modified_count == 0:
            raise HTTPException(status_code=404, detail="Task not found or no changes made")
        return {"modified_count": modified_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.patch("/tasks/{task_id}/status", tags=["Tasks"])
def update_task_status_only(task_id: str, status_update: TaskStatusUpdate, user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if not any(r in roles for r in ["manager", "developer"]):
            raise HTTPException(status_code=403, detail="Forbidden: manager or developer role required to update task status")

        modified_count = update_task_status(task_id, status_update)
        if modified_count == 0:
            raise HTTPException(status_code=404, detail="Task not found or no changes made")
        return {"modified_count": modified_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@task_router.patch("/tasks/{id}/{task_id}/remarks", tags=["Tasks"])
def update_task_remarks_only(task_id: str, remarks_update: TaskRemarksUpdate, user: str = Depends(get_current_user)):
    try:
        emp_id = int(user)
        auth_user = get_User_by_id(emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")

        roles = auth_user.role
        print("Roles of auth user:", roles)
        if not any(r in roles for r in ["manager", "developer"]):
            raise HTTPException(status_code=403, detail="Forbidden: manager or developer role required to update task remarks")

        modified_count = update_task_remarks(emp_id, task_id, remarks_update)
        if modified_count == 0:
            raise HTTPException(status_code=404, detail="Task not found or no changes made")
        return {"modified_count": modified_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))