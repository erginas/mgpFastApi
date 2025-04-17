from pydantic import BaseModel
from typing import Optional

class DosyaMalzemeBase(BaseModel):
    kalite_dosya_id: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DosyaMalzemeCreate(DosyaMalzemeBase):
    pass

class DosyaMalzeme(DosyaMalzemeBase):
    id: Optional[int]

    class Config:
        orm_mode = True