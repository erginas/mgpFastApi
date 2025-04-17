from pydantic import BaseModel
from typing import Optional

class UlkeBase(BaseModel):
    kodu: Optional[String] = None
    iso_kodu: Optional[String] = None
    tr_adi: Optional[String] = None
    en_adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UlkeCreate(UlkeBase):
    pass

class Ulke(UlkeBase):
    id: Optional[int]

    class Config:
        orm_mode = True