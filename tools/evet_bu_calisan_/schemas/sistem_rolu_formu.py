from pydantic import BaseModel
from typing import Optional

class SistemRoluFormuBase(BaseModel):
    sistem_rol_no: Optional[Integer] = None
    menu_kodu: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SistemRoluFormuCreate(SistemRoluFormuBase):
    pass

class SistemRoluFormu(SistemRoluFormuBase):
    id: Optional[int]

    class Config:
        orm_mode = True