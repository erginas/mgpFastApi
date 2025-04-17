from pydantic import BaseModel
from typing import Optional

class KontrolluKayitBase(BaseModel):
    kayit_yili: Optional[Float] = None
    kayit_no: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KontrolluKayitCreate(KontrolluKayitBase):
    pass

class KontrolluKayit(KontrolluKayitBase):
    id: Optional[int]

    class Config:
        orm_mode = True