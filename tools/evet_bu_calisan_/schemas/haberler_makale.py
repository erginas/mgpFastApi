from pydantic import BaseModel
from typing import Optional

class HaberlerMakaleBase(BaseModel):
    id: Optional[Float] = None
    yazar: Optional[String] = None
    baslik: Optional[String] = None
    aciklama: Optional[String] = None
    metin: Optional[String] = None
    sehir: Optional[String] = None
    yayinlanma_tarihi: Optional[DateTime] = None
    aktif: Optional[Float] = None
    yaratilma_tarihi: Optional[DateTime] = None
    guncelleme_tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class HaberlerMakaleCreate(HaberlerMakaleBase):
    pass

class HaberlerMakale(HaberlerMakaleBase):
    id: Optional[int]

    class Config:
        orm_mode = True