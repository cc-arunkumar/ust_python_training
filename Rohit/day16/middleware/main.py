import time
from fastapi import FastAPI,HTTPException,Request



app = FastAPI()

# @app.middleware("http")
# async def log_request(request:Request,call_next):
#     print(f"Incoming request : {request.method} {request.url.path}")
    
#     response = await call_next(request)
    
#     print(f"Response status: {response.status_code}")
#     return response
# app.get("/hello")
# async def say_hello():
#     return {"message": "Hello from fastapi with middleware"}
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()   # record start
    response = await call_next(request)  # call the actual API
    end_time = time.perf_counter()     # record end
    process_time = end_time - start_time
    # Add custom header with elapsed time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    print(f"{process_time:.4f}")
    return response

# Example endpoint
@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
    

