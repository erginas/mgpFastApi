from pydantic import BaseModel
from typing import Optional

class HataKodlariBase(BaseModel):
    hata_no: Optional[Float] = None
    bagimli_hata_no: Optional[Float] = None
    kodu: Optional[String] = None
    adi: Optional[String] = None
    kimlik_no: Optional[Float] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class HataKodlariCreate(HataKodlariBase):
    pass

class HataKodlari(HataKodlariBase):
    id: Optional[int]

    class Config:
        orm_mode = True