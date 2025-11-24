from fastapi import FastAPI,Request
import time
app = FastAPI(title="Middleware")

@app.middleware("http")
async def log_request(request:Request,call_next):

    start_time = time.perf_counter()

    print(f"Incoming Request : {request.method} {request.url.path}")

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    print(f"Time taken is : {process_time:.4f}")

    print(f"Response status : {response.status_code}")

    return response

@app.get("/hello")
async def say_hello():
    return {"message":"Hellooooooooo"}