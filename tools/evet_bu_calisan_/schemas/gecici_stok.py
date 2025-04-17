from pydantic import BaseModel
from typing import Optional

class GeciciStokBase(BaseModel):
    giris_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    kontrol_eden: Optional[Float] = None
    teslim_alan: Optional[Float] = None
    teslim_tarihi: Optional[DateTime] = None
    irsaliye_no: Optional[String] = None
    irsaliye_tarihi: Optional[DateTime] = None
    aciklama: Optional[String] = None
    yil: Optional[Float] = None
    depo_kodu: Optional[Integer] = None
    alma_zamani: Optional[DateTime] = None
    kontrol_zamani: Optional[DateTime] = None
    hareket_kodu: Optional[Float] = None
    sertifika_ref_no: Optional[Float] = None
    referans_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GeciciStokCreate(GeciciStokBase):
    pass

class GeciciStok(GeciciStokBase):
    id: Optional[int]

    class Config:
        orm_mode = True