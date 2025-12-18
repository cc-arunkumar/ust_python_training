from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from typing import List, Optional
from models.remark import RemarkReqRes
from utils.auth import get_current_user
from crud.remark_crud import add_remark, get_remarks_by_task, delete_remark_by_id, update_remark
from crud.users_crud import normalize_role_param

remark_router = APIRouter(prefix="/Remark", tags=["Remark"])


@remark_router.get("/getbytask", response_model=List[RemarkReqRes])
def list_for_task(task_id: int, role: str, user=Depends(get_current_user)):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")
        
    remarks = get_remarks_by_task(task_id)
    if not remarks:
        raise HTTPException(status_code=404, detail="No remarks found for task")
    return remarks


@remark_router.post("/create")
def create_remark(
    task_id: int = Form(...),
    comment: str = Form(...),
    file: Optional[UploadFile] = File(None),
    role: str = Form(...),
    user=Depends(get_current_user),
):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

    r = add_remark(task_id=task_id, comment=comment, e_id=getattr(user, "e_id", None), file=file, role=role_clean, user=user)
    return {"detail": "Remark Added Successfully", "remark": r}


@remark_router.put("/update")
def update_remark_api(
    remark_id: str = Form(...),
    comment: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    role: str = Form(...),
    user=Depends(get_current_user),
):
     
    role_clean = normalize_role_param(role)
    updated = update_remark(remark_id=remark_id, comment=comment, file=file, e_id=getattr(user, "e_id", None), role=role_clean)
    return {"detail": "Remark Updated Successfully", "remark": updated}


@remark_router.delete("/delete")
def delete_remark_by_id_api(id: str, role: str, user=Depends(get_current_user)):
    role_clean = normalize_role_param(role)
    if not role_clean or role_clean not in user.role:
        raise HTTPException(status_code=400,detail="you dont have the access of mentioned role")

    resp = delete_remark_by_id(id, role_clean, user)
    return resp
