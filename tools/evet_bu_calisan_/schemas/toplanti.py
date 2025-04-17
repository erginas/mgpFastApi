from pydantic import BaseModel
from typing import Optional

class ToplantiBase(BaseModel):
    toplanti_yil: Optional[Float] = None
    toplanti_no: Optional[Float] = None
    konu: Optional[String] = None
    yeri: Optional[String] = None
    baslama_t: Optional[DateTime] = None
    bitis_t: Optional[DateTime] = None
    kimlik_no: Optional[Float] = None
    iptal_eden: Optional[Float] = None
    kayit_t: Optional[DateTime] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    goster_fl: Optional[String] = None
    durumu: Optional[String] = None
    toplanti_cagrisi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ToplantiCreate(ToplantiBase):
    pass

class Toplanti(ToplantiBase):
    id: Optional[int]

    class Config:
        orm_mode = True