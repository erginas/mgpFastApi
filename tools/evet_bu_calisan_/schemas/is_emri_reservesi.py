from pydantic import BaseModel
from typing import Optional

class IsEmriReservesiBase(BaseModel):
    isemri_no: Optional[String] = None
    sira_no: Optional[Integer] = None
    yil: Optional[Float] = None
    fis_no: Optional[Float] = None
    miktar_reserve: Optional[Float] = None
    aciklama: Optional[String] = None
    kaydeden: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_z: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ue_sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriReservesiCreate(IsEmriReservesiBase):
    pass

class IsEmriReservesi(IsEmriReservesiBase):
    id: Optional[int]

    class Config:
        orm_mode = True