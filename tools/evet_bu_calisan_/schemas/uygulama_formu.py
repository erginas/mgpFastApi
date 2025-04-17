from pydantic import BaseModel
from typing import Optional

class UygulamaFormuBase(BaseModel):
    sinif_adi: Optional[String] = None
    iso_referansi: Optional[String] = None
    form_adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygulamaFormuCreate(UygulamaFormuBase):
    pass

class UygulamaFormu(UygulamaFormuBase):
    id: Optional[int]

    class Config:
        orm_mode = True