from fastapi import FastAPI, Request

# Create a FastAPI application instance with a custom title
app = FastAPI(title="Middleware demo")

# Define a middleware that runs for every HTTP request
@app.middleware("http")
async def log_request(request: Request, call_next):
    # Log the incoming request method and path
    print(f"Incoming Request: {request.method} {request.url.path}")
    
    # Process the request and get the response from the next handler
    response = await call_next(request)
    
    # Log the response status code
    print(f"Response status: {response.status_code}")
    
    # Example: response.message does not exist, so it's commented out
    # print(response.message)
    
    # Return the response back to the client
    return response

# Define a simple GET endpoint at /hello
@app.get("/hello")
async def say_hello():
    # Return a JSON response with a greeting message
    return {"message": "Hello from FastAPI with middleware!"}



"""SAMPLE OUTPUT
{
  "message": "Hello from FastAPI with middleware!"
}
Incoming Request: GET /hello
Response status: 200
INFO:     127.0.0.1:59167 - "GET /hello HTTP/1.1" 200 OK



"""



# import time
# from fastapi import FastAPI,Request

# app=FastAPI(title="Middleware Demo")

# @app.middleware("http")
# async def log_requests(request:Request, call_next):
#     start_time=time.perf_counter()
    