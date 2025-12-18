from sqlalchemy.orm import Session
from models.users import UserDB
from schemas.users import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = UserDB(
        emp_id=user.emp_id,
        password=user.password,  
        roles=user.roles,
        status=user.status
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Return a paginated list of users.

    Args:
        db: SQLAlchemy Session
        skip: number of records to skip (offset)
        limit: maximum number of records to return

    Returns:
        list[UserDB]
    """
    # Order by id to make pagination deterministic (avoid skipping items when DB returns arbitrary order)
    query = db.query(UserDB).order_by(UserDB.id).offset(skip)
    if limit is not None and limit > 0:
        query = query.limit(limit)
    return query.all()


def get_managers(db: Session, skip: int = 0, limit: int | None = None):
    """Return users which have a manager role (case-insensitive).

    This does a safe, conservative check in Python after fetching rows because
    JSON->SQL queries differ across DB backends. For small user counts this is
    fine; if you have many users consider implementing a DB-level JSON query.
    """
    # fetch all (or paginated) users and filter by roles in Python
    query = db.query(UserDB).order_by(UserDB.id).offset(skip)
    if limit is not None and limit > 0:
        query = query.limit(limit)

    users = query.all()
    managers = []
    for u in users:
        roles = u.roles or []
        # roles might be stored as a string or list; normalize to list of strings
        if not isinstance(roles, (list, tuple)):
            roles_list = [str(roles)]
        else:
            roles_list = [str(r) for r in roles]

        if any("manager" in r.lower() for r in roles_list):
            managers.append(u)

    return managers

def get_user_by_id(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()


def update_user(db: Session, user_id: int, data: UserUpdate):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        return None

    user.emp_id = data.emp_id
    user.password = data.password      # hash later
    user.roles = data.roles
    user.status = data.status

    db.commit()
    db.refresh(user)
    return user

VALID_STATUSES = {"ACTIVE", "INACTIVE","ON PROBATION"}

def patch_user(db: Session, user_id: int, status: str):
    if status not in VALID_STATUSES:
        raise ValueError("Invalid user status")

    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        return None

    user.status = status
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
