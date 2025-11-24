from fastapi import FastAPI,Request

app = FastAPI(title="Middleware")

# Middleware to log incoming requests and responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming Request:{request.method}{request.url.path}")  # Log incoming request method and path
    response = await call_next(request)  # Process the request and get the response
    print(f"Response status:{response.status_code}")  # Log the response status code
    
    return response  # Return the response

# Simple endpoint to say hello
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware!"}  # Return a simple message



# Output
# INFO:     127.0.0.1:57074 - "GET /docs HTTP/1.1" 200 OK
# Incoming Request:GET/openapi.json
# Response status:200






from fastapi import FastAPI, Request
import time

app = FastAPI(title="Middleware")

# Middleware to log request latency (time taken to process the request)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    
    start_time = time.perf_counter()  # Record the start time
    response = await call_next(request)  # Process the request and get the response
    process_time = time.perf_counter() - start_time  # Calculate the time taken for processing
    
    # Log the latency of the request 
    print(f"Latency of request type {request.method} of path {request.url.path} is {process_time:.4f}")
    
    return response  # Return the response

# Simple endpoint to say hello
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware!"}  # Return a simple message



#Sample output
# INFO:     127.0.0.1:57399 - "GET /openapi.json HTTP/1.1" 200 OK
# Latency of request type GET of path /hello is 0.0005
# INFO:     127.0.0.1:57400 - "GET /hello HTTP/1.1" 200 OK

