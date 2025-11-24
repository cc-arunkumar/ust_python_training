from fastapi import FastAPI,Request
import time

app = FastAPI(title="Middleware Demo")

@app.middleware("http")
async def log_request(request:Request,call_next):
    print(f"Incoming request : {request.method} {request.url.path}")
    start_time = time.perf_counter()
    response = await call_next(request)
    time_frame = time.perf_counter() - start_time
    print(f"Response status : {response.status_code} processing time {time_frame}")
    return response 

@app.get("/hello")
async def say_hello():
    return {"message" : "Hello welcome"}

# output

# Incoming request : GET /docs
# Response status : 200 processing time 0.0012888999999631778
# {
#   "message": "Hello welcome"
# }