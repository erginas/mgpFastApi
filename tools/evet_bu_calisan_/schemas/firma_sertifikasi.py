from pydantic import BaseModel
from typing import Optional

class FirmaSertifikasiBase(BaseModel):
    sira_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    sertifika_no: Optional[String] = None
    gecerlilik_tarihi: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    kaydeden: Optional[Float] = None
    cinsi: Optional[String] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    sinifi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class FirmaSertifikasiCreate(FirmaSertifikasiBase):
    pass

class FirmaSertifikasi(FirmaSertifikasiBase):
    id: Optional[int]

    class Config:
        orm_mode = True