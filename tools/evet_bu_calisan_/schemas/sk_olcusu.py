from pydantic import BaseModel
from typing import Optional

class SkOlcusuBase(BaseModel):
    olcu_kodu: Optional[Float] = None
    adi: Optional[String] = None
    tipi: Optional[String] = None
    kontrol_grubu: Optional[String] = None
    control_group: Optional[String] = None
    name: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SkOlcusuCreate(SkOlcusuBase):
    pass

class SkOlcusu(SkOlcusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True