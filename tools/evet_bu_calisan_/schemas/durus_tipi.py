from pydantic import BaseModel
from typing import Optional

class DurusTipiBase(BaseModel):
    durus_detay_kodu: Optional[Float] = None
    aciklama: Optional[String] = None
    kullanim_alani: Optional[String] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DurusTipiCreate(DurusTipiBase):
    pass

class DurusTipi(DurusTipiBase):
    id: Optional[int]

    class Config:
        orm_mode = True