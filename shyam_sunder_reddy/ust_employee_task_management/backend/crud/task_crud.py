from database.sql_db import get_connection
from schema.task_schema import TaskSchema
from models.task import TaskReqRes
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from datetime import datetime


def add_task(new_task: TaskReqRes,role,user):
	try:
		if role !="Manager" or role!="Admin":
			raise HTTPException(status_code=409,detail="Only Manager and Admin can create a new task")
		session = get_connection()
		task = TaskSchema(
			title=new_task.title,
			description=new_task.description,
			assigned_to=new_task.assigned_to,
			assigned_by=new_task.assigned_by,
			assigned_at=new_task.assigned_at,
			updated_by=new_task.updated_by,
			updated_at=new_task.updated_at,
			priority=new_task.priority,
			status="TO_DO",
			reviewer=new_task.reviewer,
			created_by=user.e_id,
			expected_closure=new_task.expected_closure,
			actual_closure=new_task.actual_closure
		)
		# set assigned_at if assigned_to is present but no assigned_at
		if task.assigned_to :
			task.assigned_at = datetime.now()

		session.add(task)
		session.commit()
		session.refresh(task)
		return TaskReqRes.from_orm(task)
	except SQLAlchemyError as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
	finally:
		session.close()


def get_all_tasks(role,user):
	try:
		session = get_connection()
		if role == "Manager":
			if "Manager" in user.role: 
				tasks = session.query(TaskSchema).filter(TaskSchema.reviewer == user.e_id).all()
			else:
				raise HTTPException(status_code=409,detail="Not Authorized")
		elif role=="Admin" :
			if "Admin" in user.role:
				tasks=session.query(TaskSchema).all()
			else:
				raise HTTPException(status_code=409,detail="Not Authorized")
		else:
			if role in user.role:
				tasks=session.query(TaskSchema).filter(TaskSchema.assigned_to==user.e_id).all()
			else:
				raise HTTPException(status_code=409,detail="Not Authorized")
		return [TaskReqRes.from_orm(t) for t in tasks]
	except SQLAlchemyError as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
	finally:
		session.close()


def get_task_by_id(t_id: int):
	try:
		session = get_connection()
		t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
		if not t:
			raise HTTPException(status_code=404, detail="Task Not Found")
		return TaskReqRes.from_orm(t)
	except SQLAlchemyError as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
	finally:
		session.close()


def update_task(t_id: int, updated: dict):
	try:
		session = get_connection()
		t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
		if not t:
			raise HTTPException(status_code=404, detail="Task Not Found")

		# handle assignment timestamp
		if "assigned_to" in updated and updated.get("assigned_to") and not t.assigned_at:
			t.assigned_at = datetime.utcnow()

		# handle status -> if changed to DONE set actual_closure
		if "status" in updated:
			new_status = updated.get("status")
			if new_status and new_status.upper() == "DONE":
				t.actual_closure = datetime.utcnow()

		for key, value in updated.items():
			setattr(t, key, value)

		t.updated_at = datetime.utcnow()
		session.commit()
		session.refresh(t)
		return TaskReqRes.from_orm(t)
	except SQLAlchemyError as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
	finally:
		session.close()


def delete_task(t_id: int):
	try:
		session = get_connection()
		t = session.query(TaskSchema).filter(TaskSchema.t_id == t_id).first()
		if not t:
			raise HTTPException(status_code=404, detail="Task Not Found")
		session.delete(t)
		session.commit()
		return {"detail": "Task Deleted Successfully"}
	except SQLAlchemyError as e:
		session.rollback()
		raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
	finally:
		session.close()

