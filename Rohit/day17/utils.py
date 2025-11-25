from fastapi import HTTPException

def find_task_by_id(tasks, id: int):
    for row in tasks:
        if row.id == id:
            return row
    raise HTTPException(status_code=404, detail="Task not found")
