from pydantic import BaseModel
from typing import Optional

class TanimBase(BaseModel):
    ean_kodu: Optional[String] = None
    stok_kodu: Optional[String] = None
    adi: Optional[String] = None
    en_tanim: Optional[String] = None
    tr_tanim: Optional[String] = None
    standart_1: Optional[String] = None
    materyal_1: Optional[String] = None
    standart_2: Optional[String] = None
    materyal_2: Optional[String] = None
    standart_3: Optional[String] = None
    materyal_3: Optional[String] = None
    kaplama: Optional[String] = None
    olcu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TanimCreate(TanimBase):
    pass

class Tanim(TanimBase):
    id: Optional[int]

    class Config:
        orm_mode = True