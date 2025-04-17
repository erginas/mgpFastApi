from pydantic import BaseModel
from typing import Optional

class UbbFiyatBase(BaseModel):
    stok_kodu: Optional[String] = None
    fiyat: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UbbFiyatCreate(UbbFiyatBase):
    pass

class UbbFiyat(UbbFiyatBase):
    id: Optional[int]

    class Config:
        orm_mode = True