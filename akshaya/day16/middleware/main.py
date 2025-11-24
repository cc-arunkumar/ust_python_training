# middleware
import time 
from fastapi import FastAPI, Request

# FastAPI app initialization
app = FastAPI(title="middleware demo")

# Middleware to log the details of incoming HTTP requests and measure processing time
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware to log incoming requests and calculate the time taken to process each request.
    This is useful for debugging and monitoring request performance.
    In production, logs should be directed to a logging system (e.g., Elasticsearch, or a file system) rather than just `print` statements.
    """

    # Start the timer to calculate request processing time
    start_time = time.perf_counter()

    # Log the incoming request method (e.g., GET, POST) and URL path
    print(f"Incoming request: {request.method} {request.url.path}")

    # Process the request and get the response
    response = await call_next(request)

    # Calculate the time taken to process the request
    process_time = time.perf_counter() - start_time

    # Log the processing time and response status code for monitoring purposes
    print(f"time taken is: {process_time:.4f} seconds")  # Time in seconds, precise to 4 decimal places
    print(f"Response status: {response.status_code}")  # Log the response status code (e.g., 200, 404)

    # Return the response to the client
    return response

# Example endpoint for the demo
@app.get("/hello")
async def say_hello():
    """
    A simple route that returns a hello message.
    In production, this could be replaced with a more complex route or API endpoint.
    """
    return {"message": "hello from FastAPI with middleware!"}



# sample output
# Incoming request: GET /openapi.json
# time taken is: 0.0036
# Response status :200