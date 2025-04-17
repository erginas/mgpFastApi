from pydantic import BaseModel
from typing import Optional

class ReceteOperasyonuBase(BaseModel):
    recete_no: Optional[Float] = None
    kayit_no: Optional[Float] = None
    operasyon_no: Optional[Float] = None
    ozel_not: Optional[String] = None
    sira_no: Optional[Integer] = None
    resim_no: Optional[String] = None
    sure_formulu: Optional[String] = None
    parca: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    resim_grubu: Optional[String] = None
    tr_sira_no: Optional[String] = None
    grup_no: Optional[Float] = None
    kisa_kodu: Optional[String] = None
    fason_maliyeti: Optional[Float] = None
    kaydeden: Optional[Float] = None
    uretim_aciklamasi: Optional[String] = None
    kalite_aciklamasi: Optional[String] = None
    recete_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ReceteOperasyonuCreate(ReceteOperasyonuBase):
    pass

class ReceteOperasyonu(ReceteOperasyonuBase):
    id: Optional[int]

    class Config:
        orm_mode = True