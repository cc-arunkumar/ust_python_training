# from fastapi import FastAPI,Request
# app=FastAPI(title="MiddleWare Demo")

# # 1.Custom middleware
# @app.middleware("http")
# async def log_requests(request:Request,call_next):
    
#     #Before endpoint
#     print(f"Incoming request:{request.method}{request.url.path}")
#     # call the next handler (could be another middleware or the endpoint)
#     response=await call_next(request)
#     #after endpoint
#     print(f"Response status:{response.status_code}")
#     return response
# #A simple endpoint
# @app.get("/hello")
# async def say_hello():
#     return {"message":"Hello from FastAPI with middleware!"}


#output
# Request URL
# http://127.0.0.1:8000/hello
# 200	
# Response body
# {
#   "message": "Hello from FastAPI with middleware!"
# }


import time
from fastapi import FastAPI,Request

app=FastAPI(title="Middleware Demo")

@app.middleware("http")
async def log_request(request:Request,call_next):
    start_time=time.perf_counter()
    
    response=await call_next(request)
    
    process_time=time.perf_counter()-start_time
    
    print(f"{request.method}{request.url.path} completed in {process_time:.4f} seconds")
    
    #optional
    response.headers["X-Process-Time"]=f"{process_time:.4f}"
    return response

@app.get("/hello")
async def say_hello():
    return {"message":"Hello from FastAPI with middleware!"}

# sample output:
# GET/docs completed in 0.0006 seconds
# INFO:     127.0.0.1:60564 - "GET /docs HTTP/1.1" 200 OK
# GET/openapi.json completed in 0.0015 seconds
# INFO:     127.0.0.1:60564 - "GET /openapi.json HTTP/1.1" 200 OK
# GET/hello completed in 0.0004 seconds
# INFO:     127.0.0.1:60568 - "GET /hello HTTP/1.1" 200 OK