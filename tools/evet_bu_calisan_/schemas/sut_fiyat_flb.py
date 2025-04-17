from pydantic import BaseModel
from typing import Optional

class SutFiyatFlbBase(BaseModel):
    id: Optional[Integer] = None
    gecerlik_tarihi: Optional[DateTime] = None
    sut_kodu: Optional[String] = None
    ean: Optional[String] = None
    stok_kodu: Optional[String] = None
    fiyat: Optional[Integer] = None
    iskonto: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SutFiyatFlbCreate(SutFiyatFlbBase):
    pass

class SutFiyatFlb(SutFiyatFlbBase):
    id: Optional[int]

    class Config:
        orm_mode = True