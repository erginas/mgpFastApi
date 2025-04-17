from pydantic import BaseModel
from typing import Optional

class ToplantiMaddesiBase(BaseModel):
    toplanti_yil: Optional[Float] = None
    toplanti_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    konu: Optional[String] = None
    kayit_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ToplantiMaddesiCreate(ToplantiMaddesiBase):
    pass

class ToplantiMaddesi(ToplantiMaddesiBase):
    id: Optional[int]

    class Config:
        orm_mode = True