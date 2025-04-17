from pydantic import BaseModel
from typing import Optional

class SevkiyatLogBase(BaseModel):
    sip_yil: Optional[Integer] = None
    sip_ay: Optional[Integer] = None
    sip_no: Optional[Integer] = None
    sevk_yil: Optional[Integer] = None
    sevk_ay: Optional[Integer] = None
    sevk_no: Optional[Integer] = None
    kk: Optional[Integer] = None
    miktar: Optional[Integer] = None
    sql: Optional[String] = None
    kts: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SevkiyatLogCreate(SevkiyatLogBase):
    pass

class SevkiyatLog(SevkiyatLogBase):
    id: Optional[int]

    class Config:
        orm_mode = True