from pydantic import BaseModel
from typing import Optional

class TpcCPropertiesBase(BaseModel):
    prop_name: Optional[String] = None
    prop_value: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TpcCPropertiesCreate(TpcCPropertiesBase):
    pass

class TpcCProperties(TpcCPropertiesBase):
    id: Optional[int]

    class Config:
        orm_mode = True