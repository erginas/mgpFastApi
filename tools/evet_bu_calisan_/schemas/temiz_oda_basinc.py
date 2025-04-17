from pydantic import BaseModel
from typing import Optional

class TemizOdaBasincBase(BaseModel):
    tarih: Optional[DateTime] = None
    deger: Optional[Integer] = None
    kayit_sikligi: Optional[Integer] = None
    kayit_birim: Optional[Integer] = None
    birim: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TemizOdaBasincCreate(TemizOdaBasincBase):
    pass

class TemizOdaBasinc(TemizOdaBasincBase):
    id: Optional[int]

    class Config:
        orm_mode = True