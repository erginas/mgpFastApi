from pydantic import BaseModel
from typing import Optional

class PlanDonemiBase(BaseModel):
    donem_no: Optional[Float] = None
    baslama_t: Optional[DateTime] = None
    bitis_t: Optional[DateTime] = None
    aciklama: Optional[String] = None
    durum: Optional[String] = None
    surum: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class PlanDonemiCreate(PlanDonemiBase):
    pass

class PlanDonemi(PlanDonemiBase):
    id: Optional[int]

    class Config:
        orm_mode = True