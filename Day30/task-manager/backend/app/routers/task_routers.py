# # app/routers/task_router.py

# from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
# from app.core.security import get_current_user  # Correct import from the role folder for authentication
# from app.services.task_file_service import upload_task_file  # Import the function for handling file upload
# from app.database import get_db  # Import to get the database session
# from sqlalchemy.orm import Session  # Import for SQLAlchemy session management

# # Create a new instance of APIRouter for task-related routes
# router = APIRouter()

# # Example of an admin-only route
# @router.get("/admin-only")
# def admin_only_route(current_user: dict = Depends(get_current_user)):
#     """
#     This route is accessible only by users with an 'admin' role.
#     It checks the user's role and denies access if the role is not 'admin'.
#     """
#     if current_user["role"] != "admin":
#         # If the user's role is not 'admin', access is denied (403 Forbidden)
#         raise HTTPException(status_code=403, detail="Access denied: Admin only")
    
#     # If the user is an admin, return the success message
#     return {"message": "This is an admin-only route"}

# # Example of a developer-only route
# @router.get("/developer-only")
# def developer_only_route(current_user: dict = Depends(get_current_user)):
#     """
#     This route is accessible only by users with a 'developer' role.
#     It checks the user's role and denies access if the role is not 'developer'.
#     """
#     if current_user["role"] != "developer":
#         # If the user's role is not 'developer', access is denied (403 Forbidden)
#         raise HTTPException(status_code=403, detail="Access denied: Developer only")
    
#     # If the user is a developer, return the success message
#     return {"message": "This is a developer-only route"}

# # Route for uploading a file, accessible only by 'admin' or 'developer' roles
# @router.post("/{task_id}/files")
# def upload_file(
#     task_id: int,
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db),  # Database session dependency
#     current_user: dict = Depends(get_current_user)  # Enforces JWT authentication and retrieves user info
# ):
#     """
#     This route allows 'admin' and 'developer' roles to upload files associated with a task.
#     It validates the user's role and ensures they are authorized to upload files.
#     """
#     # Check if user has a valid role to upload files (only 'admin' or 'developer' are allowed)
#     if current_user['role'] not in ['admin', 'developer']:
#         # If the user is not authorized, deny access (403 Forbidden)
#         raise HTTPException(status_code=403, detail="Access denied")
    
#     # If the user is authorized, proceed with the file upload logic
#     return upload_task_file(db, task_id, file)
