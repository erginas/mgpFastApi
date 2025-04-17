from pydantic import BaseModel
from typing import Optional

class AtamaBase(BaseModel):
    kadro_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    atayan: Optional[Float] = None
    azleden: Optional[Float] = None
    atanma_t: Optional[DateTime] = None
    azil_t: Optional[DateTime] = None
    atama_durumu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AtamaCreate(AtamaBase):
    pass

class Atama(AtamaBase):
    id: Optional[int]

    class Config:
        orm_mode = True