from pydantic import BaseModel
from typing import Optional

class TerminDegisikligiBase(BaseModel):
    isemri_no: Optional[String] = None
    degistirilme_zamani: Optional[DateTime] = None
    kimlik_no: Optional[Float] = None
    eski_oncelik: Optional[String] = None
    eski_teslim_tarihi: Optional[DateTime] = None
    gerekce: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TerminDegisikligiCreate(TerminDegisikligiBase):
    pass

class TerminDegisikligi(TerminDegisikligiBase):
    id: Optional[int]

    class Config:
        orm_mode = True