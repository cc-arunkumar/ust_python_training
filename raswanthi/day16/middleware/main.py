import time
from fastapi import FastAPI, Request

# Create a FastAPI application instance with a custom title
app = FastAPI(title="Middleware Demo")

# Define a middleware function that runs for every HTTP request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Log the incoming request method (GET, POST, etc.) and path (/hello, etc.)
    print(f"Incoming request: {request.method} {request.url.path}") 
    
    # Step 1: Record the start time before processing the request
    start_time = time.perf_counter()
    
    # Step 2: Pass the request to the next handler (route or another middleware)
    response = await call_next(request)
    
    # Step 3: Calculate how long the request took to process
    process_time = time.perf_counter() - start_time
    
    # Log the time taken and the response status code (e.g., 200 OK)
    print(f"Time taken: {process_time:.4f}")
    print(f"Response status: {response.status_code}")
    
    # Optionally, add the processing time to the response headers
    # This can be useful for debugging or performance monitoring
    # response.headers["X-Process-Time"] = f"{process_time:.4f}"
    
    # Return the response back to the client
    return response 

# Define a simple GET endpoint at /hello
@app.get("/hello")
async def say_hello():
    # Return a JSON response
    return {"message": "Hello from FastAPI with middleware!"}
