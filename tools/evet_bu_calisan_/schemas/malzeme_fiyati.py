from pydantic import BaseModel
from typing import Optional

class MalzemeFiyatiBase(BaseModel):
    tarife_no: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    gecerlilik_tarihi: Optional[DateTime] = None
    kisa_kodu: Optional[String] = None
    birim_fiyati: Optional[Float] = None
    sira_no: Optional[Integer] = None
    ems_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemeFiyatiCreate(MalzemeFiyatiBase):
    pass

class MalzemeFiyati(MalzemeFiyatiBase):
    id: Optional[int]

    class Config:
        orm_mode = True