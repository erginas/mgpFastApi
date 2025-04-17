from pydantic import BaseModel
from typing import Optional

class SkPlaniBase(BaseModel):
    sk_plan_kodu: Optional[Float] = None
    adi: Optional[String] = None
    stok_kodu: Optional[String] = None
    ust_sk_plan_kodu: Optional[Float] = None
    name: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SkPlaniCreate(SkPlaniBase):
    pass

class SkPlani(SkPlaniBase):
    id: Optional[int]

    class Config:
        orm_mode = True