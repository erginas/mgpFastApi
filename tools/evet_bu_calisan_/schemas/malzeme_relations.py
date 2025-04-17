from pydantic import BaseModel
from typing import Optional

class MalzemeRelationsBase(BaseModel):
    id: Optional[Integer] = None
    parent_id: Optional[Integer] = None
    grup_adi: Optional[String] = None
    temel_stok_kodu: Optional[String] = None
    tipi: Optional[String] = None
    pasif: Optional[Float] = None
    ortak_grup: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeRelationsCreate(MalzemeRelationsBase):
    pass

class MalzemeRelations(MalzemeRelationsBase):
    id: Optional[int]

    class Config:
        orm_mode = True