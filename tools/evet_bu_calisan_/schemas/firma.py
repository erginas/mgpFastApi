from pydantic import BaseModel
from typing import Optional

class FirmaBase(BaseModel):
    firma_kodu: Optional[Integer] = None
    unvani: Optional[String] = None
    adresi: Optional[String] = None
    tel: Optional[String] = None
    fax: Optional[String] = None
    eposta: Optional[String] = None
    url: Optional[String] = None
    ic_dis_fl: Optional[String] = None
    satici_fl: Optional[String] = None
    alici_fl: Optional[String] = None
    bayi_fl: Optional[String] = None
    vergi_dairesi: Optional[String] = None
    vergi_no: Optional[String] = None
    kisa_kodu: Optional[String] = None
    ulke: Optional[String] = None
    onay_t: Optional[DateTime] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    kimlik_no: Optional[Float] = None
    ilgili_kisi: Optional[String] = None
    cari_kodu: Optional[String] = None
    il: Optional[String] = None
    ilce: Optional[String] = None
    uts_tanimlayici_no: Optional[String] = None
    uts_unvan: Optional[String] = None
    uts_durum: Optional[String] = None
    uts_mersis_no: Optional[String] = None
    uts_ckys_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class FirmaCreate(FirmaBase):
    pass

class Firma(FirmaBase):
    id: Optional[int]

    class Config:
        orm_mode = True