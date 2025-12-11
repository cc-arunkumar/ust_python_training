# from typing import Optional
# from models import Task

# user_db = {
#     "rahul": {"username": "rahul", "password": "password123"}
# }

# task_list: list[Task] = []

# def next_id() -> int:
#     if len(task_list) == 0:
#         return 1
#     else:
#         last_task = task_list[-1]
#         return last_task.id + 1

# def find_task(task_id: int) -> Optional[int]:
#     for index in range(len(task_list)):
#         if task_list[index].id == task_id:
#             return index
#     return None