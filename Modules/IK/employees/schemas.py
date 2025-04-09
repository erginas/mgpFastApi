from pydantic import BaseModel
from datetime import date
from typing import Optional

# Employee creation and update schemas
class EmployeeBase(BaseModel):
    name: str
    hire_date: date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    name: Optional[str] = None
    hire_date: Optional[date] = None

# Response schema
class EmployeeOut(EmployeeBase):
    employee_id: int

    class Config:
        orm_mode = True  # SQLAlchemy modelini Pydantic modeline dönüştürür
