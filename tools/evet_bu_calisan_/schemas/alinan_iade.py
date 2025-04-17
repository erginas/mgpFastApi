from pydantic import BaseModel
from typing import Optional

class AlinanIadeBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    iade_fis_no: Optional[Float] = None
    firma_kodu: Optional[Integer] = None
    aciklama: Optional[String] = None
    irsaliye: Optional[String] = None
    fatura: Optional[String] = None
    kimlik_no: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    iade_nedeni: Optional[String] = None
    durumu: Optional[String] = None
    birim_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanIadeCreate(AlinanIadeBase):
    pass

class AlinanIade(AlinanIadeBase):
    id: Optional[int]

    class Config:
        orm_mode = True