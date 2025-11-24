# from fastapi import FastAPI,Request
# app=FastAPI(title="Middleware")
# @app.middleware("http")
# async def log_requests(request:Request,call_next):
#     print(f"Incoming request: {request.method} {request.url.path}")
#     response=await call_next(request)
#     print(f"Response status:{response.status_code}")
#     return response
# @app.get("/hello")
# async def say_hello():
#     return {"message":"hello from FastAPI with middleware"}

import time
from fastapi import FastAPI,Request
app=FastAPI(title="Middleware Demo")
@app.middleware("http")
async def log_requests(request:Request,call_next):
    start_time=time.perf_counter()
    response=await call_next(request)
    process_time=time.perf_counter()-start_time
    print(f"Response status:{response.status_code} and processed time:{process_time:.4f}")
    return response
@app.get("/hello")
async def say_hello():
    return {"message":"hello from FastAPI with middleware"}
    