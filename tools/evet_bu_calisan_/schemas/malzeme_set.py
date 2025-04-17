from pydantic import BaseModel
from typing import Optional

class MalzemeSetBase(BaseModel):
    id: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    sira_no: Optional[Integer] = None
    set_stok_kodu: Optional[String] = None
    set_adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeSetCreate(MalzemeSetBase):
    pass

class MalzemeSet(MalzemeSetBase):
    id: Optional[int]

    class Config:
        orm_mode = True