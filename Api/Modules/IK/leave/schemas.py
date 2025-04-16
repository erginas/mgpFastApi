from pydantic import BaseModel
from datetime import date
from enum import Enum

class LeaveTypeEnum(str, Enum):
    annual = "Annual"
    sick = "Sick"
    unpaid = "Unpaid"

class LeaveBase(BaseModel):
    leave_type: LeaveTypeEnum
    start_date: date
    end_date: date
    reason: str

class LeaveCreate(LeaveBase):
    pass

class Leave(LeaveBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True
