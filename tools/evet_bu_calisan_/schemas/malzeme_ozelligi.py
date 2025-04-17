from pydantic import BaseModel
from typing import Optional

class MalzemeOzelligiBase(BaseModel):
    malzeme_no: Optional[Integer] = None
    ozellik_sinif_kodu: Optional[Float] = None
    ozellik: Optional[String] = None
    secenek_no: Optional[Float] = None
    etiket_sirasi: Optional[Float] = None
    sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemeOzelligiCreate(MalzemeOzelligiBase):
    pass

class MalzemeOzelligi(MalzemeOzelligiBase):
    id: Optional[int]

    class Config:
        orm_mode = True