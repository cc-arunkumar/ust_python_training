from app.database.mysql_connection import get_connection
from app.schemas.schemas import UserSchema
from app.models.models import UserReqRes
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException


def _ensure_roles_list(roles):
    if roles is None:
        return []
    if isinstance(roles, list):
        # Normalize each entry:
        # - If it's an Enum (has .value), use the value (e.g., UserRole.DEVELOPER -> "Developer").
        # - If it's a string that looks like 'UserRole.DEVELOPER' or 'userrole.DEVELOPER', extract the final part.
        # - Normalize casing to the canonical capitalized forms expected by Pydantic/logic.
        normalized = []
        for r in roles:
            # Enum member: take its .value
            if hasattr(r, "value"):
                val = r.value
            else:
                val = str(r)

            # If stored as 'UserRole.DEVELOPER' or similar, extract suffix
            if "." in val:
                val = val.split(".")[-1]

            # Normalize common casings to canonical values
            lc = val.strip().lower()
            if lc == "admin":
                normalized.append("Admin")
            elif lc == "manager":
                normalized.append("Manager")
            elif lc in ("developer", "dev", "developerrole"):
                normalized.append("Developer")
            else:
                # Fallback: capitalize first letter
                normalized.append(val.strip().capitalize())

        return normalized
    # roles may be a comma separated string from older data
    if isinstance(roles, str):
        return [r.strip() for r in roles.split(',') if r.strip()]
    # fallback
    return [str(roles)]


# def normalize_role_param(role_value):
#     """Normalize incoming role parameter (which may be a JSON string, comma list or single value)

#     Returns the first role as canonical string (title-cased), or empty string if none.
#     """
#     if role_value is None:
#         return ""
#     # If it's a list, take first
#     if isinstance(role_value, list) and len(role_value) > 0:
#         return str(role_value[0]).strip().strip('\"').strip("'").title()
#     # If it's already a string, try to reuse _ensure_roles_list logic
#     if isinstance(role_value, str):
#         lst = _ensure_roles_list(role_value)
#         if lst:
#             return lst[0]
#         return ""
#     # Other types
#     return str(role_value).strip().strip('\"').strip("'").title()


def add_user(new_user: UserReqRes):
    try:
        session = get_connection()
        user = UserSchema(
            e_id=new_user.e_id,
            password=new_user.password or "password123",
            roles=_ensure_roles_list(new_user.roles),
            status=new_user.status,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        res = UserReqRes(
            e_id=user.e_id,
            password=user.password,
            roles=_ensure_roles_list(user.roles),
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
                roles=_ensure_roles_list(u.roles),
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
        users = session.query(UserSchema).filter(UserSchema.roles.contains(role)).all()
        res = []
        for u in users:
            res.append(UserReqRes(
                e_id=u.e_id,
                password=u.password,
                roles=_ensure_roles_list(u.roles),
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
        return UserReqRes(e_id=u.e_id, password=u.password, roles=_ensure_roles_list(u.roles), status=u.status)
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
            # normalize to stored representation (JSON/list supported by SQLAlchemy JSON)
            updated["roles"] = _ensure_roles_list(updated["roles"]) if updated["roles"] is not None else u.role
        for key, value in updated.items():
            setattr(u, key, value)
        session.commit()
        session.refresh(u)
        return UserReqRes(e_id=u.e_id, password=u.password, roles=_ensure_roles_list(u.roles), status=u.status)
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


def add_role_to_user(e_id: int, role: str):
    """Ensure the user with e_id has the given role. Adds and persists if missing.

    Returns the updated UserReqRes.
    """
    try:
        session = get_connection()
        u = session.query(UserSchema).filter(UserSchema.e_id == e_id).first()
        if not u:
            raise HTTPException(status_code=404, detail="User Not Found")
        roles = _ensure_roles_list(u.roles)
        if role not in roles:
            roles.append(role)
            # persist the updated roles (SQLAlchemy will handle JSON/list columns)
            u.roles = roles
            session.commit()
            session.refresh(u)
        return UserReqRes(e_id=u.e_id, password=u.password, roles=_ensure_roles_list(u.roles), status=u.status)
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        session.close()


def normalize_role_param(role: str) -> str | None:
    """Normalize a role string to canonical form or return None for invalid.

    Examples: 'admin' -> 'Admin', 'MANAGER' -> 'Manager', 'dev' -> 'Developer'
    """
    if not role:
        return None
    r = str(role).strip().lower()
    if r == "admin":
        return "Admin"
    if r == "manager":
        return "Manager"
    if r in ("developer", "dev"):
        return "Developer"
    return None