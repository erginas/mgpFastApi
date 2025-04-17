from pydantic import BaseModel
from typing import Optional

class AktarIadeBase(BaseModel):
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    lot_no: Optional[String] = None
    miktar: Optional[Integer] = None
    skt: Optional[String] = None
    aciklama: Optional[String] = None
    ozel_olcu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AktarIadeCreate(AktarIadeBase):
    pass

class AktarIade(AktarIadeBase):
    id: Optional[int]

    class Config:
        orm_mode = True