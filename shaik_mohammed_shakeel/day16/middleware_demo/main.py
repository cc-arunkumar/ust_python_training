# Import FastAPI framework and Request object
from fastapi import FastAPI, Request

# Create a FastAPI application instance with a custom title
app = FastAPI(title="Middleware Demo")

# Define a middleware function that will run for every HTTP request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the incoming request method (GET/POST/etc.) and path (URL endpoint)
    print(f"Incoming request: {request.method} {request.url.path}")
    
    # Pass the request to the next handler (route or another middleware)
    response = await call_next(request)
    
    # Log the response status code (e.g., 200 for success, 404 for not found)
    print(f"Response status: {response.status_code}")
    
    # Return the response back to the client
    return response

# Define a simple GET endpoint at /hello
@app.get("/hello")
async def say_hello():
    # Return a JSON response with a message
    return {"message": "Hello from FastAPI with Middleware"}


#Sample Output

# Incoming request:GET/docs
# Response status: 200
# INFO:     127.0.0.1:62660 - "GET /docs HTTP/1.1" 200 OK
# Incoming request:GET/openapi.json
# Response status: 200
# INFO:     127.0.0.1:62660 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request:GET/hello
# Response status: 200
# INFO:     127.0.0.1:62661 - "GET /hello HTTP/1.1" 200 OK

# Import the time module to measure request processing duration
import time

# Import FastAPI framework and Request object
from fastapi import FastAPI, Request

# Create a FastAPI application instance with a custom title
app = FastAPI(title="Middleware Time Demo")

# Define a middleware function that runs for every HTTP request
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Record the start time before processing the request
    start_time = time.perf_counter()
    
    # Pass the request to the next handler (route or another middleware)
    response = await call_next(request)
    
    # Calculate how long the request took to process
    process_time = time.perf_counter() - start_time
    
    # Print the HTTP method, path, and time taken in seconds
    print(f"{request.method} {request.url.path} completed in {process_time} Seconds")
    
    # Return the response back to the client
    return response

# Define a simple GET endpoint at /hello
@app.get("/hello")
async def get_msg():
    # Return a JSON response with a message
    return {"message": "Hello from FastAPI with Middleware"}

    
#Sample Output

# GET/docs completed in 0.0009667000003901194 Seconds
# INFO:     127.0.0.1:62682 - "GET /docs HTTP/1.1" 200 OK
# GET/openapi.json completed in 0.0013467999997374136 Seconds
# INFO:     127.0.0.1:62682 - "GET /openapi.json HTTP/1.1" 200 OK
# GET/hello completed in 0.0005093999998280196 Seconds
# INFO:     127.0.0.1:62683 - "GET /hello HTTP/1.1" 200 OK