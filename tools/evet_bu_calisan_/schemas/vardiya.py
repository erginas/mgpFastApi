from pydantic import BaseModel
from typing import Optional

class VardiyaBase(BaseModel):
    vardiya_no: Optional[Integer] = None
    adi: Optional[String] = None
    baslama_zamani: Optional[String] = None
    bitis_zamani: Optional[String] = None
    mola_1_baslama: Optional[String] = None
    mola_1_bitis: Optional[String] = None
    mola_2_baslama: Optional[String] = None
    mola_2_bitis: Optional[String] = None
    mola_3_baslama: Optional[String] = None
    mola_3_bitis: Optional[String] = None
    kaydeden: Optional[Float] = None
    kayit_zamani: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_zamani: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class VardiyaCreate(VardiyaBase):
    pass

class Vardiya(VardiyaBase):
    id: Optional[int]

    class Config:
        orm_mode = True