from pydantic import BaseModel
from typing import Optional

class KontrolPrefixBase(BaseModel):
    prefix: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KontrolPrefixCreate(KontrolPrefixBase):
    pass

class KontrolPrefix(KontrolPrefixBase):
    id: Optional[int]

    class Config:
        orm_mode = True