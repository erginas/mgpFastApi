from pydantic import BaseModel
from typing import Optional

class AaUtsBase(BaseModel):
    uno: Optional[String] = None
    lno: Optional[String] = None
    lnoo: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AaUtsCreate(AaUtsBase):
    pass

class AaUts(AaUtsBase):
    id: Optional[int]

    class Config:
        orm_mode = True