from pydantic import BaseModel
from typing import Optional

class KodlarBase(BaseModel):
    id: Optional[Integer] = None
    turu: Optional[String] = None
    kodu: Optional[String] = None
    adi: Optional[String] = None
    aktif: Optional[Integer] = None
    sira: Optional[Integer] = None
    grup_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KodlarCreate(KodlarBase):
    pass

class Kodlar(KodlarBase):
    id: Optional[int]

    class Config:
        orm_mode = True