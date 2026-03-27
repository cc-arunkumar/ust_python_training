from fastapi import FastAPI  # Import the FastAPI class for creating the API
from app.crud import router as training_request_router  # Import the router for training requests from the crud module
from app.auth import router as auth_router  # Import the router for authentication from the auth module

# Create a FastAPI application instance
app = FastAPI(title="UST Employee Training Request Management API")  # Set the title for the API

# Include the routes from the 'crud' module for managing training requests
# The 'training_request_router' handles all routes related to training requests
app.include_router(training_request_router, prefix="/api/v1/training-requests", tags=["Training Requests"])

# Include the routes from the 'auth' module for authentication
# The 'auth_router' handles all routes related to authentication, such as login and signup
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# The 'tags' argument helps categorize the authentication routes in the generated documentation

#output

# POST/auth/login/Login
	
# Response body

# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyb290IiwiZXhwIjoxNzY0NjExNTc3fQ.8l7smtoRQY1SyR7D3iB43glIvhJk3Qa_8zlJmE2Vdss",
#   "token_type": "bearer"
# }

# GET /api/v1/training-requests/


#   {
#     "id": 1,
#     "employee_id": "UST123",
#     "employee_name": "Bhargavi",
#     "training_title": "Python Basics",
#     "training_description": "Learn the basics of Python programming.",
#     "requested_date": "2025-12-01",
#     "status": "PENDING",
#     "manager_id": "UST456"
#   },
#   {
#     "id": 2,
#     "employee_id": "UST124",
#     "employee_name": "Meena",
#     "training_title": "Data Science",
#     "training_description": "Introduction to Data Science and machine learning.",
#     "requested_date": "2025-12-02",
#     "status": "APPROVED",
#     "manager_id": "UST457"
#   }

