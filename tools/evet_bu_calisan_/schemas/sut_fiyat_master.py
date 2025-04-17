from pydantic import BaseModel
from typing import Optional

class SutFiyatMasterBase(BaseModel):
    id: Optional[Integer] = None
    sut_tarihi: Optional[DateTime] = None
    aciklama: Optional[String] = None
    ozel_aciklama: Optional[String] = None
    aktif: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SutFiyatMasterCreate(SutFiyatMasterBase):
    pass

class SutFiyatMaster(SutFiyatMasterBase):
    id: Optional[int]

    class Config:
        orm_mode = True