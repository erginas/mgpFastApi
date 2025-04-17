from pydantic import BaseModel
from typing import Optional

class FirmaDegerlendirmesiBase(BaseModel):
    firma_kodu: Optional[Integer] = None
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    kriter_no: Optional[Float] = None
    degeri: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class FirmaDegerlendirmesiCreate(FirmaDegerlendirmesiBase):
    pass

class FirmaDegerlendirmesi(FirmaDegerlendirmesiBase):
    id: Optional[int]

    class Config:
        orm_mode = True