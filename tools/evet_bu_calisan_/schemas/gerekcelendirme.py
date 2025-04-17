from pydantic import BaseModel
from typing import Optional

class GerekcelendirmeBase(BaseModel):
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Float] = None
    gerekce: Optional[String] = None
    gecikme_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GerekcelendirmeCreate(GerekcelendirmeBase):
    pass

class Gerekcelendirme(GerekcelendirmeBase):
    id: Optional[int]

    class Config:
        orm_mode = True