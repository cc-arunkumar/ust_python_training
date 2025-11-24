from fastapi import FastAPI, Request
import time 

# FastAPI application instance for the middleware demo
app = FastAPI(title="Middleware Demo")


@app.middleware('http')
async def log_requests(request: Request, call_next):

    # log incoming request method and path
    print(f"Incoming Request: {request.method} {request.url.path}")
    start_time = time.perf_counter()

    # call the next handler (endpoint or next middleware)
    response = await call_next(request)

    # compute elapsed time and log response status
    process_time = time.perf_counter() - start_time
    print(f"Response status: {response.status_code} and processed time: {process_time:.4f}")

    return response


@app.get('/hello')
async def say_hello():
    # simple health / demo endpoint used to exercise the middleware
    return {'message': "Hello from FastAPI with middleware"}
