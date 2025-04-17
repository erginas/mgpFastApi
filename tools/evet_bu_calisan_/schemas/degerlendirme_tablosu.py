from pydantic import BaseModel
from typing import Optional

class DegerlendirmeTablosuBase(BaseModel):
    gun_sayisi: Optional[Integer] = None
    oncelik_a: Optional[Integer] = None
    oncelik_b: Optional[Integer] = None
    oncelik_c: Optional[Integer] = None
    oncelik_d: Optional[Integer] = None
    tarih: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DegerlendirmeTablosuCreate(DegerlendirmeTablosuBase):
    pass

class DegerlendirmeTablosu(DegerlendirmeTablosuBase):
    id: Optional[int]

    class Config:
        orm_mode = True