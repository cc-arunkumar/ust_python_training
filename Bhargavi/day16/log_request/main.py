
# This FastAPI application demonstrates the use of middleware to log details of incoming requests and responses. The middleware captures the HTTP method, URL path, and calculates the time taken to process the request. 
# The /hello endpoint simply returns a JSON message, and the middleware logs the request information before and after the request is processed. This setup allows tracking of request processing times and response status codes for every API call.
from fastapi import FastAPI,Request
app = FastAPI(title = "Middleware Demo")

#1.customer middleware
@app.middleware("http")
async def log_requests(request:Request,call_next):
    
    #befor endpoint
    print(f"Incoming request : {request.method} {request.url.path}")
    #call the next handler
    response = await call_next(request)
    #after endpoint
    print(f"Response status : {response.status_code}")
    return response

#2.A simple endpoint
@app.get("/hello")
async def say_hello():
    return {"message" : "Hello from FastAPI with middleware!"}


from fastapi import FastAPI, Request
import time  # for measuring time

app = FastAPI(title="Middleware Demo")

# 1. Customer Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Before endpoint
    start_time = time.time()  # Record start time
    print(f"Incoming request: {request.method} {request.url.path}")
    # Call the next handler (process the request)
    response = await call_next(request)
    # After endpoint
    process_time = time.time() - start_time  # Calculate time taken
    print(f"Response status: {response.status_code}")
    print(f"Request processing time: {process_time:.4f} seconds")  # Log time taken

    return response

# 2. A Simple Endpoint
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware!"}


	
# Response body

# {
#   "message": "Hello from FastAPI with middleware!"
# }
# Incoming request: GET /hello
# Response status: 200
# Request processing time: 0.0014 seconds
# INFO:     127.0.0.1:59602 - "GET /hello HTTP/1.1" 200 OK