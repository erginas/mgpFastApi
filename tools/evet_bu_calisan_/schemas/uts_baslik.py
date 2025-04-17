from pydantic import BaseModel
from typing import Optional

class UtsBaslikBase(BaseModel):
    id: Optional[Integer] = None
    adi: Optional[String] = None
    veri_yolu: Optional[String] = None
    bildirim_tipi: Optional[String] = None
    iptal_fl: Optional[Integer] = None
    kodu: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class UtsBaslikCreate(UtsBaslikBase):
    pass

class UtsBaslik(UtsBaslikBase):
    id: Optional[int]

    class Config:
        orm_mode = True