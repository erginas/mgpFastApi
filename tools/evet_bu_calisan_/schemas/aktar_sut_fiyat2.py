from pydantic import BaseModel
from typing import Optional

class AktarSutFiyat2Base(BaseModel):
    sut_kodu: Optional[String] = None
    fiyat: Optional[Integer] = None
    iskonto: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    ean: Optional[String] = None
    gecerlik_tarihi: Optional[DateTime] = None
    malzeme_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AktarSutFiyat2Create(AktarSutFiyat2Base):
    pass

class AktarSutFiyat2(AktarSutFiyat2Base):
    id: Optional[int]

    class Config:
        orm_mode = True