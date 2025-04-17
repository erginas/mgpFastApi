from pydantic import BaseModel
from typing import Optional

class BankaHesabiBase(BaseModel):
    banka_kodu: Optional[Float] = None
    hesap_kodu: Optional[Float] = None
    hesap_no: Optional[String] = None
    adi: Optional[String] = None
    acilis_tarihi: Optional[DateTime] = None
    kapanis_tarihi: Optional[DateTime] = None
    iban_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class BankaHesabiCreate(BankaHesabiBase):
    pass

class BankaHesabi(BankaHesabiBase):
    id: Optional[int]

    class Config:
        orm_mode = True