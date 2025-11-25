# from fastapi import FastAPI, Request

# app = FastAPI(title="Middleware demo")

# # Middleware that logs request method and URL path, and response status code
# @app.middleware("http")
# async def log_request(request: Request, call_next):
#     # Log incoming request details
#     print(f"Incomming Request: {request.method} {request.url.path}")
    
#     # Process the request
#     response = await call_next(request)
    
#     # Log the response status
#     print(f"Response Status: {response.status_code}")
    
#     return response

# # Sample route
# @app.get("/hello")
# async def say_hello():
#     return {"message": "Hello from FastAPI with middleware"}



import time
from fastapi import FastAPI, Request

app = FastAPI(title="Middleware time demo")

# Middleware that logs the time taken to process a request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Record the start time
    time_start = time.perf_counter()
    
    # Process the request
    response = await call_next(request)
    
    # Calculate the time taken for the request to process
    process_time = time.perf_counter() - time_start
    
    # Log the time taken
    print(f"{request.method} {request.url.path}  completed in {process_time:.4f} seconds")
    
    return response

# Sample route
@app.get("/hello")
async def get_msg():
    return {"message": "Hello from FastAPI with middleware"}
