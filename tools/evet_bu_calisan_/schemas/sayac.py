from pydantic import BaseModel
from typing import Optional

class SayacBase(BaseModel):
    adi: Optional[String] = None
    numara: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SayacCreate(SayacBase):
    pass

class Sayac(SayacBase):
    id: Optional[int]

    class Config:
        orm_mode = True