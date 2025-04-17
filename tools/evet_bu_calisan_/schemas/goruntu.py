from pydantic import BaseModel
from typing import Optional

class GoruntuBase(BaseModel):
    goruntu_no: Optional[Float] = None
    icerik: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GoruntuCreate(GoruntuBase):
    pass

class Goruntu(GoruntuBase):
    id: Optional[int]

    class Config:
        orm_mode = True