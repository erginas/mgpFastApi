from pydantic import BaseModel
from typing import Optional

class SkPlanOlcusuBase(BaseModel):
    olcu_kodu: Optional[Float] = None
    sk_plan_kodu: Optional[Float] = None
    sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SkPlanOlcusuCreate(SkPlanOlcusuBase):
    pass

class SkPlanOlcusu(SkPlanOlcusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True