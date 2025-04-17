from pydantic import BaseModel
from typing import Optional

class DepoHareketSebebiBase(BaseModel):
    hareket_kodu: Optional[Float] = None
    depo_kodu: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DepoHareketSebebiCreate(DepoHareketSebebiBase):
    pass

class DepoHareketSebebi(DepoHareketSebebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True