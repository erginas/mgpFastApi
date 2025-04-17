from pydantic import BaseModel
from typing import Optional

class UrunAlternatifiBase(BaseModel):
    asama_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    temel_malzeme: Optional[Integer] = None
    nedeni: Optional[String] = None
    aciklama: Optional[String] = None
    giris_cikis_fl: Optional[String] = None
    miktar: Optional[Float] = None
    tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UrunAlternatifiCreate(UrunAlternatifiBase):
    pass

class UrunAlternatifi(UrunAlternatifiBase):
    id: Optional[int]

    class Config:
        orm_mode = True