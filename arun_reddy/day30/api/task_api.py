from fastapi import APIRouter
from Models.task_model import TaskCreate,TaskStatus,Remark
from crud.task_crud import insert_task,get_all_tasks,get_task_by_id,update_task,get_task_by_manager_id,delete_task_by_id,update_status,update_remarks_byid
from fastapi import APIRouter, Depends
from authorise.authorisation import role_guard
from Models.user_model import UserSchema

task_router=APIRouter(prefix="/tasks")

@task_router.post("",tags=["Tasks"],dependencies=[Depends(role_guard(["admin","manager"]))])
def create_task(task:TaskCreate):
    return insert_task(task)


@task_router.get("",tags=["Tasks"],dependencies=[Depends(role_guard(["admin","manager","developer"]))])
def read_all_tasks():
    return get_all_tasks()

@task_router.get("/{task_id}",tags=["Tasks"])
def read_task_by_id(task_id:str):
    return get_task_by_id(task_id)

@task_router.patch("/remark/{task_id}",tags=["Tasks"],dependencies=[Depends(role_guard(["manager","developer"]))])
def update_remarks(task_id:str,task:Remark):
    return update_remarks_byid(task_id,task)

@task_router.patch("/{task_id}",tags=["Tasks"],dependencies=[Depends(role_guard(["manager","developer"]))])
def update_status_by_id(task_id:str,task:TaskStatus):
    return update_status(task_id,task)



@task_router.put("/{task_id}",tags=["Tasks"],dependencies=[Depends(role_guard(["admin","manager"]))])
def update_task_by_id(task_id:str,task:TaskCreate):
    return update_task(task_id,task)

@task_router.get("/manager/{manager_id}",tags=["Tasks"],dependencies=[Depends(role_guard(["admin","manager"]))])
def read_tasks_by_manager_id(manager_id:int):
    return get_task_by_manager_id(manager_id)   


@task_router.delete("/{task_id}",tags=["Tasks"],dependencies=[Depends(role_guard(["admin","manager"]))])
def delete_task(id:str):
    return delete_task_by_id(id)

