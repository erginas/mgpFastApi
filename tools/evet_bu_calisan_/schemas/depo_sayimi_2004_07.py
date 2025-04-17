from pydantic import BaseModel
from typing import Optional

class DepoSayimi200407Base(BaseModel):
    depo_kodu: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    lot_no: Optional[String] = None
    ilk_miktar: Optional[Float] = None
    son_miktar: Optional[Float] = None
    ilk_hareket: Optional[Float] = None
    son_hareket: Optional[Float] = None
    ilk_zaman: Optional[DateTime] = None
    son_zaman: Optional[DateTime] = None
    aciklama: Optional[String] = None
    sayilan_miktar: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    durumu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DepoSayimi200407Create(DepoSayimi200407Base):
    pass

class DepoSayimi200407(DepoSayimi200407Base):
    id: Optional[int]

    class Config:
        orm_mode = True