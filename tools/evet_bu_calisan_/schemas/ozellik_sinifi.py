from pydantic import BaseModel
from typing import Optional

class OzellikSinifiBase(BaseModel):
    ozellik_sinif_kodu: Optional[Float] = None
    adi: Optional[String] = None
    secenek_sabit_fl: Optional[String] = None
    stok_kod_uzunlugu: Optional[Integer] = None
    eski_kod: Optional[String] = None
    gezgin_sirasi: Optional[Float] = None
    siniflandirma_bitti: Optional[String] = None
    siniflandirma_kodlu: Optional[String] = None
    otomatik_aktar: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class OzellikSinifiCreate(OzellikSinifiBase):
    pass

class OzellikSinifi(OzellikSinifiBase):
    id: Optional[int]

    class Config:
        orm_mode = True