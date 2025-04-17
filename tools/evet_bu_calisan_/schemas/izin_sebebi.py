from pydantic import BaseModel
from typing import Optional

class IzinSebebiBase(BaseModel):
    sebep_kodu: Optional[Integer] = None
    adi: Optional[String] = None
    tipi: Optional[String] = None
    turu: Optional[String] = None
    ucretlimi: Optional[String] = None
    ttipi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IzinSebebiCreate(IzinSebebiBase):
    pass

class IzinSebebi(IzinSebebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True