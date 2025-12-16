from fastapi import APIRouter, HTTPException
from crud.task_crud import add_task, get_all_tasks, get_task_by_id, update_task, delete_task
from models.task import TaskReqRes
from typing import List

task_router = APIRouter(prefix="/Task", tags=["Task"])


@task_router.get("/getall", response_model=List[TaskReqRes])
def get_all(role):
    try:
        tasks = get_all_tasks(role)
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found")
        return tasks
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.post("/create")
def add_new_task(new_task: TaskReqRes):
    try:
        t = add_task(new_task)
        return {"detail": "Task Added Successfully", "task": t}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.get("/get", response_model=TaskReqRes)
def get_by_id(id: int):
    try:
        t = get_task_by_id(id)
        return t
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.put("/update")
def update_task_data(id: int, new_data: dict):
    try:
        updated = update_task(id, new_data)
        return {"detail": "Task Updated Successfully", "task": updated}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@task_router.delete("/delete")
def delete_task_by_id(id: int):
    try:
        resp = delete_task(id)
        return resp
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
