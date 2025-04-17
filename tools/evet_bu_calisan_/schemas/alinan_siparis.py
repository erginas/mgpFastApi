from pydantic import BaseModel
from typing import Optional

from sqlalchemy import Float, Integer, String, DateTime


class AlinanSiparisBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    tarife_no: Optional[Float] = None
    firma_kodu: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    banka_kodu: Optional[Float] = None
    hesap_kodu: Optional[Float] = None
    aciklama: Optional[String] = None
    ref_belge: Optional[String] = None
    sevk_yeri: Optional[String] = None
    teslim_sekli: Optional[String] = None
    gorusulen_kisi: Optional[String] = None
    tasima_bedeli: Optional[Float] = None
    odeme_sekli: Optional[String] = None
    durumu: Optional[String] = None
    kayit_zamani: Optional[DateTime] = None
    istenilen_termin: Optional[DateTime] = None
    onerilen_termin: Optional[DateTime] = None
    kesinlesen_termin: Optional[DateTime] = None
    fatura_irsaliye_fl: Optional[String] = None
    araci_firma: Optional[Integer] = None
    musteri_termini: Optional[DateTime] = None
    onaylayan: Optional[Float] = None
    onay_tarihi: Optional[DateTime] = None
    hareket_kodu: Optional[Float] = None
    ambar_kimlik_no: Optional[Float] = None
    ambar_sevk_t: Optional[DateTime] = None
    ref_belge_no: Optional[String] = None
    alt_durumu: Optional[String] = None
    kesinlesme_ciddiyeti: Optional[Float] = None
    fatura_kesilme_fl: Optional[String] = None
    birim_no: Optional[Integer] = None
    teslim_suresi: Optional[String] = None
    iskonto_tutari: Optional[Float] = None
    iskonto_yuzdesi: Optional[Float] = None
    opsiyon: Optional[DateTime] = None
    garanti_suresi: Optional[String] = None
    bagimli_yil: Optional[Float] = None
    bagimli_ay: Optional[Float] = None
    bagimli_siparis_no: Optional[Float] = None
    icerik: Optional[String] = None
    iade_no: Optional[String] = None
    gizli: Optional[Integer] = None
    irsaliye_no: Optional[String] = None
    siparis_bayi_kodu: Optional[Integer] = None
    baski_sayisi: Optional[String] = None
    sip_iade_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None


class AlinanSiparisCreate(AlinanSiparisBase):
    pass


class AlinanSiparis(AlinanSiparisBase):
    id: Optional[int]

    class Config:
        orm_mode = True
