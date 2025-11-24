from fastapi import FastAPI,Request
app = FastAPI(title="Middleware Demo")

#1. Custom Middleware
@app.middleware("http")
async def log_requests(request:Request,call_next):
    
    #BFORE Endpoint
    print(f"Incomming request: {request.method} {request.url.path}")
    
    #call the next handler
    response = await call_next(request)
    
    #AFTER endpoint
    print(f"Response status: {response.status_code}")
    return response

#2. A simple endpoint
@app.get("/hello")
async def say_hello():
    return {"message":"Hello from FastAPI with Middleware!"}

#Sample Output
# Incomming request: GET /hello
# Response status: 200
# INFO:     127.0.0.1:50802 - "GET /hello HTTP/1.1" 200 OK






from fastapi import FastAPI,Request
import time
app = FastAPI(title="Middleware Demo")

#1. Custom Middleware
@app.middleware("http")
async def log_requests(request:Request,call_next):
    
    start_time = time.perf_counter()
    
    #BFORE Endpoint
    print(f"Incomming request:{start_time} {request.method} {request.url.path}")
    
    #call the next handler
    response = await call_next(request)
    
    end_time = time.perf_counter()
    
    #AFTER endpoint
    print(f"Time: {end_time-start_time: .4f} Response status: {response.status_code}")
    return response

#2. A simple endpoint
@app.get("/hello")
async def say_hello():
    return {"message":"Hello from FastAPI with Middleware!"}

#Sample Output
# Incomming request:9393.2094225 GET /hello
# Time:  0.0008 Response status: 200
# INFO:     127.0.0.1:50737 - "GET /hello HTTP/1.1" 200 OK