from typing import List, Optional
from models import Task, TaskCreate, TaskUpdate

tasks: List[Task] = []
_next_task_id: int = 1


def create_task(task_in: TaskCreate) -> Task:
    global _next_task_id
    task = Task(
        id=_next_task_id,
        title=task_in.title,
        description=task_in.description,
        completed=False,
    )
    _next_task_id += 1
    tasks.append(task)
    return task


def get_all_tasks() -> List[Task]:
    return tasks


def get_task_by_id(task_id: int) -> Optional[Task]:
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, task_in: TaskUpdate) -> Optional[Task]:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(
                id=task_id,
                title=task_in.title,
                description=task_in.description,
                completed=task_in.completed,
            )
            tasks[index] = updated_task
            return updated_task
    return None


def delete_task(task_id: int) -> bool:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return True
    return False
