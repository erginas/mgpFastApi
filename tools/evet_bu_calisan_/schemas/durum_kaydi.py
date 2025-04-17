from pydantic import BaseModel
from typing import Optional

class DurumKaydiBase(BaseModel):
    key: Optional[String] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    durumu: Optional[String] = None
    tarih: Optional[DateTime] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DurumKaydiCreate(DurumKaydiBase):
    pass

class DurumKaydi(DurumKaydiBase):
    id: Optional[int]

    class Config:
        orm_mode = True