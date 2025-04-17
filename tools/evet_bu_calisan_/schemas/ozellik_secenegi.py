from pydantic import BaseModel
from typing import Optional

class OzellikSecenegiBase(BaseModel):
    ozellik_sinif_kodu: Optional[Float] = None
    secenek_no: Optional[Float] = None
    adi: Optional[String] = None
    tanim_parcasi: Optional[String] = None
    stok_kodu_parcasi: Optional[String] = None
    ust_secenek: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class OzellikSecenegiCreate(OzellikSecenegiBase):
    pass

class OzellikSecenegi(OzellikSecenegiBase):
    id: Optional[int]

    class Config:
        orm_mode = True