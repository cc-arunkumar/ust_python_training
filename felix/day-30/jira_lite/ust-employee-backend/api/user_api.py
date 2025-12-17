from fastapi import APIRouter, HTTPException, Depends
from services.user_services import update_user_role, create_User, get_User_by_id
from models.user_model import UpdateRole, UserModel
from auth.jwt_auth import get_current_user

user_router = APIRouter()


@user_router.put("/users/{emp_id}/role", tags=["Users"])
def update_user_role_endpoint(
    emp_id: int, 
    role_update: UpdateRole,
    user: str = Depends(get_current_user)
):
    """Update user role - Admin only"""
    try:
        auth_emp_id = int(user)
        
        # Get the authenticated user's info
        auth_user = get_User_by_id(auth_emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")
        
        # Check if user has admin role
        roles = auth_user.role
        if "admin" not in roles:
            raise HTTPException(
                status_code=403, 
                detail="Forbidden: admin role required to update user roles"
            )
        
        # Update the role
        updated_user = update_user_role(emp_id, role_update.role)
        if updated_user is None:
            raise HTTPException(status_code=500, detail="User role update failed")
        
        return updated_user
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user role: {e}")


@user_router.post("/users", tags=["Users"])
def create_new_user(
    user_data: UserModel,
    user: str = Depends(get_current_user)
):
    """Create new user - Admin only"""
    try:
        auth_emp_id = int(user)
        
        # Get the authenticated user's info
        auth_user = get_User_by_id(auth_emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")
        
        # Check if user has admin role
        roles = auth_user.role
        if "admin" not in roles:
            raise HTTPException(
                status_code=403, 
                detail="Forbidden: admin role required to create users"
            )
        
        # Create the user
        new_user = create_User(user_data)
        if new_user is None:
            raise HTTPException(status_code=500, detail="User creation failed")
        
        return new_user
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {e}")


@user_router.get("/users/{emp_id}", tags=["Users"])
def get_user_by_id_endpoint(
    emp_id: int,
    user: str = Depends(get_current_user)
):
    """Get user by ID - Authenticated users can view user info"""
    try:
        auth_emp_id = int(user)
        
        # Users can view their own info or admins can view anyone's info
        auth_user = get_User_by_id(auth_emp_id)
        if not auth_user:
            raise HTTPException(status_code=401, detail="User not found")
        
        # Allow users to view their own info or admins to view any user
        is_admin = "admin" in auth_user.role
        if auth_emp_id != emp_id and not is_admin:
            raise HTTPException(
                status_code=403, 
                detail="Forbidden: You can only view your own user information"
            )
        
        # Get the requested user
        requested_user = get_User_by_id(emp_id)
        if requested_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return requested_user
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user: {e}")