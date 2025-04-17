from pydantic import BaseModel
from typing import Optional

class DegerlendirmeKriteriBase(BaseModel):
    kriter_no: Optional[Float] = None
    adi: Optional[String] = None
    dusuk_puani: Optional[Float] = None
    yuksek_puani: Optional[Float] = None
    kaydeden: Optional[Float] = None
    yayin_tarihi: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DegerlendirmeKriteriCreate(DegerlendirmeKriteriBase):
    pass

class DegerlendirmeKriteri(DegerlendirmeKriteriBase):
    id: Optional[int]

    class Config:
        orm_mode = True