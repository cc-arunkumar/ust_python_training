from fastapi import FastAPI,Request
from datetime import datetime, time
import time
app=FastAPI(title="Middleware Demo")

# @app.middleware("http")
# async def log_Requests(request:Request,call_next):
#     print(f"Incoming request: {request.method} {request.url.path}")
#     response = await call_next(request)
#     print(f"Response status: {response.status_code}")
#     return response

# @app.get("/hello")
# async def say_hello():
#     return {"message":"Hello from FastAPI with middleware"}

@app.middleware("http")
async def log_request(request:Request,call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    process_time = (end_time - start_time)
    
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    print(f"process time : {process_time:.4f}")
    return response

@app.get("/hello")
async def hello():
    return {"message":"Hello from FastAPI with middleware"}
    