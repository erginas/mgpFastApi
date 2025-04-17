from pydantic import BaseModel
from typing import Optional

class IsEmriOperasyonDurusuBase(BaseModel):
    islem_sirasi: Optional[Float] = None
    durus_detay_kodu: Optional[Float] = None
    frekans: Optional[Float] = None
    toplam_sure: Optional[Float] = None
    isemri_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriOperasyonDurusuCreate(IsEmriOperasyonDurusuBase):
    pass

class IsEmriOperasyonDurusu(IsEmriOperasyonDurusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True