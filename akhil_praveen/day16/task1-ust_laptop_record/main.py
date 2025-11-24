from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

app = FastAPI(title="Ust Laptop Inventory")

