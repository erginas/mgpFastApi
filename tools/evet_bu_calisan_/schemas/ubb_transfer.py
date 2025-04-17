from pydantic import BaseModel
from typing import Optional

class UbbTransferBase(BaseModel):
    stok_kodu: Optional[String] = None
    c09_ubb_kodu: Optional[String] = None
    c35_unspsc_kodu: Optional[String] = None
    c36_unspsc_adi: Optional[String] = None
    c10_ambalaj_turu: Optional[String] = None
    c18_ambalaj_miktar: Optional[String] = None
    c19_ambalaj_birimi: Optional[String] = None
    c20_genislik: Optional[String] = None
    c21_yukseklik: Optional[String] = None
    c22_derinlik: Optional[String] = None
    c02_gmdn_kodu: Optional[String] = None
    c32_gmdn_adi: Optional[String] = None
    c40_ubb_kayit_tarihi: Optional[String] = None
    c41_brans_kodu: Optional[String] = None
    c42_brans_adi: Optional[String] = None
    c37_ubb_kayitli: Optional[String] = None
    mlz_no: Optional[Float] = None
    c12_ubb_adi: Optional[String] = None
    c00_kok_urun: Optional[String] = None
    fiyat: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UbbTransferCreate(UbbTransferBase):
    pass

class UbbTransfer(UbbTransferBase):
    id: Optional[int]

    class Config:
        orm_mode = True