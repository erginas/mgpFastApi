from pydantic import BaseModel
from typing import Optional

class SevkEdilenSiparisBase(BaseModel):
    sevk_yil: Optional[Float] = None
    sevk_ay: Optional[Float] = None
    sevk_no: Optional[Float] = None
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SevkEdilenSiparisCreate(SevkEdilenSiparisBase):
    pass

class SevkEdilenSiparis(SevkEdilenSiparisBase):
    id: Optional[int]

    class Config:
        orm_mode = True