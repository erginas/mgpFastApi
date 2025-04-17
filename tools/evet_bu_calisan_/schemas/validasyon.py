from pydantic import BaseModel
from typing import Optional

class ValidasyonBase(BaseModel):
    id: Optional[Float] = None
    yayin_tarihi: Optional[DateTime] = None
    modul_versiyon: Optional[Float] = None
    aciklama: Optional[String] = None
    degisiklik_tipi: Optional[Float] = None
    modul_id: Optional[Float] = None
    yayinlandi: Optional[Float] = None
    yayinlayan: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ValidasyonCreate(ValidasyonBase):
    pass

class Validasyon(ValidasyonBase):
    id: Optional[int]

    class Config:
        orm_mode = True