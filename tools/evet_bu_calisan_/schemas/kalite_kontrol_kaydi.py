from pydantic import BaseModel
from typing import Optional

class KaliteKontrolKaydiBase(BaseModel):
    kalite_kontrol_kayit_id: Optional[String] = None
    resim_olcu_id: Optional[String] = None
    isemri_no: Optional[String] = None
    olculen_deger: Optional[Float] = None
    olcum_zamani: Optional[DateTime] = None
    gozlem: Optional[String] = None
    aciklama: Optional[String] = None
    sonuc: Optional[String] = None
    ornek_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KaliteKontrolKaydiCreate(KaliteKontrolKaydiBase):
    pass

class KaliteKontrolKaydi(KaliteKontrolKaydiBase):
    id: Optional[int]

    class Config:
        orm_mode = True