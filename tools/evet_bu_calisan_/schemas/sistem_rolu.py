from pydantic import BaseModel
from typing import Optional

class SistemRoluBase(BaseModel):
    sistem_rol_no: Optional[Integer] = None
    adi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SistemRoluCreate(SistemRoluBase):
    pass

class SistemRolu(SistemRoluBase):
    id: Optional[int]

    class Config:
        orm_mode = True