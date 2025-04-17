from pydantic import BaseModel
from typing import Optional

class TeknikResimKapsamiBase(BaseModel):
    teknik_resim_kapsam_id: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    teknik_resim_id: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TeknikResimKapsamiCreate(TeknikResimKapsamiBase):
    pass

class TeknikResimKapsami(TeknikResimKapsamiBase):
    id: Optional[int]

    class Config:
        orm_mode = True