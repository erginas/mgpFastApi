from pydantic import BaseModel
from typing import Optional

class SayacSilinenBase(BaseModel):
    adi: Optional[String] = None
    numara: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SayacSilinenCreate(SayacSilinenBase):
    pass

class SayacSilinen(SayacSilinenBase):
    id: Optional[int]

    class Config:
        orm_mode = True