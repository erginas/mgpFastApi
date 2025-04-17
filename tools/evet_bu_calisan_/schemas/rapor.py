from pydantic import BaseModel
from typing import Optional

class RaporBase(BaseModel):
    rapor_no: Optional[Integer] = None
    rapor_adi: Optional[String] = None
    icerik: Optional[String] = None
    id: Optional[Integer] = None
    parent_id: Optional[Integer] = None
    referans_id: Optional[Integer] = None
    turu: Optional[Integer] = None
    aciklama: Optional[String] = None
    ic_kayit: Optional[Integer] = None
    versiyon: Optional[Integer] = None
    gorunurluk: Optional[Integer] = None
    kilitli: Optional[Integer] = None
    kopya_sayisi: Optional[Integer] = None
    kagit_boyu: Optional[Integer] = None
    ust_bosluk: Optional[Integer] = None
    alt_bosluk: Optional[Integer] = None
    barkod_yazici_kullan: Optional[Integer] = None
    saat_sinirli: Optional[Integer] = None
    saatler: Optional[String] = None
    istatistik_tutma: Optional[Integer] = None
    tasarimi_yapan: Optional[String] = None
    sablon: Optional[String] = None
    kk: Optional[Float] = None
    kts: Optional[DateTime] = None
    dts: Optional[DateTime] = None
    kodu: Optional[String] = None
    adi: Optional[String] = None
    guid: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class RaporCreate(RaporBase):
    pass

class Rapor(RaporBase):
    id: Optional[int]

    class Config:
        orm_mode = True