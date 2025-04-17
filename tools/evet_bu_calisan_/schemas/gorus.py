from pydantic import BaseModel
from typing import Optional

class GorusBase(BaseModel):
    sira_no: Optional[Integer] = None
    kullanildigi_yer_fl: Optional[String] = None
    aciklama: Optional[String] = None
    grup_kodu: Optional[String] = None
    bagimli_sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GorusCreate(GorusBase):
    pass

class Gorus(GorusBase):
    id: Optional[int]

    class Config:
        orm_mode = True