from typing import List
from models import Task

def get_next_task_id(tasks:List[dict])->int:
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1