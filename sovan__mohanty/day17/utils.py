

from typing import List, Optional
from models import Task

tasks: List[Task] = []
task_counter = 0
def find_task(task_id: int) -> Optional[Task]:
    for task in tasks:
        if task.id == task_id:
            return task
    return None
