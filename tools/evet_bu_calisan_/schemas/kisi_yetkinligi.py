from pydantic import BaseModel
from typing import Optional

class KisiYetkinligiBase(BaseModel):
    kimlik_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kaydeden: Optional[Float] = None
    yetkinlik_no: Optional[Float] = None
    baslama_t: Optional[DateTime] = None
    bitis_t: Optional[DateTime] = None
    seviye: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KisiYetkinligiCreate(KisiYetkinligiBase):
    pass

class KisiYetkinligi(KisiYetkinligiBase):
    id: Optional[int]

    class Config:
        orm_mode = True