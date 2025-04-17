from pydantic import BaseModel
from typing import Optional

class KullaniciFormBase(BaseModel):
    kullanici_kodu: Optional[String] = None
    menu_kodu: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KullaniciFormCreate(KullaniciFormBase):
    pass

class KullaniciForm(KullaniciFormBase):
    id: Optional[int]

    class Config:
        orm_mode = True