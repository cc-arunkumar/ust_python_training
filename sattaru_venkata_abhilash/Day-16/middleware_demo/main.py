from fastapi import FastAPI, Request

app = FastAPI(title="Middleware Demo")

# 1. Custom middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # BEFORE endpoint
    print(f"Incoming request: {request.method} {request.url.path}")
    
    # Call the next handler (could be another middleware or the endpoint)
    response = await call_next(request)
    
    # AFTER endpoint
    print(f"Response status: {response.status_code}")
    
    return response

# 2. A simple endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware!"}


# sample output:
#     Incoming request: GET /docs
# Response status: 200
# INFO:     127.0.0.1:52540 - "GET /docs HTTP/1.1" 200 OK
# Incoming request: GET /openapi.json
# Response status: 200
# INFO:     127.0.0.1:52540 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request: GET /hello
# Response status: 200
# # INFO:     127.0.0.1:52541 - "GET /hello HTTP/1.1" 200 OK



# WITH TIMEE

from fastapi import FastAPI, Request
import time

app = FastAPI(title="Middleware Demo")

# 1. Custom middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Get the current time (before handling the request)
    start_time = time.time()
    
    # BEFORE endpoint
    print(f"Incoming request: {request.method} {request.url.path} at {start_time}")
    
    # Call the next handler (could be another middleware or the endpoint)
    response = await call_next(request)
    
    # AFTER endpoint
    end_time = time.time()
    print(f"Response status: {response.status_code} at {end_time}")
    
    # Log the time taken for processing the request
    processing_time = end_time - start_time
    print(f"Processing time: {processing_time:.4f} seconds")
    
    return response

# 2. A simple endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI!"}


# Sample output:
    
# Incoming request: GET /docs at 1763981000.4162698
# Response status: 200 at 1763981000.4176238
# Processing time: 0.0014 seconds
# INFO:     127.0.0.1:52569 - "GET /docs HTTP/1.1" 200 OK
# Incoming request: GET /openapi.json at 1763981000.4916594
# Response status: 200 at 1763981000.4934952
# Processing time: 0.0018 seconds
# INFO:     127.0.0.1:52569 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request: GET /hello at 1763981007.6950366
# Response status: 200 at 1763981007.6962023
# Processing time: 0.0012 seconds
# INFO:     127.0.0.1:52570 - "GET /hello HTTP/1.1" 200 OK