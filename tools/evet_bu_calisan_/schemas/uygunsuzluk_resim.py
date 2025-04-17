from pydantic import BaseModel
from typing import Optional

class UygunsuzlukResimBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    resim: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukResimCreate(UygunsuzlukResimBase):
    pass

class UygunsuzlukResim(UygunsuzlukResimBase):
    id: Optional[int]

    class Config:
        orm_mode = True