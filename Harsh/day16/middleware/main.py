from fastapi import FastAPI,Request
import time
app=FastAPI(title="MiddleWare")

@app.middleware("http")
async def log_request(request:Request,call_next):
    print(f"incoming request:{request.method}{request.url.path}")
    start_time=time.perf_counter()
    response=await call_next(request)
    process_time = time.perf_counter() - start_time
    print(f"Response status: {response.status_code}, Process time: {process_time:.4f} seconds")
    return response

@app.get("/home")
def hello():
    return{"message":"hello"}