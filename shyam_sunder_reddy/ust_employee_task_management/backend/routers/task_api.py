from fastapi import APIRouter, HTTPException, Depends
from crud.task_crud import add_task, get_all_tasks, get_task_by_id, update_task, delete_task, get_task_by_status, patch_status,patch_priority
from models.task import TaskReqRes
from typing import List
from utils.auth import get_current_user
from crud.users_crud import normalize_role_param
from datetime import datetime

task_router = APIRouter(prefix="/Task", tags=["Task"])


@task_router.get("/getall", response_model=List[TaskReqRes])
def get_all(role: str, user=Depends(get_current_user)):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean:
            raise HTTPException(status_code=400, detail="Invalid role parameter")
        if role_clean not in user.role:
            raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

        tasks = get_all_tasks(role_clean, user)
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found")
        return tasks
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.post("/create")
def add_new_task(role: str, new_task: TaskReqRes, user=Depends(get_current_user)):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        t = add_task(new_task, role_clean, user)
        return {"detail": "Task Added Successfully", "task": t}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.get("/get", response_model=TaskReqRes)
def get_by_id(id: int,role, user=Depends(get_current_user)):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean:
            raise HTTPException(status_code=400, detail="Invalid role parameter")
        if role_clean not in user.role:
            raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

        t = get_task_by_id(id, role_clean, user)  # FIXED: Pass user parameter
        return t
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.get("/getbystatus", response_model=List[TaskReqRes])
def get_by_status(status: str, role: str, user=Depends(get_current_user)):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        return get_task_by_status(status, role_clean, user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.put("/update")
def update_task_data(t_id: int,role: str,
    title: str = None,
    description: str = None,
    assigned_to: int = None,
    priority: str = None,
    status: str = None,
    reviewer: int = None,
    expected_closure: datetime = None, 
    user=Depends(get_current_user),
    ):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")

        # Disallow Developer role from making arbitrary updates to tasks
        if role_clean == "Developer":
            raise HTTPException(status_code=403, detail="Developers are not allowed to update tasks")
        
        # FIXED: Check if 'status' key exists before accessing it
        
        updated_task = update_task(
            t_id=t_id,
            title=title,
            description=description,
            assigned_to=assigned_to,
            priority=priority,
            status=status,
            reviewer=reviewer,
            expected_closure=expected_closure,
            role=role_clean,
            user=user
        )
        return {"detail": "Task Updated Successfully", "task": updated_task}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.patch("/patch")
def patch_stat(id: int, status: str, role: str, user=Depends(get_current_user)):
    try:
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")

        # Allow Manager and Admin to change status broadly.
        # Developers are allowed to change status for limited transitions (e.g. TO_DO->IN_PROGRESS and IN_PROGRESS->REVIEW)
        # The lower-level `patch_status` CRUD function enforces those transition rules and assignment checks.
        if role_clean not in ("Manager", "Admin", "Developer"):
            raise HTTPException(status_code=403, detail="Only Manager, Admin or Developer can change task status")

        patched = patch_status(id, status, role_clean, user)
        return {"detail": "Patched the task", "task": patched}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@task_router.patch("/tasks/{t_id}/priority")
async def update_task_priority(t_id: int, priority: str, role: str, user=Depends(get_current_user)):
    # Call patch_priority function to handle priority change
    try:
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

        return patch_priority(t_id=t_id, priority=priority, role=role_clean, user=user)
    except HTTPException as e:
        raise e

@task_router.delete("/delete")
def delete_task_by_id(id: int, role: str, user=Depends(get_current_user)):
    try:
        # FIXED: Simplified logic - only Admin can delete
        role_clean = normalize_role_param(role)
        if not role_clean or role_clean not in user.role:
            raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

        if role_clean.upper() != "ADMIN":
            raise HTTPException(status_code=403, detail="Only Admin can delete tasks")

        if "Admin" not in user.role:
            raise HTTPException(status_code=403, detail="User doesn't have Admin role")

        resp = delete_task(id, user)  # FIXED: Pass user parameter
        return resp
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")