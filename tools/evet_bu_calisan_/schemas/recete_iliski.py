from pydantic import BaseModel
from typing import Optional

class ReceteIliskiBase(BaseModel):
    ana_recete_id: Optional[Integer] = None
    iliskili_recete_id: Optional[Integer] = None
    detay_parent_id: Optional[Integer] = None
    detay_sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteIliskiCreate(ReceteIliskiBase):
    pass

class ReceteIliski(ReceteIliskiBase):
    id: Optional[int]

    class Config:
        orm_mode = True