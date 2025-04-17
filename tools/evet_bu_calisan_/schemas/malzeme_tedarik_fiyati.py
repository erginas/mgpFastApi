from pydantic import BaseModel
from typing import Optional

class MalzemeTedarikFiyatiBase(BaseModel):
    id: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    tedarik_tarihi: Optional[DateTime] = None
    islem_zamani: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeTedarikFiyatiCreate(MalzemeTedarikFiyatiBase):
    pass

class MalzemeTedarikFiyati(MalzemeTedarikFiyatiBase):
    id: Optional[int]

    class Config:
        orm_mode = True