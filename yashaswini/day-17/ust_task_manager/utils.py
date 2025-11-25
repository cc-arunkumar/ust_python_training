# In-memory task storage
tasks = []
task_counter = 0

def get_next_id():
    """Auto-increment task ID"""
    global task_counter
    task_counter += 1
    return task_counter
