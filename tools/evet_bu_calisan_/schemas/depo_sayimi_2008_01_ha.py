from pydantic import BaseModel
from typing import Optional

class DepoSayimi200801HaBase(BaseModel):
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

class DepoSayimi200801HaCreate(DepoSayimi200801HaBase):
    pass

class DepoSayimi200801Ha(DepoSayimi200801HaBase):
    id: Optional[int]

    class Config:
        orm_mode = True