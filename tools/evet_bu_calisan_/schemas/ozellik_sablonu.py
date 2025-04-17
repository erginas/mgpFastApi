from pydantic import BaseModel
from typing import Optional

class OzellikSablonuBase(BaseModel):
    grup_no: Optional[Integer] = None
    ozellik_sinif_kodu: Optional[Float] = None
    gosterim_sirasi: Optional[Integer] = None
    stok_kod_sirasi: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class OzellikSablonuCreate(OzellikSablonuBase):
    pass

class OzellikSablonu(OzellikSablonuBase):
    id: Optional[int]

    class Config:
        orm_mode = True