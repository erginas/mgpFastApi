from pydantic import BaseModel
from typing import Optional

class UygunsuzlukGorusuBase(BaseModel):
    sira_no: Optional[Integer] = None
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    birim_no: Optional[Integer] = None
    tarih: Optional[DateTime] = None
    gorus: Optional[String] = None
    gorus_karar_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukGorusuCreate(UygunsuzlukGorusuBase):
    pass

class UygunsuzlukGorusu(UygunsuzlukGorusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True