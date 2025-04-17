from pydantic import BaseModel
from typing import Optional

class GirisKaliteDetayBase(BaseModel):
    yil: Optional[Float] = None
    giris_no: Optional[Integer] = None
    kayit_no: Optional[Float] = None
    miktar_kontrol: Optional[Float] = None
    miktar_numune: Optional[Float] = None
    miktar_kabul: Optional[Float] = None
    miktar_sartli: Optional[Float] = None
    miktar_red: Optional[Float] = None
    uygunsuzluk_raporu: Optional[Float] = None
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GirisKaliteDetayCreate(GirisKaliteDetayBase):
    pass

class GirisKaliteDetay(GirisKaliteDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True