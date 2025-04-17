from pydantic import BaseModel
from typing import Optional

class DepoSayimi201203Base(BaseModel):
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
    sira_no: Optional[Integer] = None
    son_kullanma_t: Optional[DateTime] = None
    ce_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DepoSayimi201203Create(DepoSayimi201203Base):
    pass

class DepoSayimi201203(DepoSayimi201203Base):
    id: Optional[int]

    class Config:
        orm_mode = True