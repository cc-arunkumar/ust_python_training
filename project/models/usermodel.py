from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid

class UserRole(str, Enum):
    ADMIN = "Admin"
    TP_MANAGER = "TP Manager"
    WFM = "WFM"
    HM = "HM"
    EMPLOYEE_TP = "TP"
    EMPLOYEE_NON_TP = "Non TP"