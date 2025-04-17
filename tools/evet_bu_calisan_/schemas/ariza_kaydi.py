from pydantic import BaseModel
from typing import Optional

class ArizaKaydiBase(BaseModel):
    id: Optional[Integer] = None
    tarih: Optional[DateTime] = None
    tezgah_no: Optional[String] = None
    ariza_turu: Optional[String] = None
    ariza_nedeni: Optional[String] = None
    yapilan_islem: Optional[String] = None
    baslama_zamani: Optional[DateTime] = None
    bitis_zamani: Optional[DateTime] = None
    kaydi_acan: Optional[Integer] = None
    tamiri_yapan: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ArizaKaydiCreate(ArizaKaydiBase):
    pass

class ArizaKaydi(ArizaKaydiBase):
    id: Optional[int]

    class Config:
        orm_mode = True