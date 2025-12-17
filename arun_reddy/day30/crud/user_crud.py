from fastapi import HTTPException, status
from database.mysql_connection import SessionLocal, User

# Create a new user
def create_user(user: User):
    session = SessionLocal()
    try:
        new_user = User(
            emp_id=user.emp_id,
            role=user.role,
            status=user.status
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )
    finally:
        session.close()


# Get user by ID
def get_user_by_id(id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching user: {str(e)}"
        )
    finally:
        session.close()


# Get users by employee ID
def get_users_by_emp_id(emp_id: int):
    session = SessionLocal()
    try:
        users = session.query(User).filter(User.emp_id == emp_id).all()
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No users found for this employee"
            )
        return users

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching users: {str(e)}"
        )
    finally:
        session.close()


# Update user by ID
def update_user_by_id(id: int, user: User):
    session = SessionLocal()
    try:
        existing_user = session.query(User).filter(User.id == id).first()
        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Update fields
        existing_user.emp_id = user.emp_id
        existing_user.password = user.password
        existing_user.role = user.role
        existing_user.status = user.status

        session.commit()
        session.refresh(existing_user)
        return {"message": "Updated successfully"}

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating user: {str(e)}"
        )
    finally:
        session.close()


# Delete user by ID
def delete_user_by_id(id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        session.delete(user)
        session.commit()
        return {"message": "Deleted successfully"}

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting user: {str(e)}"
        )
    finally:
        session.close()
