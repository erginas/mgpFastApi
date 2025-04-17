from pydantic import BaseModel
from typing import Optional

class DepoYetkilisiBase(BaseModel):
    kimlik_no: Optional[Float] = None
    depo_kodu: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DepoYetkilisiCreate(DepoYetkilisiBase):
    pass

class DepoYetkilisi(DepoYetkilisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True