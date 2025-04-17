from pydantic import BaseModel
from typing import Optional

class UrunGrubuBase(BaseModel):
    urun_grup_no: Optional[Float] = None
    ust_grup: Optional[Float] = None
    adi: Optional[String] = None
    grup_kodu: Optional[String] = None
    analiz_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UrunGrubuCreate(UrunGrubuBase):
    pass

class UrunGrubu(UrunGrubuBase):
    id: Optional[int]

    class Config:
        orm_mode = True