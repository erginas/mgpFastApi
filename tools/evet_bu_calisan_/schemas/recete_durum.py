from pydantic import BaseModel
from typing import Optional

class ReceteDurumBase(BaseModel):
    id: Optional[Integer] = None
    durum_tipi: Optional[String] = None
    istem_tarihi: Optional[DateTime] = None
    birim_no: Optional[Integer] = None
    aciklama: Optional[String] = None
    recete_id: Optional[Integer] = None
    durumu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteDurumCreate(ReceteDurumBase):
    pass

class ReceteDurum(ReceteDurumBase):
    id: Optional[int]

    class Config:
        orm_mode = True