from pydantic import BaseModel
from typing import Optional

class RaporYeniBase(BaseModel):
    id: Optional[Float] = None
    parent_id: Optional[Float] = None
    referans_id: Optional[Float] = None
    adi: Optional[String] = None
    turu: Optional[Float] = None
    aciklama: Optional[String] = None
    ic_kayit: Optional[Float] = None
    versiyon: Optional[Float] = None
    gorunurluk: Optional[Float] = None
    kilitli: Optional[Float] = None
    kopya_sayisi: Optional[Float] = None
    kagit_boyu: Optional[Float] = None
    ust_bosluk: Optional[Float] = None
    alt_bosluk: Optional[Float] = None
    barkod_yazici_kullan: Optional[Float] = None
    saat_sinirli: Optional[Float] = None
    saatler: Optional[String] = None
    istatistik_tutma: Optional[Float] = None
    tasarimi_yapan: Optional[String] = None
    sablon: Optional[String] = None
    kts: Optional[DateTime] = None
    dts: Optional[DateTime] = None
    kodu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class RaporYeniCreate(RaporYeniBase):
    pass

class RaporYeni(RaporYeniBase):
    id: Optional[int]

    class Config:
        orm_mode = True