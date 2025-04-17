from pydantic import BaseModel
from typing import Optional

class AktarFromUtsBase(BaseModel):
    ean: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    gmdn: Optional[Integer] = None
    brans_kodu: Optional[Integer] = None
    sut_kodu: Optional[String] = None
    takip_kapsm_durumu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AktarFromUtsCreate(AktarFromUtsBase):
    pass

class AktarFromUts(AktarFromUtsBase):
    id: Optional[int]

    class Config:
        orm_mode = True