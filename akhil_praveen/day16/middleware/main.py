from fastapi import FastAPI,Request
import time

app = FastAPI(title="Middleware demo")

@app.middleware("http")
async def log_requests(request:Request,call_next):
    
    start_time = time.perf_counter()
    print(f"Incoming: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    process_time = time.perf_counter() - start_time
    
    print(f"time taken: {process_time:.4f}")
    
    print(f"Response status: {response.status_code}")
    
    return response

@app.get("/hello")
async def say_hello():
    return {"message": "Hello from Fastapi with middleware"}