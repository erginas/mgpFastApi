from pydantic import BaseModel
from typing import Optional

class ResimOlcusuBase(BaseModel):
    resim_olcu_id: Optional[String] = None
    adi: Optional[String] = None
    olcum_turu: Optional[String] = None
    ust_limit: Optional[Float] = None
    alt_limit: Optional[Float] = None
    esas_olcu: Optional[Float] = None
    aciklama: Optional[String] = None
    teknik_resim_id: Optional[String] = None
    teknik_resim_kapsam_id: Optional[String] = None
    kritik_fl: Optional[String] = None
    malzemeye_ozgu_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ResimOlcusuCreate(ResimOlcusuBase):
    pass

class ResimOlcusu(ResimOlcusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True