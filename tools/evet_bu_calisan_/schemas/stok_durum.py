from pydantic import BaseModel
from typing import Optional

class StokDurumBase(BaseModel):
    depo_kodu: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    lot_no: Optional[String] = None
    ce_bilgisi: Optional[String] = None
    son_kullanma_tarihi: Optional[DateTime] = None
    giren_miktar: Optional[Integer] = None
    cikan_miktar: Optional[Integer] = None
    kalan_miktar: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class StokDurumCreate(StokDurumBase):
    pass

class StokDurum(StokDurumBase):
    id: Optional[int]

    class Config:
        orm_mode = True