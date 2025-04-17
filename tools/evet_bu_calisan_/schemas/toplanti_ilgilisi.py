from pydantic import BaseModel
from typing import Optional

class ToplantiIlgilisiBase(BaseModel):
    toplanti_yil: Optional[Float] = None
    toplanti_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    birim_no: Optional[Integer] = None
    katilim_fl: Optional[String] = None
    firma: Optional[String] = None
    katilimci: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ToplantiIlgilisiCreate(ToplantiIlgilisiBase):
    pass

class ToplantiIlgilisi(ToplantiIlgilisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True