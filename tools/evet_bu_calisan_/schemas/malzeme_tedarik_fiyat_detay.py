from pydantic import BaseModel
from typing import Optional

class MalzemeTedarikFiyatDetayBase(BaseModel):
    id: Optional[Integer] = None
    mlz_ted_fiyat_detay_id: Optional[Integer] = None
    birim_fiyati: Optional[Integer] = None
    para_birimi: Optional[String] = None
    kts: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeTedarikFiyatDetayCreate(MalzemeTedarikFiyatDetayBase):
    pass

class MalzemeTedarikFiyatDetay(MalzemeTedarikFiyatDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True