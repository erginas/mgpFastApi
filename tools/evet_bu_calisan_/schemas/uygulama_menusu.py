from pydantic import BaseModel
from typing import Optional

class UygulamaMenusuBase(BaseModel):
    menu_kodu: Optional[Float] = None
    sinif_adi: Optional[String] = None
    basligi: Optional[String] = None
    tanimi: Optional[String] = None
    ust_menu: Optional[Float] = None
    sira: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygulamaMenusuCreate(UygulamaMenusuBase):
    pass

class UygulamaMenusu(UygulamaMenusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True