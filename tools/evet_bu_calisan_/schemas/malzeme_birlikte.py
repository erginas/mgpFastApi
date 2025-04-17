from pydantic import BaseModel
from typing import Optional

class MalzemeBirlikteBase(BaseModel):
    malzeme_no1: Optional[Integer] = None
    malzeme_no2: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeBirlikteCreate(MalzemeBirlikteBase):
    pass

class MalzemeBirlikte(MalzemeBirlikteBase):
    id: Optional[int]

    class Config:
        orm_mode = True