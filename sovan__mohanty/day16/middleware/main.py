#Middleware Demo
from fastapi import FastAPI, Request
import time

# Create FastAPI app
app = FastAPI(title="Middleware demo")

# Middleware to log request and response details
@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.perf_counter()  # Start timer
    print(f"Incoming request: {request.method} {request.url.path}")  # Log request
    response = await call_next(request)  # Process request
    process_time = time.perf_counter() - start_time  # Calculate time taken
    print(f"Response status: {response.status_code} {process_time}")  # Log response
    return response  # Return response

# Simple GET endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware"}

#Sample Execution
# Incoming request: GET /hello
# Response status: 200 0.000123456

# {
#   "message": "Hello from FastAPI with middleware"
# }
