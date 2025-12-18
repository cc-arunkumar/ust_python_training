from database.sql_db import get_connection
from schema.user_schema import UserSchema
from models.user import UserReqRes
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import json


def _ensure_roles_list(roles):
    """Normalize various role representations into a clean list of role strings.

    Handles:
    - actual Python list -> returns list of str
    - JSON-encoded list strings: '["Developer","Manager"]'
    - comma separated strings: 'Developer,Manager'
    - single role string: 'Developer'
    """
    if roles is None:
        return []
    # Already a list
    if isinstance(roles, list):
        # Normalize each entry to a canonical form (e.g. 'Developer', 'Manager', 'Admin')
        return [str(r).strip().strip('\"').strip("'").title() for r in roles if r is not None]
    # If it's a string, try JSON parse first (handles ["A","B"]) then fallback to comma split
    if isinstance(roles, str):
        s = roles.strip()
        # Try JSON array
        try:
            parsed = json.loads(s)
            if isinstance(parsed, list):
                return [str(r).strip() for r in parsed if r is not None]
        except Exception:
            pass
    # Fallback: remove surrounding brackets if any and split by comma
    s_clean = s.strip('[]')
    parts = [p.strip().strip('\"').strip("'") for p in s_clean.split(',') if p.strip()]
    # Normalize casing
    return [p.title() for p in parts]
    # Fallback for other types
    return [str(roles).strip().strip('\"').strip("'").title()]


def normalize_role_param(role_value):
    """Normalize incoming role parameter (which may be a JSON string, comma list or single value)

    Returns the first role as canonical string (title-cased), or empty string if none.
    """
    if role_value is None:
        return ""
    # If it's a list, take first
    if isinstance(role_value, list) and len(role_value) > 0:
        return str(role_value[0]).strip().strip('\"').strip("'").title()
    # If it's already a string, try to reuse _ensure_roles_list logic
    if isinstance(role_value, str):
        lst = _ensure_roles_list(role_value)
        if lst:
            return lst[0]
        return ""
    # Other types
    return str(role_value).strip().strip('\"').strip("'").title()


def add_user(new_user: UserReqRes,role,user):
    try:
        session = get_connection()
        user = UserSchema(
            e_id=new_user.e_id,
            password=new_user.password or "password123",
            role=_ensure_roles_list(new_user.role),
            status=new_user.status,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        res = UserReqRes(
            e_id=user.e_id,
            password=user.password,
            role=_ensure_roles_list(user.role),
            status=user.status,
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
                role=_ensure_roles_list(u.role),
                status=u.status,
            ))
        return res
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def get_user_by_role(role: str):
    try:
        session = get_connection()
        users = session.query(UserSchema).filter(UserSchema.role.contains(role)).all()
        res = []
        for u in users:
            res.append(UserReqRes(
                e_id=u.e_id,
                password=u.password,
                role=_ensure_roles_list(u.role),
                status=u.status,
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
        return UserReqRes(e_id=u.e_id, password=u.password, role=_ensure_roles_list(u.role), status=u.status)
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
            # Normalize roles into JSON list for storage
            updated["role"] = _ensure_roles_list(updated["role"]) if updated["role"] is not None else u.role
        for key, value in updated.items():
            setattr(u, key, value)
        session.commit()
        session.refresh(u)
        return UserReqRes(e_id=u.e_id, password=u.password, role=_ensure_roles_list(u.role), status=u.status)
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
