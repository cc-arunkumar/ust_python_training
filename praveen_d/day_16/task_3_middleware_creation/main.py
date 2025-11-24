from fastapi import FastAPI,Request

app= FastAPI(description="Middleware demo")

@app.middleware("http")
async def log_request(request:Request,call_next):
    # Before endpoint
    print(f"Incoming request:{request.method} {request.url.path}")
    # call the next handeler
    response=await call_next(request)
    # AFTER endpoint
    print(f"Response status:{response.status_code}")
    return response

# Api created to test
@app.get("/hello")
async def greeting():
    return{"Greet":"Hi welome to the middleware"}