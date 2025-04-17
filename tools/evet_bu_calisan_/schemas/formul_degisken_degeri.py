from pydantic import BaseModel
from typing import Optional

class FormulDegiskenDegeriBase(BaseModel):
    kodu: Optional[String] = None
    gecerlilik_tarihi: Optional[DateTime] = None
    kimlik_no: Optional[Float] = None
    degeri: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class FormulDegiskenDegeriCreate(FormulDegiskenDegeriBase):
    pass

class FormulDegiskenDegeri(FormulDegiskenDegeriBase):
    id: Optional[int]

    class Config:
        orm_mode = True