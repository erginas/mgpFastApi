from pydantic import BaseModel
from typing import Optional

class UygunsuzlukBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    fonksiyon: Optional[String] = None
    tespit_tarihi: Optional[DateTime] = None
    tespit_yeri: Optional[String] = None
    konu: Optional[String] = None
    aciklama: Optional[String] = None
    kayit_z: Optional[DateTime] = None
    eski_rapor_no: Optional[String] = None
    kapandi_fl: Optional[String] = None
    kapandi_tarihi: Optional[DateTime] = None
    firma_kodu: Optional[Integer] = None
    irsaliye_no: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    etiket_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukCreate(UygunsuzlukBase):
    pass

class Uygunsuzluk(UygunsuzlukBase):
    id: Optional[int]

    class Config:
        orm_mode = True