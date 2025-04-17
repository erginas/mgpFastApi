from pydantic import BaseModel
from typing import Optional

class AlinanSiparisSevkiyatiBase(BaseModel):
    sevk_yil: Optional[Float] = None
    sevk_ay: Optional[Float] = None
    sevk_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    fiili_teslim_tarihi: Optional[DateTime] = None
    teslim_saati: Optional[String] = None
    gidis_sekli: Optional[String] = None
    tasiyici_firma: Optional[String] = None
    tasiyici_firma_referansi: Optional[String] = None
    irsaliye_no: Optional[String] = None
    fatura_no: Optional[String] = None
    aciklama: Optional[String] = None
    durumu: Optional[String] = None
    firma_kodu: Optional[Integer] = None
    birim_no: Optional[Integer] = None
    irs_fat_fl: Optional[Integer] = None
    hareket_kodu: Optional[Integer] = None
    otomatik_fl: Optional[Integer] = None
    iade_no: Optional[String] = None
    beyanname_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanSiparisSevkiyatiCreate(AlinanSiparisSevkiyatiBase):
    pass

class AlinanSiparisSevkiyati(AlinanSiparisSevkiyatiBase):
    id: Optional[int]

    class Config:
        orm_mode = True