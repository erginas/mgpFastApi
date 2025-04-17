from pydantic import BaseModel
from typing import Optional

class MalzemeUbbEkBase(BaseModel):
    malzeme_no: Optional[Integer] = None
    ubb_no_tipi: Optional[String] = None
    ubb_no: Optional[String] = None
    marka: Optional[String] = None
    katalog_no: Optional[String] = None
    unspsc_kodu: Optional[String] = None
    unspsc_sinif_adi: Optional[String] = None
    ithal_imal_fl: Optional[String] = None
    ambalaj_turu: Optional[String] = None
    ambalaj_ici_miktar: Optional[Float] = None
    ambalaj_birimi: Optional[String] = None
    genislik: Optional[Float] = None
    yukseklik: Optional[Float] = None
    derinlik: Optional[Float] = None
    gmdn_kodu: Optional[String] = None
    gmdn_adi: Optional[String] = None
    yonetmelik: Optional[String] = None
    ubb_brans_kodu: Optional[String] = None
    ubb_brans_adi: Optional[String] = None
    durumu: Optional[String] = None
    mevzuat_kaydi_fl: Optional[String] = None
    etiket_adi: Optional[String] = None
    fiyat: Optional[Float] = None
    fiyat_sonlanma_t: Optional[DateTime] = None
    sertifika_adi: Optional[String] = None
    sertifika_bitis_t: Optional[String] = None
    kisa_kodu: Optional[String] = None
    aciklama: Optional[String] = None
    ubb_kayit_t: Optional[DateTime] = None
    belgelendirme_kurulusu: Optional[String] = None
    uygunluk_beyani: Optional[String] = None
    ce_sinifi: Optional[String] = None
    sut_kodu: Optional[String] = None
    sut_adi: Optional[String] = None
    raf_omru: Optional[String] = None
    son_onay_tarihi: Optional[DateTime] = None
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    ubb_yedek: Optional[String] = None
    gecici_ean: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeUbbEkCreate(MalzemeUbbEkBase):
    pass

class MalzemeUbbEk(MalzemeUbbEkBase):
    id: Optional[int]

    class Config:
        orm_mode = True