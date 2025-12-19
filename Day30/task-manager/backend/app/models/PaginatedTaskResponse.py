from pydantic import BaseModel
from typing import List
from app.schemas.task import TaskResponse

class PaginatedTaskResponse(BaseModel):
    tasks: List[TaskResponse]
    total: int
    page: int
    limit: int
