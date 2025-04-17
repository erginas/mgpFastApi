from pydantic import BaseModel
from typing import Optional

class ResimGrubuBase(BaseModel):
    resim_grubu: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ResimGrubuCreate(ResimGrubuBase):
    pass

class ResimGrubu(ResimGrubuBase):
    id: Optional[int]

    class Config:
        orm_mode = True