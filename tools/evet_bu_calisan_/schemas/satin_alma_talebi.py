from pydantic import BaseModel
from typing import Optional

class SatinAlmaTalebiBase(BaseModel):
    satinalma_talep_id: Optional[String] = None
    firma_kodu: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    yil: Optional[Float] = None
    parti_no: Optional[Float] = None
    malzeme_adi: Optional[String] = None
    marka: Optional[String] = None
    miktar: Optional[Float] = None
    giris_cikis: Optional[Float] = None
    kayit_tarihi: Optional[DateTime] = None
    termin_tarihi: Optional[DateTime] = None
    onay_tarihi: Optional[DateTime] = None
    fatura_irsaliye_no: Optional[String] = None
    belge_tarihi: Optional[DateTime] = None
    birim_fiyat: Optional[Float] = None
    farkli_karsilama: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SatinAlmaTalebiCreate(SatinAlmaTalebiBase):
    pass

class SatinAlmaTalebi(SatinAlmaTalebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True