from pydantic import BaseModel
from typing import Optional

class ReceteMalzemeBase(BaseModel):
    recete_detay_id: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    miktar: Optional[Integer] = None
    aciklama: Optional[String] = None
    sira_no: Optional[Float] = None
    id: Optional[Integer] = None
    master_id: Optional[Integer] = None
    detay_stok_kodu: Optional[String] = None
    detay_operasyon_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteMalzemeCreate(ReceteMalzemeBase):
    pass

class ReceteMalzeme(ReceteMalzemeBase):
    id: Optional[int]

    class Config:
        orm_mode = True