# from fastapi import FastAPI,Request

# Fast api application
# app=FastAPI(title="Middle ware")

# Prints the incoming request and response
# @app.middleware("http")
# async def log_request(request:Request,call_next):
#     print(f"Incoming request : {request.method} {request.url.path}")
#     response=await call_next(request)
#     print(f"response status {response.status_code}")
#     return response

# The main api call
# @app.get("/hello")
# async def hello():
#     return {"Message":"Hello from shyam"}

#Sample output
# Incoming request : GET /openapi.json
# response status 200

# Incoming request : GET /hello
# response status 200


#importing the modules required
from fastapi import FastAPI,Request
import time

#fast api application
app=FastAPI(title="Middle ware")

#Middle ware to note the time taken for the process to complete
@app.middleware("http")
async def logging(request:Request,call_next):
    start=time.perf_counter()
    response=await call_next(request)
    process_time=time.perf_counter()-start
    print(f"The process took {process_time:.4f}")
    response.headers["X-Process-Time"] = str(process_time)
    return response

#the main api call
@app.get("/hello")
async def hello():
    return {"message":"Hello shyam"} 

# #Sample output
# The process took 0.0005
# INFO:     127.0.0.1:52060 - "GET /hello HTTP/1.1" 200 OK