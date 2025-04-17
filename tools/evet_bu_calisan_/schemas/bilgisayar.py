from pydantic import BaseModel
from typing import Optional

class BilgisayarBase(BaseModel):
    sira_no: Optional[String] = None
    birim_no: Optional[Integer] = None
    ip_no: Optional[String] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class BilgisayarCreate(BilgisayarBase):
    pass

class Bilgisayar(BilgisayarBase):
    id: Optional[int]

    class Config:
        orm_mode = True