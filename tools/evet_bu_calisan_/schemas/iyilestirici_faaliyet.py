from pydantic import BaseModel
from typing import Optional

class IyilestiriciFaaliyetBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    kayit_tarihi: Optional[DateTime] = None
    konu: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IyilestiriciFaaliyetCreate(IyilestiriciFaaliyetBase):
    pass

class IyilestiriciFaaliyet(IyilestiriciFaaliyetBase):
    id: Optional[int]

    class Config:
        orm_mode = True