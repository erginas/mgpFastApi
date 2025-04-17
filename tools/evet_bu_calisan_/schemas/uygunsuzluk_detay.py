from pydantic import BaseModel
from typing import Optional

class UygunsuzlukDetayBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    parti_no: Optional[String] = None
    lot_no: Optional[String] = None
    konu: Optional[String] = None
    parti_miktari: Optional[Float] = None
    uygunsuzluk_miktari: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    aciklama: Optional[String] = None
    isemri_no: Optional[String] = None
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Float] = None
    dof_no: Optional[String] = None
    diger_ref_no: Optional[String] = None
    fonksiyon: Optional[String] = None
    tespit_tarihi: Optional[DateTime] = None
    tespit_yeri: Optional[String] = None
    kk_lot_no: Optional[String] = None
    irsaliye_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukDetayCreate(UygunsuzlukDetayBase):
    pass

class UygunsuzlukDetay(UygunsuzlukDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True