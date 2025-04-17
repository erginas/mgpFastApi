from pydantic import BaseModel
from typing import Optional

class CeKapsam2019Base(BaseModel):
    stok_kodu: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class CeKapsam2019Create(CeKapsam2019Base):
    pass

class CeKapsam2019(CeKapsam2019Base):
    id: Optional[int]

    class Config:
        orm_mode = True