from fastapi import FastAPI  # Import the FastAPI class for creating the API
from ust_training_requests.crud import router as training_request_router  # Import the router for training requests from the crud module
from ust_training_requests.auth import router as auth_router  # Import the router for authentication from the auth module

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



