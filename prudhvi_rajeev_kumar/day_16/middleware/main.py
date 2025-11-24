from fastapi import FastAPI, Request
import time

app = FastAPI(title="Middleware demo.")
@app.middleware("http")
async def log_requests(request : Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    print(f"Response status  : {response.status_code}, Process time : {process_time, :.4f} seconds.")
    return response

@app.get("/hello")
def say_hello():
    return {"message" : "Hello from fast api with middleware."}
