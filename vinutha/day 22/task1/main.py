from fastapi import FastAPI, Depends
from models import Employee
import crud
from auth_jwt import auth_router, verify_token

app = FastAPI(title="UST TRAINING REQUEST MANAGEMENT")

# JWT router
app.include_router(auth_router, prefix="/auth")

@app.post("/api/v1/training-requests/", dependencies=[Depends(verify_token)])
def create_request(employee: Employee):
    return crud.create_training_request(employee)

@app.get("/api/v1/training-requests/", dependencies=[Depends(verify_token)])
def get_all_requests():
    return crud.get_all_training_requests()

@app.get("/api/v1/training-requests/{employee_id}", dependencies=[Depends(verify_token)])
def get_request(employee_id: str):
    return crud.get_training_request_by_id(employee_id)

@app.put("/api/v1/training-requests/{id}", dependencies=[Depends(verify_token)])
def update_request(id: int, employee: Employee):
    return crud.update_training_request(id, employee)

@app.delete("/api/v1/training-requests/{id}", dependencies=[Depends(verify_token)])
def delete_request(id: int):
    return crud.delete_training_request(id)
