from pydantic import BaseModel
from typing import Optional

class FirmaSiniflandirmasiBase(BaseModel):
    firma_kodu: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    sinifi: Optional[String] = None
    kayit_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class FirmaSiniflandirmasiCreate(FirmaSiniflandirmasiBase):
    pass

class FirmaSiniflandirmasi(FirmaSiniflandirmasiBase):
    id: Optional[int]

    class Config:
        orm_mode = True