from pydantic import BaseModel
from typing import Optional

class AstipDepoBase(BaseModel):
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    lot_no: Optional[String] = None
    adet: Optional[Integer] = None
    skt: Optional[String] = None
    iade_no: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    iade_sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AstipDepoCreate(AstipDepoBase):
    pass

class AstipDepo(AstipDepoBase):
    id: Optional[int]

    class Config:
        orm_mode = True