from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from models import TrainingRequest, Token, LoginRequest, User
from datetime import timedelta
from crud import (
	read_all_requests,
	read_req_by_id,
	create_request,
	update_request,
	delete_request_by_id,
    patch_request,
    DEMO_PASSWORD,
    DEMO_USERNAME,
    create_access_token,
    get_curr_user
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI app instance for the Training Request Management System
app = FastAPI(title="Training Request Management System")


@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
 
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

@app.get('/requests/{request_id}', response_model=TrainingRequest)
# API endpoint to fetch a training request by ID
def get_request_id(request_id: int, User = Depends(get_curr_user)):
	try:
		data = read_req_by_id(request_id)
		if not data:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found")
		return data
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"ID not Found or Unable to fetch the Record : {e}")


@app.get('/requests/', response_model=List[TrainingRequest])
# API endpoint to fetch all training requests
def get_all_requests(User = Depends(get_curr_user)):
	try:
		data = read_all_requests()
		return data
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@app.post('/requests/', response_model=TrainingRequest)
# API endpoint to create a new training request
def create_request_endpoint(new_req: TrainingRequest, User = Depends(get_curr_user)):
	try:
		create_request(new_req)
		return new_req
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@app.put('/requests/', response_model=TrainingRequest)
# API endpoint to update an existing training request
def update_request_endpoint(req_id: int, updated_req: TrainingRequest, User = Depends(get_curr_user)):
	try:
		update_request(req_id, updated_req)
		return get_request_id(req_id)
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")

@app.patch('/requests/{request_id}')

def patch_endpoint(request_id : int,col:str,val:str, User = Depends(get_curr_user)):
    try:
        patch_request(request_id,col,val)
        return {'details': 'Updated Successfully'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f'Error: {e}')

@app.delete('/requests/{request_id}')
# API endpoint to delete a training request by ID
def delete_request_endpoint(request_id: int, User = Depends(get_curr_user)):
	try:
		delete_request_by_id(request_id)
		return {'details': 'Request Deleted Successfully!'}
	except Exception as e:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Error: {e}")


