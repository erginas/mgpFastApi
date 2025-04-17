from pydantic import BaseModel
from typing import Optional

class BankaBase(BaseModel):
    banka_kodu: Optional[Float] = None
    adi: Optional[String] = None
    sube_adi: Optional[String] = None
    eft_kodu: Optional[String] = None
    swift_kodu: Optional[String] = None
    il: Optional[String] = None
    ilce: Optional[String] = None
    sube_kodu: Optional[String] = None
    doviz_cinsi: Optional[String] = None
    hesap_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class BankaCreate(BankaBase):
    pass

class Banka(BankaBase):
    id: Optional[int]

    class Config:
        orm_mode = True