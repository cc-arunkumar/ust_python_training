from database.mongo_connection import tasks
from models.task_model import TaskCreate,Task,TaskRemarksUpdate,TaskUpdate,TaskStatusUpdate
from services.user_services import get_User_by_id
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
            reviewer=task.reviewer,
            assigned_at = task.assigned_at,
            updated_by = task.updated_by,
            updated_at = datetime.now(),
            notifications = {},
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
        all_tasks = tasks.find({"assigned_to":id})
        print(all_tasks)
        return all_tasks
    except Exception as e:
        raise Exception(e)

def get_all_tasks_by_manager(id:int):
    try:
        all_tasks = tasks.find({
    "$or": [
        {"reviewer": id},          # tasks sent to this manager by admin
        {"assigned_by": id}        # tasks this manager created directly
    ]
})
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
        print("Status update result:", result.raw_result)
        return result.modified_count
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}") 
    except Exception as e:
        raise Exception(e)

def update_task_remarks(id:int, task_id:str, remarks_update:TaskRemarksUpdate):
    try:
        updated_remark = {str(id): remarks_update.remarks}
        oid = ObjectId(task_id)
        
        # First, get the task to determine recipient
        task = tasks.find_one({"_id": oid})
        if not task:
            return 0
        
        # Ensure notifications field exists as an object and remarks as an array (not null)
        fields_to_init = {}
        if task.get('notifications') is None:
            fields_to_init['notifications'] = {}
        if task.get('remarks') is None:
            fields_to_init['remarks'] = []
        
        # Initialize null fields if needed
        if fields_to_init:
            tasks.update_one(
                {"_id": oid},
                {"$set": fields_to_init}
            )
        
        # Determine recipient based on sender role
        sender = get_User_by_id(id)
        recipient_id = None
        
        if sender:
            roles = getattr(sender, 'role', None)
            has_manager = False
            has_developer = False
            
            try:
                # roles might be a list (JSON) or a string
                if isinstance(roles, list):
                    has_manager = 'manager' in roles
                    has_developer = 'developer' in roles
                else:
                    # coerce to string and check
                    roles_str = str(roles or '').lower()
                    has_manager = 'manager' in roles_str
                    has_developer = 'developer' in roles_str
            except Exception:
                has_manager = False
                has_developer = False

            if has_manager:
                # notify the assigned developer (if any)
                recipient_id = task.get('assigned_to')
            elif has_developer:
                # notify the assigning manager (if any)
                recipient_id = task.get('assigned_by')
            else:
                # unknown role shape — no recipient
                recipient_id = None
        else:
            # no sender found in user service
            recipient_id = None

        # Build update operations
        update_ops = {"$push": {"remarks": updated_remark}}
        
        if recipient_id:
            # increment notifications for the recipient for this task
            update_ops.setdefault("$inc", {})[f"notifications.{recipient_id}"] = 1
        else:
            # for debugging: ensure we at least log that no recipient was found
            print(f"No recipient to notify for remark by user {id} on task {task_id}")

        # Perform the update
        result = tasks.update_one(
            {"_id": oid},
            update_ops
        )
        return result.modified_count
    except (InvalidId, TypeError):
        raise ValueError(f"Invalid task_id: {task_id}")
    except Exception as e:
        raise Exception(e)