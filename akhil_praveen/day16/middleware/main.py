from fastapi import FastAPI, Request
import time

app = FastAPI(title="Middleware demo")

# Middleware to log requests and response time
@app.middleware("http")
async def log_requests(request: Request, call_next):
    
    start_time = time.perf_counter()
    print(f"Incoming: {request.method} {request.url.path}")
    
    # Process the request and get the response
    response = await call_next(request)
    
    # Calculate time taken for request processing
    process_time = time.perf_counter() - start_time
    
    # Log response status and time taken
    print(f"time taken: {process_time:.4f}")
    print(f"Response status: {response.status_code}")
    
    return response

@app.get("/hello")
async def say_hello():
    return {"message": "Hello from Fastapi with middleware"}

# Sample Output

"""
Sample Output for /hello (GET):

Incoming: GET /hello
time taken: 0.0004
Response status: 200
Output:
{
    "message": "Hello from Fastapi with middleware"
}
"""
