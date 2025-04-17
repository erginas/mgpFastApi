from pydantic import BaseModel
from typing import Optional

class AlinanSiparisTeslimiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    teslim_sira_no: Optional[Integer] = None
    fiili_teslim_tarihi: Optional[DateTime] = None
    teslim_saati: Optional[String] = None
    gidis_sekli: Optional[String] = None
    tasiyici_firma: Optional[String] = None
    tasiyici_firma_ref: Optional[String] = None
    sevk_irsaliyesi: Optional[String] = None
    fatura_no: Optional[String] = None
    aciklama: Optional[String] = None
    kimlik_no: Optional[Float] = None
    irsaliye_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanSiparisTeslimiCreate(AlinanSiparisTeslimiBase):
    pass

class AlinanSiparisTeslimi(AlinanSiparisTeslimiBase):
    id: Optional[int]

    class Config:
        orm_mode = True