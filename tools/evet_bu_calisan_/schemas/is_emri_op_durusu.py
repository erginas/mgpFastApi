from pydantic import BaseModel
from typing import Optional

class IsEmriOpDurusuBase(BaseModel):
    baslama_z: Optional[DateTime] = None
    isemri_no: Optional[String] = None
    islem_sirasi: Optional[Float] = None
    durus_detay_kodu: Optional[Float] = None
    bitis_z: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriOpDurusuCreate(IsEmriOpDurusuBase):
    pass

class IsEmriOpDurusu(IsEmriOpDurusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True