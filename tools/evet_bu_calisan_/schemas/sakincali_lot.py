from pydantic import BaseModel
from typing import Optional

class SakincaliLotBase(BaseModel):
    lot_no: Optional[String] = None
    kimlik_no: Optional[Float] = None
    ce_durumu: Optional[String] = None
    kayit_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SakincaliLotCreate(SakincaliLotBase):
    pass

class SakincaliLot(SakincaliLotBase):
    id: Optional[int]

    class Config:
        orm_mode = True