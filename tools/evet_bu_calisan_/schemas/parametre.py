from pydantic import BaseModel
from typing import Optional

class ParametreBase(BaseModel):
    parametre: Optional[String] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    kullanici_kodu: Optional[String] = None
    deger: Optional[String] = None
    blg_sira_no: Optional[String] = None
    property: Optional[String] = None
    opsiyon: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ParametreCreate(ParametreBase):
    pass

class Parametre(ParametreBase):
    id: Optional[int]

    class Config:
        orm_mode = True