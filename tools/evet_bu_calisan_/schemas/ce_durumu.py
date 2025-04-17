from pydantic import BaseModel
from typing import Optional

class CeDurumuBase(BaseModel):
    lot_no: Optional[String] = None
    ce_bilgisi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class CeDurumuCreate(CeDurumuBase):
    pass

class CeDurumu(CeDurumuBase):
    id: Optional[int]

    class Config:
        orm_mode = True