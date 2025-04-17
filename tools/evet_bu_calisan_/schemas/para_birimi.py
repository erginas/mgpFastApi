from pydantic import BaseModel
from typing import Optional

class ParaBirimiBase(BaseModel):
    kisa_kodu: Optional[String] = None
    uzun_adi: Optional[String] = None
    id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ParaBirimiCreate(ParaBirimiBase):
    pass

class ParaBirimi(ParaBirimiBase):
    id: Optional[int]

    class Config:
        orm_mode = True