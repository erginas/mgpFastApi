from pydantic import BaseModel
from typing import Optional

class OzgecmisBase(BaseModel):
    kimlik_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kaydeden: Optional[Float] = None
    turu: Optional[String] = None
    bilgi: Optional[String] = None
    baslama_t: Optional[DateTime] = None
    bitis_t: Optional[DateTime] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class OzgecmisCreate(OzgecmisBase):
    pass

class Ozgecmis(OzgecmisBase):
    id: Optional[int]

    class Config:
        orm_mode = True