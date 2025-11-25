# CRUD API Development
#  UST Employee Laptop Inventory 
#  UST maintains an internal inventory of company laptops assigned to employees.
#  The IT department needs a small internal API to:
#  Register laptops
#  View laptop details
#  Update laptop records
#  Remove laptops that are retired or disposed
#  All data will be stored in memory for this exercise.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="UST Employee Laptop Inventory")


class LaptopAsset(BaseModel):
    asset_id: int
    serial_number: str
    model_name: str
    purchase_year: int
    location: str = "Bengaluru"


laptops = []


@app.get("/laptops", response_model=list[LaptopAsset])
def get_all_laptops():
    return laptops

@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop(asset_id: int):
    for laptop in laptops:
        if laptop["asset_id"] == asset_id:
            return laptop
    raise HTTPException(status_code=404, detail="Laptop not found")


@app.post("/laptops", response_model=LaptopAsset, status_code=201)
def create_laptop(laptop: LaptopAsset):
    for existing in laptops:
        if existing["asset_id"] == laptop.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    new_laptop = laptop.dict()
    laptops.append(new_laptop)
    return new_laptop

@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop: LaptopAsset):
    if asset_id != laptop.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    for i in range(len(laptops)):
        if laptops[i]["asset_id"] == asset_id:
            laptops[i] = laptop.dict()
            return laptops[i]
    raise HTTPException(status_code=404, detail="Laptop not found")

@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for laptop in laptops:
        if laptop["asset_id"] == asset_id:
            laptops.remove(laptop)
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")

#Sample output


#1. Post laptop

#Request

#  {
#  "asset_id": 2,
#  "serial_number": "XYZ98765",
#  "model_name": "HP EliteBook 840",
#  "assigned_to_emp_id" 54321,
#  "status": "assigned",
#  "purchase_year": 2021,
#  "location": "Chennai"
#}

#Response # 200

# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2021,
#   "location": "Chennai"
# }

# Response headers
#  content-length: 162 
#  content-type: application/json 
#  date: Mon,24 Nov 2025 11:06:09 GMT 
#  server: uvicorn 


# 2. Get all 

# Request

# curl -X 'GET' \
#   'http://127.0.0.1:8000/laptops' \
#   -H 'accept: application/json'

	
# Response body
# Download
# [
#   {
#     "asset_id": 2,
#     "serial_number": "XYZ98765",
#     "model_name": "HP EliteBook 840",
#     "assigned_to_emp_id": 54321,
#     "status": "assigned",
#     "purchase_year": 2021,
#     "location": "Chennai"
#   }
# ]
# Response headers
#  content-length: 164 
#  content-type: application/json 
#  date: Mon,24 Nov 2025 11:41:54 GMT 
#  server: uvicorn


#3. Get by id

# curl -X 'GET' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json'


# Response body
# 200	
# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2021,
#   "location": "Chennai"
# }


#4. Put command

#Request

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "asset_id": 2,
#     "serial_number": "XYZ98765",
#     "model_name": "Macbook m1pro",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2020,
#     "location": "Ranchi"
#   }'


#Response
	
# 200
# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "Macbook m1pro",
#   "assigned_to_emp_id": 12345,
#   "status": "assigned",
#   "purchase_year": 2020,
#   "location": "Ranchi"
# }

#5. Delete api by emp_id

#Request
# curl -X 'DELETE' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json'

#Response
#200
# {
#   "detail": "Laptop deleted successfully"
# }
