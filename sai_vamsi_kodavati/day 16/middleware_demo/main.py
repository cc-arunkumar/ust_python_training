import time
from fastapi import FastAPI, Request

app = FastAPI(title="Middleware Demo")

@app.middleware("http")
async def log_requests(request:Request,call_next):
    
    # Before Endpoint
    print(f"Incoming request: {request.method} {request.url.path}")
    start_time = time.perf_counter()
    
    # call the next handler(could be another middleware or end point)
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    
    # Afetr endpoint
    print(f"{request.method} {request.url.path} Completed at {process_time}")
    return response
    

@app.get("/hello")
async def say_hello():
    return {"message":"Hello from FastAPI with middleware"}
    

# ---------------------------------------------------------------------------------------

# Sample Output

# INFO:     127.0.0.1:49255 - "GET /docs HTTP/1.1" 200 OK
# Incoming request: GET /openapi.json
# GET /openapi.json Completed at 0.001966600000002927
# INFO:     127.0.0.1:49255 - "GET /openapi.json HTTP/1.1" 200 OK
# Incoming request: GET /hello
# GET /hello Completed at 0.0018202999999630265
# INFO:     127.0.0.1:49258 - "GET /hello HTTP/1.1" 200 OK
