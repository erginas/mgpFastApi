from pydantic import BaseModel
from typing import Optional

class PerformansBase(BaseModel):
    performans_yil: Optional[Float] = None
    performans_ay: Optional[Float] = None
    performans_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    kaydeden: Optional[Float] = None
    tipi: Optional[String] = None
    degerlendirme_puani: Optional[Float] = None
    olumlu_fl: Optional[String] = None
    aciklama: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_z: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class PerformansCreate(PerformansBase):
    pass

class Performans(PerformansBase):
    id: Optional[int]

    class Config:
        orm_mode = True