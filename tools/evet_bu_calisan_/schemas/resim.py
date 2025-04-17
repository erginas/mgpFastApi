from pydantic import BaseModel
from typing import Optional

class ResimBase(BaseModel):
    id: Optional[Integer] = None
    tipi: Optional[Integer] = None
    icerik: Optional[String] = None
    dosya_adi: Optional[String] = None
    turu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ResimCreate(ResimBase):
    pass

class Resim(ResimBase):
    id: Optional[int]

    class Config:
        orm_mode = True