from pydantic import BaseModel
from typing import Optional

class ReceteBase(BaseModel):
    id: Optional[Integer] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    parent_id: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    onayli: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteCreate(ReceteBase):
    pass

class Recete(ReceteBase):
    id: Optional[int]

    class Config:
        orm_mode = True