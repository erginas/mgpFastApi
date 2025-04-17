from pydantic import BaseModel
from typing import Optional

class ReceteMalzemeEksiklerBase(BaseModel):
    recete_detay_id: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    miktar: Optional[Integer] = None
    aciklama: Optional[String] = None
    sira_no: Optional[Float] = None
    detay_operasyon_no: Optional[String] = None
    detay_stok_kodu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ReceteMalzemeEksiklerCreate(ReceteMalzemeEksiklerBase):
    pass

class ReceteMalzemeEksikler(ReceteMalzemeEksiklerBase):
    id: Optional[int]

    class Config:
        orm_mode = True