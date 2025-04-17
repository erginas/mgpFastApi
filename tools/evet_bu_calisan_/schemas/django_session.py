from pydantic import BaseModel
from typing import Optional

class DjangoSessionBase(BaseModel):
    session_key: Optional[String] = None
    session_data: Optional[String] = None
    expire_date: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DjangoSessionCreate(DjangoSessionBase):
    pass

class DjangoSession(DjangoSessionBase):
    id: Optional[int]

    class Config:
        orm_mode = True