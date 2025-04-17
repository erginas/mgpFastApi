from pydantic import BaseModel
from typing import Optional

class TmpResimOlcusuBase(BaseModel):
    resim_olcu_id: Optional[String] = None
    adi: Optional[String] = None
    olcum_turu: Optional[String] = None
    ust_limit: Optional[Float] = None
    alt_limit: Optional[Float] = None
    esas_olcu: Optional[Float] = None
    aciklama: Optional[String] = None
    teknik_resim_id: Optional[String] = None
    teknik_resim_kapsam_id: Optional[String] = None
    kritik_fl: Optional[String] = None
    malzemeye_ozgu_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TmpResimOlcusuCreate(TmpResimOlcusuBase):
    pass

class TmpResimOlcusu(TmpResimOlcusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True