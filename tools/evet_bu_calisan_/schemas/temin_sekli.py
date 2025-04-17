from pydantic import BaseModel
from typing import Optional

class TeminSekliBase(BaseModel):
    temin_sekil_kodu: Optional[Float] = None
    adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TeminSekliCreate(TeminSekliBase):
    pass

class TeminSekli(TeminSekliBase):
    id: Optional[int]

    class Config:
        orm_mode = True