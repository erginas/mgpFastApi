from pydantic import BaseModel
from typing import Optional

class ReceteSinifiBase(BaseModel):
    id: Optional[Integer] = None
    adi: Optional[String] = None
    turu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteSinifiCreate(ReceteSinifiBase):
    pass

class ReceteSinifi(ReceteSinifiBase):
    id: Optional[int]

    class Config:
        orm_mode = True