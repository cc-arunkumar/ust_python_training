from database.mongo_connection import tasks
from models.task_model import TaskCreate,Task,TaskRemarksUpdate,TaskUpdate,TaskStatusUpdate
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId

def create_task(task:TaskCreate):
    try:
        new_task = Task(
            title = task.title,
            description = task.description,
            assigned_to = task.assigned_to,
            assigned_by = task.assigned_by,
            assigned_at = task.assigned_at,
            updated_by = task.updated_by,
            updated_at = datetime.now(),
            priority = task.priority,
            status = task.status,
            remarks = task.remarks,
            expected_completion_date = task.expected_completion_date,
            actual_completion_date = task.actual_completion_date
        )
        result = tasks.insert_one(new_task.__dict__)
        return str(result.inserted_id)
    except Exception as e:
        raise Exception(e)
    
def get_all_tasks():
    try:
        all_tasks = tasks.find()
        return all_tasks
    except Exception as e:
        raise Exception(e)

def get_tasks_by_id(task_id:str):
    try:
        oid = ObjectId(task_id)
        task = tasks.find_one({"_id": oid})
        return task
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}")
    except Exception as e:
        raise Exception(e)

def get_all_tasks_by_employee(id:int):
    try:
        all_tasks = tasks.find({},{"assigned_to":id})
        print(all_tasks)
        return all_tasks
    except Exception as e:
        raise Exception(e)

def get_all_tasks_by_manager(id:int):
    try:
        all_tasks = tasks.find({},{"assigned_by":id})
        return all_tasks
    except Exception as e:
        raise Exception(e)
    
def update_task(task_id:str, updated_fields:dict):
    try:
        oid = ObjectId(task_id)
        result = tasks.update_one(
            {"_id": oid},
            {"$set": updated_fields}
        )
        return result.modified_count
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}")
    except Exception as e:
        raise Exception(e)
    
def update_task_status(task_id:str, status_update:TaskStatusUpdate):
    try:
        oid = ObjectId(task_id)
        result = tasks.update_one(
            {"_id": oid},
            {"$set": {"status": status_update.status}}
        )
        return result.modified_count
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}") 
    except Exception as e:
        raise Exception(e)

def update_task_remarks(id:int, task_id:str, remarks_update:TaskRemarksUpdate):
    try:
        updated_remark = {str(id): remarks_update.remarks}
        oid = ObjectId(task_id)
        result = tasks.update_one(
            {"_id": oid},
            {"$push": {"remarks": updated_remark}}
        )
        return result.modified_count
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}")
    except Exception as e:
        raise Exception(e)