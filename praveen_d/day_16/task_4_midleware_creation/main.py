from fastapi import FastAPI, Request
from datetime import time

# Initialize the FastAPI app with a description
app = FastAPI(description="Middleware demo")

# Define the middleware function
@app.middleware("http")
async def log_request(request: Request, call_next):
    
    # Before the endpoint is processed, capture the start time.
    # `time.perf_counter()` provides a high-resolution timer to measure the elapsed time.
    in_time = time.perf_counter()

    # Call the next handler in the request-response cycle (the actual endpoint)
    # `await call_next(request)` processes the request and returns a response.
    response = await call_next(request)

    # After the endpoint is processed, calculate the time taken to process the request.
    process_time = time.perf_counter() - in_time  # Elapsed time in seconds

    # Log the response status and the time taken for processing.
    print(f"Response status: {response.status_code}")  # Print the status code of the response
    print(f"Time taken: {process_time} seconds")  # Print the time taken to process the request
    
    # Return the response to the client.
    return response

# Define a simple GET endpoint that returns a greeting message
@app.get("/hello")
async def greeting():

    return {"Greet": "Hi, welcome to the middleware"}
