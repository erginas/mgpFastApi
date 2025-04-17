from pydantic import BaseModel
from typing import Optional

class TezgahGrubuBase(BaseModel):
    grup_no: Optional[Float] = None
    bagimli_grup_no: Optional[Float] = None
    grup_kodu: Optional[String] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TezgahGrubuCreate(TezgahGrubuBase):
    pass

class TezgahGrubu(TezgahGrubuBase):
    id: Optional[int]

    class Config:
        orm_mode = True