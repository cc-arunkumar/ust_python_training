from fastapi import APIRouter, HTTPException, Depends
from services.user_services import update_user_role, create_User, get_User_by_id,get_all_manager_for_admin,delete_User_account, get_all_Users, update_User
from models.user_model import UpdateRole, UserModel, UserUpdate
from auth.jwt_auth import get_current_user

user_router = APIRouter()

@user_router.get("/managers", tags=["Users"])
def get_all_managers_endpoint():
    """Get all managers - Admin only"""
    try:
        # Fetch all managers
        managers = get_all_manager_for_admin()
        if isinstance(managers, dict) and "detail" in managers:
            raise HTTPException(status_code=404, detail=managers["detail"])
        
        return managers
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching managers: {e}")
    
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
    
# Add these endpoints to your user_router in routes/user_routes.py

@user_router.get("/users", tags=["Users"])
def get_all_users_endpoint(user: str = Depends(get_current_user)):
    """Get all users - Admin only"""
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
                detail="Forbidden: admin role required to view all users"
            )
        
        # Get all users
        users = get_all_Users()
        if isinstance(users, dict) and "detail" in users:
            raise HTTPException(status_code=404, detail=users["detail"])
        
        return users
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching users: {e}")


@user_router.put("/users/{emp_id}", tags=["Users"])
def update_user_endpoint(
    emp_id: int, 
    user_update: UserUpdate,
    user: str = Depends(get_current_user)
):
    """Update user - Admin only"""
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
                detail="Forbidden: admin role required to update users"
            )
        
        # Update the user
        updated_user = update_User(emp_id, user_update)
        if updated_user is None:
            raise HTTPException(status_code=500, detail="User update failed")
        
        return updated_user
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user: {e}")


@user_router.delete("/users/{emp_id}", tags=["Users"])
def delete_user_endpoint(
    emp_id: int,
    user: str = Depends(get_current_user)
):
    """Delete user - Admin only"""
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
                detail="Forbidden: admin role required to delete users"
            )
        
        # Prevent self-deletion
        if auth_emp_id == emp_id:
            raise HTTPException(
                status_code=400, 
                detail="You cannot delete your own user account"
            )
        
        # Delete the user
        success = delete_User_account(emp_id)
        if not success:
            raise HTTPException(status_code=404, detail="User not found or deletion failed")
        
        return {"message": "User deleted successfully", "emp_id": emp_id}
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting user: {e}")