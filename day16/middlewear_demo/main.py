from fastapi import FastAPI, Request  # Import FastAPI and Request classes
import time  # Import time module to track request processing time

app = FastAPI(title='Middleware Demo')  # Create FastAPI instance with a title

@app.middleware("http")  # Middleware that runs for each HTTP request
async def log_requests(request: Request, call_next):
    
# Middleware to log incoming requests and measure processing time.
    print(f"Incoming request {request.method} {request.url.path}")  # Log the HTTP method and request URL
    
    start_time = time.perf_counter()  # Start the timer to measure processing time
    
    response = await call_next(request)  # Process the request and get the response
    
    time_frame = time.perf_counter() - start_time  # Calculate the processing time
    print(f"Response status: {response.status_code} Processing time: {time_frame:.4f} seconds")  # Log the response status and time
    
    return response  # Return the response to the client

@app.get("/hello")  # Define an endpoint at /hello
async def say_hello():
    return {"message": "Hello from FastAPI with middleware"}  # Return a greeting message in JSON format



# Output

# Response status: 200 Processing time: 0.0013 seconds
# INFO:     127.0.0.1:57147 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request GET /docs

# Response status: 200 Processing time: 0.0004 seconds
# INFO:     127.0.0.1:57149 - "GET /docs HTTP/1.1" 200 OK
# Incoming request GET /openapi.json

# Response status: 200 Processing time: 0.0004 seconds
# INFO:     127.0.0.1:57149 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request GET /docs

# Response status: 200 Processing time: 0.0005 seconds
# INFO:     127.0.0.1:57150 - "GET /docs HTTP/1.1" 200 OK
# Incoming request GET /openapi.json

# Response status: 200 Processing time: 0.0003 seconds
# INFO:     127.0.0.1:57150 - "GET /openapi.json HTTP/1.1" 200 OK
