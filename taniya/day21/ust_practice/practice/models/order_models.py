import re
from typing import Optional,Literal
from pydantic import BaseModel, Field, field_validator
from datetime import date

# allowed_status={"Pending","Shipped","Delivered","Cancelled"}

class Orders(BaseModel):
    order_id:int=0
    customer_name:str=Field(...,pattern=r"^[A-Za-z ]+")
    product_id:int=Field(...,gt=0)
    quantity:int=Field(...,gt=0)
    status:str=Literal["Pending","Shipped","Delivered","Cancelled"]
    
    
    