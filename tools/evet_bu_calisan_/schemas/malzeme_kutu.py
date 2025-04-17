from pydantic import BaseModel
from typing import Optional

class MalzemeKutuBase(BaseModel):
    id: Optional[String] = None
    adi: Optional[String] = None
    en: Optional[String] = None
    yukseklik: Optional[String] = None
    boy: Optional[String] = None
    tip: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemeKutuCreate(MalzemeKutuBase):
    pass

class MalzemeKutu(MalzemeKutuBase):
    id: Optional[int]

    class Config:
        orm_mode = True