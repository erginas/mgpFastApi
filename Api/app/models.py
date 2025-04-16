from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Malzeme(BaseModel):
    malzeme_no: int
    malzeme_adi: str
    class Config:
        from_attributes = True

