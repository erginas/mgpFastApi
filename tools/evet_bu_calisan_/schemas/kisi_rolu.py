from pydantic import BaseModel
from typing import Optional

class KisiRoluBase(BaseModel):
    sistem_rol_no: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    eklendigi_tarih: Optional[DateTime] = None
    ciktigi_tarih: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class KisiRoluCreate(KisiRoluBase):
    pass

class KisiRolu(KisiRoluBase):
    id: Optional[int]

    class Config:
        orm_mode = True