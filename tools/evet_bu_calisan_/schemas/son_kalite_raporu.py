from pydantic import BaseModel
from typing import Optional

class SonKaliteRaporuBase(BaseModel):
    rapor_tarihi: Optional[DateTime] = None
    sira_no: Optional[Integer] = None
    isemri_no: Optional[String] = None
    duzenleyen: Optional[Float] = None
    miktar_kontrol: Optional[Float] = None
    miktar_kabul: Optional[Float] = None
    miktar_sartli_kabul: Optional[Float] = None
    miktar_red: Optional[Float] = None
    sk_plan_kodu: Optional[Float] = None
    baski_sayisi: Optional[Float] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    iptal_eden: Optional[Float] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SonKaliteRaporuCreate(SonKaliteRaporuBase):
    pass

class SonKaliteRaporu(SonKaliteRaporuBase):
    id: Optional[int]

    class Config:
        orm_mode = True