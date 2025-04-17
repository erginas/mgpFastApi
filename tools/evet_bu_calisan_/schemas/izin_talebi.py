from pydantic import BaseModel
from typing import Optional

class IzinTalebiBase(BaseModel):
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    kayit_zamani: Optional[DateTime] = None
    sebep_kodu: Optional[Integer] = None
    baslama_zamani: Optional[DateTime] = None
    izin_suresi: Optional[Integer] = None
    bitis_zamani: Optional[DateTime] = None
    izin_veren: Optional[Float] = None
    fiili_kayit_zamani: Optional[DateTime] = None
    fiili_giris_zamani: Optional[DateTime] = None
    fiili_sure: Optional[Integer] = None
    fiili_cikis_zamani: Optional[DateTime] = None
    onaylayan: Optional[Float] = None
    izin_durumu: Optional[String] = None
    izin_sure_tipi: Optional[String] = None
    fiili_sure_tipi: Optional[String] = None
    aciklama: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_zamani: Optional[DateTime] = None
    izin_nedeni: Optional[String] = None
    vardiya_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class IzinTalebiCreate(IzinTalebiBase):
    pass

class IzinTalebi(IzinTalebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True