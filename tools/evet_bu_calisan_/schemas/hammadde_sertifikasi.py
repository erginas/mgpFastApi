from pydantic import BaseModel
from typing import Optional

class HammaddeSertifikasiBase(BaseModel):
    sertifika_no: Optional[String] = None
    goruntu: Optional[String] = None
    malzeme_bilgisi: Optional[String] = None
    tipi: Optional[String] = None
    id: Optional[Integer] = None
    file_backup: Optional[Integer] = None
    dosya_yolu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class HammaddeSertifikasiCreate(HammaddeSertifikasiBase):
    pass

class HammaddeSertifikasi(HammaddeSertifikasiBase):
    id: Optional[int]

    class Config:
        orm_mode = True