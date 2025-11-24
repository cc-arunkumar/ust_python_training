from fastapi import FastAPI, Request
import time 

# Create FastAPI app with a title
app = FastAPI(title="Middleware Demo")

# Middleware to log requests and measure processing time
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Print incoming request method and path
    print(f"Incoming request: {request.method} {request.url.path}")
    
    # Record start time
    start_time = time.perf_counter()
    
    # Process the request and get response
    response = await call_next(request)
    
    # Calculate how long it took
    processing_time = time.perf_counter() - start_time
    
    # Print response status and processing time
    print(f"Response status: {response.status_code} -- Processing time: {processing_time}")
    
    # Return the response back to client
    return response

# Simple GET endpoint
@app.get("/hello")
async def say_hello():
    # Return JSON response
    return {"message": "Hello from FastAPI"}

# sample execution 
# sample output:
# GET/docs completed in 0.0006 seconds
# INFO:     127.0.0.1:60564 - "GET /docs HTTP/1.1" 200 OK
# GET/openapi.json completed in 0.0015 seconds
# INFO:     127.0.0.1:60564 - "GET /openapi.json HTTP/1.1" 200 OK
# GET/hello completed in 0.0004 seconds
# INFO:     127.0.0.1:60568 - "GET /hello HTTP/1.1" 200 OK