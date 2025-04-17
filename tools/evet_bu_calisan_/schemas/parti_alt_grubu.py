from pydantic import BaseModel
from typing import Optional

class PartiAltGrubuBase(BaseModel):
    refakat_no: Optional[String] = None
    isemri_no: Optional[String] = None
    miktar: Optional[Float] = None
    nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class PartiAltGrubuCreate(PartiAltGrubuBase):
    pass

class PartiAltGrubu(PartiAltGrubuBase):
    id: Optional[int]

    class Config:
        orm_mode = True