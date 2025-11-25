next_task_id = 1

def generate_task_id() -> int:
    global next_task_id
    task_id = next_task_id
    next_task_id += 1
    return task_id
