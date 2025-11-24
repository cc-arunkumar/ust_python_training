from fastapi import FastAPI, Request
import time

# Initialize a FastAPI application with a custom title.
app = FastAPI(title="Middleware Demo")

# Define a middleware that will intercept every HTTP request.
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Log basic information about the incoming request.
    print(f"Incoming request : {request.method} {request.url.path}")
    
    # Capture the start time to measure processing duration.
    start_time = time.perf_counter()
    
    # Forward the request to the next middleware or endpoint handler.
    response = await call_next(request)
    
    # Calculate how long the request took to process.
    time_frame = time.perf_counter() - start_time
    
    # Log the response status and the processing time.
    print(f"Response status : {response.status_code} processing time {time_frame}")
    
    # Return the final response to the client.
    return response 

# Basic GET endpoint to return a welcome message.
@app.get("/hello")
async def say_hello():
    # Return a simple JSON response.
    return {"message" : "Hello welcome"}

# Sample output:
#
# Incoming request : GET /docs
# Response status : 200 processing time 0.0012888999999631778
# {
#   "message": "Hello welcome"
# }
