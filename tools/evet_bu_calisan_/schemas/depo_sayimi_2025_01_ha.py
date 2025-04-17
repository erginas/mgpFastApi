from pydantic import BaseModel
from typing import Optional

class DepoSayimi202501HaBase(BaseModel):
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
    bt_note: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DepoSayimi202501HaCreate(DepoSayimi202501HaBase):
    pass

class DepoSayimi202501Ha(DepoSayimi202501HaBase):
    id: Optional[int]

    class Config:
        orm_mode = True