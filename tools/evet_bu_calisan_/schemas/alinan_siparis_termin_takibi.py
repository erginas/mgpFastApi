from pydantic import BaseModel
from typing import Optional

class AlinanSiparisTerminTakibiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    termin_tipi: Optional[String] = None
    termin_tarihi: Optional[DateTime] = None
    is_gunu: Optional[String] = None
    aciklama: Optional[String] = None
    kaydeden: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_nedeni: Optional[String] = None
    iptal_z: Optional[DateTime] = None
    tolerans: Optional[String] = None
    gun_opsiyonu: Optional[Float] = None
    gonderilme_z: Optional[DateTime] = None
    birim_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanSiparisTerminTakibiCreate(AlinanSiparisTerminTakibiBase):
    pass

class AlinanSiparisTerminTakibi(AlinanSiparisTerminTakibiBase):
    id: Optional[int]

    class Config:
        orm_mode = True