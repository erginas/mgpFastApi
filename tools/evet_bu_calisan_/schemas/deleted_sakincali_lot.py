from pydantic import BaseModel
from typing import Optional

class DeletedSakincaliLotBase(BaseModel):
    lt: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DeletedSakincaliLotCreate(DeletedSakincaliLotBase):
    pass

class DeletedSakincaliLot(DeletedSakincaliLotBase):
    id: Optional[int]

    class Config:
        orm_mode = True