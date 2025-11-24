import time
from fastapi import FastAPI, Request

# Initialize FastAPI app
app = FastAPI(title="MiddleWare Demo")

# Middleware to log request processing time and status
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()   # start timer
    
    response = await call_next(request)  # process request
    
    process_time = time.perf_counter() - start_time  # calculate time
    
    # log response status and time taken
    print(f"Method: {request.method} Path: {request.url.path} "
          f"Status: {response.status_code} Time: {process_time:.4f}s")
    return response

# Simple GET endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello sohan"}
#Output

# GET /hello
# {
#   "message": "Hello sohan"
# }

# Console log example (printed by middleware):
# Method: GET Path: /hello Status: 200 Time: 0.0001s
