from pydantic import BaseModel
from typing import Optional

class FazlaMesaiBase(BaseModel):
    mesai_kalan: Optional[Float] = None
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    sira_no: Optional[Integer] = None
    duzenleyen: Optional[Float] = None
    onaylayan: Optional[Float] = None
    duzenlenme_t: Optional[DateTime] = None
    istenen_baslama_t: Optional[DateTime] = None
    istenen_bitis_t: Optional[DateTime] = None
    istenen_sure: Optional[Integer] = None
    sure_tipi: Optional[String] = None
    neden: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    kontrol_eden: Optional[Float] = None
    kontrol_t: Optional[DateTime] = None
    fiili_baslama_t: Optional[DateTime] = None
    fiili_bitis_t: Optional[DateTime] = None
    fiili_sure: Optional[Integer] = None
    durumu: Optional[String] = None
    onay_t: Optional[DateTime] = None
    acil_siparis_fl: Optional[String] = None
    mesai_nedeni: Optional[String] = None
    birimi: Optional[String] = None
    dusulen_sure: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class FazlaMesaiCreate(FazlaMesaiBase):
    pass

class FazlaMesai(FazlaMesaiBase):
    id: Optional[int]

    class Config:
        orm_mode = True