from pydantic import BaseModel
from typing import Optional

class RakipMalzemeBase(BaseModel):
    sira_no: Optional[Integer] = None
    malzeme_kodu: Optional[String] = None
    malzeme_adi: Optional[String] = None
    marka: Optional[String] = None
    firma_adi: Optional[String] = None
    turu: Optional[String] = None
    durumu: Optional[String] = None
    aciklama: Optional[String] = None
    kombine_urun: Optional[String] = None
    doviz1: Optional[Float] = None
    dovizcinsi1: Optional[String] = None
    tarih: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class RakipMalzemeCreate(RakipMalzemeBase):
    pass

class RakipMalzeme(RakipMalzemeBase):
    id: Optional[int]

    class Config:
        orm_mode = True