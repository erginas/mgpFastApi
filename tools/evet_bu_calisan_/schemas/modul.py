from pydantic import BaseModel
from typing import Optional

class ModulBase(BaseModel):
    id: Optional[Integer] = None
    adi: Optional[String] = None
    version: Optional[String] = None
    data: Optional[String] = None
    path: Optional[String] = None
    aktif: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ModulCreate(ModulBase):
    pass

class Modul(ModulBase):
    id: Optional[int]

    class Config:
        orm_mode = True