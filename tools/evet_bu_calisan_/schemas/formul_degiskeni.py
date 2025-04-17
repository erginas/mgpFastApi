from pydantic import BaseModel
from typing import Optional

class FormulDegiskeniBase(BaseModel):
    kodu: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class FormulDegiskeniCreate(FormulDegiskeniBase):
    pass

class FormulDegiskeni(FormulDegiskeniBase):
    id: Optional[int]

    class Config:
        orm_mode = True