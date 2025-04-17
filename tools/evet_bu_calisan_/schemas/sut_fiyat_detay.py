from pydantic import BaseModel
from typing import Optional

class SutFiyatDetayBase(BaseModel):
    id: Optional[Integer] = None
    gecerlik_tarihi: Optional[DateTime] = None
    sut_kodu: Optional[String] = None
    ean: Optional[String] = None
    stok_kodu: Optional[String] = None
    fiyat: Optional[Integer] = None
    iskonto: Optional[Integer] = None
    aciklama: Optional[String] = None
    aktif: Optional[String] = None
    islem_zamani: Optional[DateTime] = None
    s_fiyat_master_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SutFiyatDetayCreate(SutFiyatDetayBase):
    pass

class SutFiyatDetay(SutFiyatDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True