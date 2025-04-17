from pydantic import BaseModel
from typing import Optional

class OperasyonChecklistBase(BaseModel):
    operasyon_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kontrol_turu: Optional[String] = None
    kontrol_edilen: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class OperasyonChecklistCreate(OperasyonChecklistBase):
    pass

class OperasyonChecklist(OperasyonChecklistBase):
    id: Optional[int]

    class Config:
        orm_mode = True