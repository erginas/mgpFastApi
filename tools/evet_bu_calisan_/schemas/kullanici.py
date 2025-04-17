from pydantic import BaseModel
from typing import Optional

class KullaniciBase(BaseModel):
    kullanici_kodu: Optional[String] = None
    kimlik_no: Optional[Float] = None
    sifre_eski: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class KullaniciCreate(KullaniciBase):
    pass

class Kullanici(KullaniciBase):
    id: Optional[int]

    class Config:
        orm_mode = True