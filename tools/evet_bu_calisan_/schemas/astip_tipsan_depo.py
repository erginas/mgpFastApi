from pydantic import BaseModel
from typing import Optional

class AstipTipsanDepoBase(BaseModel):
    malzeme_no: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    malzeme_adi: Optional[String] = None
    lot_no: Optional[String] = None
    siparis_yil: Optional[Float] = None
    siparis_ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    siparis_sira_no: Optional[Integer] = None
    sip_no: Optional[String] = None
    ce_bilgisi: Optional[String] = None
    son_kullanma_t: Optional[DateTime] = None
    miktar: Optional[Integer] = None
    irs_fat: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AstipTipsanDepoCreate(AstipTipsanDepoBase):
    pass

class AstipTipsanDepo(AstipTipsanDepoBase):
    id: Optional[int]

    class Config:
        orm_mode = True