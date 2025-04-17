from pydantic import BaseModel
from typing import Optional

class UtsTempBase(BaseModel):
    id: Optional[Integer] = None
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Integer] = None
    lot_no: Optional[String] = None
    miktar: Optional[Integer] = None
    uretim_tarihi: Optional[DateTime] = None
    bildirim_tipi: Optional[String] = None
    bildirim_no: Optional[String] = None
    bildirim_tarihi: Optional[DateTime] = None
    kaydeden_kimlik: Optional[Integer] = None
    iptal_eden: Optional[Integer] = None
    g_c: Optional[String] = None
    paket_no: Optional[String] = None
    iptal_tarihi: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    iptal_no: Optional[String] = None
    aciklama: Optional[String] = None
    parent_id: Optional[Integer] = None
    tekrar_bildir: Optional[Integer] = None
    bildirim_kodu: Optional[Integer] = None
    als_fatura_detay_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class UtsTempCreate(UtsTempBase):
    pass

class UtsTemp(UtsTempBase):
    id: Optional[int]

    class Config:
        orm_mode = True