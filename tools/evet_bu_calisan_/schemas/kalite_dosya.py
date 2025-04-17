from pydantic import BaseModel
from typing import Optional

class KaliteDosyaBase(BaseModel):
    id: Optional[Integer] = None
    dosya_no: Optional[String] = None
    dosya_adi: Optional[String] = None
    icerik: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class KaliteDosyaCreate(KaliteDosyaBase):
    pass

class KaliteDosya(KaliteDosyaBase):
    id: Optional[int]

    class Config:
        orm_mode = True