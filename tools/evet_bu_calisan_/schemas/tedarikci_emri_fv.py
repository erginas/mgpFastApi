from pydantic import BaseModel
from typing import Optional

class TedarikciEmriFvBase(BaseModel):
    fas_yil: Optional[Integer] = None
    fas_ay: Optional[Integer] = None
    fas_no: Optional[Integer] = None
    kimlik_no: Optional[Integer] = None
    renk_kodu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TedarikciEmriFvCreate(TedarikciEmriFvBase):
    pass

class TedarikciEmriFv(TedarikciEmriFvBase):
    id: Optional[int]

    class Config:
        orm_mode = True