from pydantic import BaseModel
from typing import Optional

class YetkinlikBase(BaseModel):
    sira_no: Optional[Integer] = None
    adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class YetkinlikCreate(YetkinlikBase):
    pass

class Yetkinlik(YetkinlikBase):
    id: Optional[int]

    class Config:
        orm_mode = True