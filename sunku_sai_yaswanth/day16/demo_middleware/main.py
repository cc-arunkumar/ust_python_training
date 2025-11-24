from fastapi import FastAPI, Request

# Initialize FastAPI application with a title
app = FastAPI(title="middleware demo")

# Middleware function to log incoming requests and their responses
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Log the incoming request method and URL path
    print(f"Incoming request {request.method} {request.url.path}")
    
    # Process the request and get the response
    response = await call_next(request)
    
    # Log the response status code
    print(f"Response status: {response.status_code}")
    
    # Return the response to the client
    return response

# Define an endpoint that returns a hello message
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware"}






# Import necessary modules for calculating the processing time of requests
import time
from fastapi import FastAPI, Request

# Initialize FastAPI application again (re-using for the second part)
app = FastAPI(title="middleware demo")

# Middleware function to log request processing time
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Record the start time of the request
    time_start = time.perf_counter()
    
    # Process the request and get the response
    response = await call_next(request)
    
    # Calculate the processing time of the request
    process_time = time.perf_counter() - time_start
    
    # Log the method, URL path, and processing time
    print(f"{request.method} {request.url.path} completed at {process_time}")
    
    # Return the response to the client
    return response

# Define the /hello endpoint again
@app.get("/hello")
async def say_hello():
    return {"message": "Hello from FastAPI with middleware"}


# Log information provided by Uvicorn server about incoming requests and responses
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [12032] using StatReload
# INFO:     Started server process [11888]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.   

# Sample logs showing request processing times:
# GET / completed at 0.001305300000012721
# INFO:     127.0.0.1:58967 - "GET / HTTP/1.1" 404 Not Found
# GET /favicon.ico completed at 0.0007309000000077504
# INFO:     127.0.0.1:58967 - "GET /favicon.ico HTTP/1.1" 404 Not Found
# GET /docs completed at 0.0012472000000229855
# INFO:     127.0.0.1:58968 - "GET /docs HTTP/1.1" 200 OK
# GET /openapi.json completed at 0.0016173999999864463
# INFO:     127.0.0.1:58968 - "GET /openapi.json HTTP/1.1" 200 OK
# GET /hello completed at 0.0006248999999911575
# INFO:     127.0.0.1:58969 - "GET /hello HTTP/1.1" 200 OK
