from fastapi import APIRouter, HTTPException, Depends
from crud.task_crud import add_task, get_all_tasks, get_task_by_id, update_task, delete_task, get_task_by_status, patch_status
from models.task import TaskReqRes
from typing import List
from utils.auth import get_current_user

task_router = APIRouter(prefix="/Task", tags=["Task"])


@task_router.get("/getall", response_model=List[TaskReqRes])
def get_all(role: str, user=Depends(get_current_user)):
    try:
        tasks = get_all_tasks(role, user)
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
        if role not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        t = add_task(new_task, role, user)
        return {"detail": "Task Added Successfully", "task": t}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.get("/get", response_model=TaskReqRes)
def get_by_id(id: int, user=Depends(get_current_user)):
    try:
        t = get_task_by_id(id, user)  # FIXED: Pass user parameter
        return t
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.get("/getbystatus", response_model=List[TaskReqRes])
def get_by_status(status: str, role: str, user=Depends(get_current_user)):
    try:
        if role not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        return get_task_by_status(status, role, user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.put("/update")
def update_task_data(id: int, new_data: dict, role: str, user=Depends(get_current_user)):
    try:
        if role not in user.role:
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        
        # FIXED: Check if 'status' key exists before accessing it
        if role == "Admin" and new_data.get("status"):
            raise HTTPException(status_code=409, detail="Admin cannot update the status of task")
        
        updated = update_task(id, new_data, role, user)
        return {"detail": "Task Updated Successfully", "task": updated}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.patch("/patch")
def patch_stat(id: int, status: str, role: str, user=Depends(get_current_user)):
    try:
        # FIXED: Changed 'and' to 'or' for proper validation
        if role not in user.role or role.upper() == "ADMIN":
            raise HTTPException(status_code=409, detail="The user doesn't have the mentioned role")
        
        patched = patch_status(id, status, role, user)
        return {"detail": "Patched the task", "task": patched}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.delete("/delete")
def delete_task_by_id(id: int, role: str, user=Depends(get_current_user)):
    try:
        # FIXED: Simplified logic - only Admin can delete
        if role.upper() != "ADMIN":
            raise HTTPException(status_code=403, detail="Only Admin can delete tasks")
        
        if "Admin" not in user.role:
            raise HTTPException(status_code=403, detail="User doesn't have Admin role")
        
        resp = delete_task(id, user)  # FIXED: Pass user parameter
        return resp
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")