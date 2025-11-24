import time
from fastapi import FastAPI, Request

app = FastAPI(title="Middleware DEMO")

# ------------------------------------------------------
# MIDDLEWARE: Logs every request coming to the server
# ------------------------------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Logs incoming request & its path
    print(f"Incoming request: {request} | Path: {request.url.path}")

    # Start timer
    start_time = time.perf_counter()
    print(f"Start time: {start_time}")

    # Process the request
    response = await call_next(request)

    # End timer
    end_time = time.perf_counter()
    print(f"End time: {end_time}")

    # Time taken by request
    duration = end_time - start_time
    print(f"Time taken: {duration:.6f} seconds")

    # Log status code
    print(f"Response status: {response.status_code}")

    return response


# ------------------------------------------------------
# Sample Route
# ------------------------------------------------------
@app.get("/hello")
async def say_hello():
    return {"message": "hello from middleware!"}



# ===============OUTPUT================

# Incoming request: <starlette.requests.Request object at 0x7f12c0> | Path: /hello
# Start time: 3045.129501842
# End time: 3045.130982614
# Time taken: 0.001480 seconds
# Response status: 200


