from database.sql_db import get_connection
from schema.user_schema import UserSchema
from models.user import UserReqRes
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def _roles_to_str(roles):
    if isinstance(roles, list):
        return ",".join(roles)
    return str(roles)


def _str_to_roles(s):
    if not s:
        return []
    return [r.strip() for r in s.split(",") if r.strip()]


def add_user(new_user: UserReqRes):
    try:
        session = get_connection()
        user = UserSchema(
            e_id=new_user.e_id,
            password=new_user.password or "defaultPass123",
            role=_roles_to_str(new_user.role),
            status=new_user.status
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        res = UserReqRes(
            e_id=user.e_id,
            password=user.password,
            role=_str_to_roles(user.role),
            status=user.status
        )
        return res
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()



def get_all_users():
    try:
        session = get_connection()
        users = session.query(UserSchema).all()
        res = []
        for u in users:
            res.append(UserReqRes(
                e_id=u.e_id,
                password=u.password,
                role=_str_to_roles(u.role),
                status=u.status
            ))
        return res
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_user_by_id(e_id: int):
    try:
        session = get_connection()
        u = session.query(UserSchema).filter(UserSchema.e_id == e_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="User Not Found")
        return UserReqRes(e_id=u.e_id, password=u.password, role=_str_to_roles(u.role), status=u.status)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def update_user(e_id: int, updated: dict):
    try:
        session = get_connection()
        u = session.query(UserSchema).filter(UserSchema.e_id == e_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="User Not Found")
        if "role" in updated:
            updated["role"] = _roles_to_str(updated["role"]) if updated["role"] is not None else u.role
        for key, value in updated.items():
            setattr(u, key, value)
        session.commit()
        session.refresh(u)
        return UserReqRes(e_id=u.e_id, password=u.password, role=_str_to_roles(u.role), status=u.status)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def delete_user(e_id: int):
    try:
        session = get_connection()
        u = session.query(UserSchema).filter(UserSchema.e_id == e_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="User Not Found")
        session.delete(u)
        session.commit()
        return {"detail": "User Deleted Successfully"}
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()
