from pydantic import BaseModel
from typing import Optional

class ReceteTezgahBase(BaseModel):
    recete_detay_id: Optional[Integer] = None
    tezgah_grup_id: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    master_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteTezgahCreate(ReceteTezgahBase):
    pass

class ReceteTezgah(ReceteTezgahBase):
    id: Optional[int]

    class Config:
        orm_mode = True