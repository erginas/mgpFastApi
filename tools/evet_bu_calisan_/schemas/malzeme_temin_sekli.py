from pydantic import BaseModel
from typing import Optional

class MalzemeTeminSekliBase(BaseModel):
    temin_sekil_kodu: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    oncelik: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeTeminSekliCreate(MalzemeTeminSekliBase):
    pass

class MalzemeTeminSekli(MalzemeTeminSekliBase):
    id: Optional[int]

    class Config:
        orm_mode = True