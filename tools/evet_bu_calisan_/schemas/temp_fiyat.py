from pydantic import BaseModel
from typing import Optional

class TempFiyatBase(BaseModel):
    stok_kodu: Optional[String] = None
    fiyat: Optional[Integer] = None
    opsn_0: Optional[Integer] = None
    opsn_700: Optional[Integer] = None
    opsn_780: Optional[Integer] = None
    opsn_800: Optional[Integer] = None
    opsn_810: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TempFiyatCreate(TempFiyatBase):
    pass

class TempFiyat(TempFiyatBase):
    id: Optional[int]

    class Config:
        orm_mode = True