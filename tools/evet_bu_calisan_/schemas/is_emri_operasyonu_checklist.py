from pydantic import BaseModel
from typing import Optional

class IsEmriOperasyonuChecklistBase(BaseModel):
    isemri_no: Optional[String] = None
    islem_sirasi: Optional[Float] = None
    sira_no: Optional[Integer] = None
    operasyon_no: Optional[Float] = None
    check_sira_no: Optional[Integer] = None
    olcu_kodu: Optional[Float] = None
    sk_plan_kodu: Optional[Float] = None
    paraf: Optional[String] = None
    aciklama: Optional[String] = None
    kimlik_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriOperasyonuChecklistCreate(IsEmriOperasyonuChecklistBase):
    pass

class IsEmriOperasyonuChecklist(IsEmriOperasyonuChecklistBase):
    id: Optional[int]

    class Config:
        orm_mode = True