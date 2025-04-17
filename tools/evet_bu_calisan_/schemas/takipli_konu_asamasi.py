from pydantic import BaseModel
from typing import Optional

class TakipliKonuAsamasiBase(BaseModel):
    takip_yil: Optional[Float] = None
    takip_ay: Optional[Float] = None
    takip_no: Optional[Float] = None
    cesidi: Optional[String] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    tarih: Optional[DateTime] = None
    aciklama: Optional[String] = None
    cozum_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TakipliKonuAsamasiCreate(TakipliKonuAsamasiBase):
    pass

class TakipliKonuAsamasi(TakipliKonuAsamasiBase):
    id: Optional[int]

    class Config:
        orm_mode = True