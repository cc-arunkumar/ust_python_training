from fastapi import FastAPI, Request
app=FastAPI(title="Middleware dema")
@app.middleware("http")
async def log_request(request:Request, call_next):
    print(f"Incoming Request: {request.method} {request.url.path}")
    response=await call_next(request)
    print(f"Response status: {response.status_code}")
    # print(response.message)
    return response

@app.get("/hello")
async def say_hello():
    return {"message":"Hello from FastAPI with middleware!"}

# Output
# INFO:     127.0.0.1:57074 - "GET /docs HTTP/1.1" 200 OK
# Incoming Request:GET/openapi.json
# Response status:200