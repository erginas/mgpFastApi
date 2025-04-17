from pydantic import BaseModel
from typing import Optional

class HareketSebebiBase(BaseModel):
    hareket_kodu: Optional[Float] = None
    adi: Optional[String] = None
    giris_cikis_fl: Optional[String] = None
    davranis_sekli: Optional[String] = None
    e_kodu: Optional[String] = None
    imza_ister_fl: Optional[String] = None
    class_name: Optional[String] = None
    karsi_hareket_kodu: Optional[Float] = None
    goster_fl: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class HareketSebebiCreate(HareketSebebiBase):
    pass

class HareketSebebi(HareketSebebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True