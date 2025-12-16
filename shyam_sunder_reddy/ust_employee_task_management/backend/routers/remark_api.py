from fastapi import APIRouter, HTTPException
from crud.remark_crud import add_remark, get_remarks_for_task, delete_remark
from models.remark import RemarkReqRes
from typing import List

remark_router = APIRouter(prefix="/Remark", tags=["Remark"])


@remark_router.get("/getbytask", response_model=List[RemarkReqRes])
def list_for_task(task_id: int):
    try:
        remarks = get_remarks_for_task(task_id)
        if not remarks:
            raise HTTPException(status_code=404, detail="No remarks found for task")
        return remarks
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@remark_router.post("/create")
def create_remark(new_remark: RemarkReqRes):
    try:
        r = add_remark(new_remark)
        return {"detail": "Remark Added Successfully", "remark": r}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@remark_router.delete("/delete")
def delete_remark_by_id(id: str):
    try:
        resp = delete_remark(id)
        return resp
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
