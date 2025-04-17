from pydantic import BaseModel
from typing import Optional

class ParaBirimiDetayBase(BaseModel):
    id: Optional[Integer] = None
    alis: Optional[Float] = None
    satis: Optional[Float] = None
    forex_alis: Optional[Float] = None
    forex_satis: Optional[Float] = None
    para_birimi: Optional[Integer] = None
    kur_tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ParaBirimiDetayCreate(ParaBirimiDetayBase):
    pass

class ParaBirimiDetay(ParaBirimiDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True