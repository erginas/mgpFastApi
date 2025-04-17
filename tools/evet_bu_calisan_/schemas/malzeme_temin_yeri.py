from pydantic import BaseModel
from typing import Optional

class MalzemeTeminYeriBase(BaseModel):
    temin_sekil_kodu: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    kimlik_no: Optional[Float] = None
    sertifika_sira_no: Optional[Integer] = None
    iptal_eden: Optional[Float] = None
    tedarikci_kodu: Optional[String] = None
    tahmini_temin_suresi: Optional[Float] = None
    min_temin_miktari: Optional[Float] = None
    kayit_tarihi: Optional[DateTime] = None
    iptal_tarihi: Optional[DateTime] = None
    oncelik: Optional[Float] = None
    marka: Optional[String] = None
    aciklama: Optional[String] = None
    iptal_nedeni: Optional[String] = None
    eko_temin_miktari: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemeTeminYeriCreate(MalzemeTeminYeriBase):
    pass

class MalzemeTeminYeri(MalzemeTeminYeriBase):
    id: Optional[int]

    class Config:
        orm_mode = True