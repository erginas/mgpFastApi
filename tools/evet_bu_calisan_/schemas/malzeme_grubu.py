from pydantic import BaseModel
from typing import Optional

class MalzemeGrubuBase(BaseModel):
    grup_no: Optional[Integer] = None
    ust_grup_no: Optional[Integer] = None
    adi: Optional[String] = None
    temel_stok_kodu: Optional[String] = None
    malzeme_tipi: Optional[String] = None
    is_leaf: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeGrubuCreate(MalzemeGrubuBase):
    pass

class MalzemeGrubu(MalzemeGrubuBase):
    id: Optional[int]

    class Config:
        orm_mode = True