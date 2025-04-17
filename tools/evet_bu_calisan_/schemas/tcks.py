from pydantic import BaseModel
from typing import Optional

class TcksBase(BaseModel):
    bm_sk: Optional[String] = None
    bm_tanim: Optional[String] = None
    bm_yeni_tanim: Optional[String] = None
    bm_ozellik: Optional[String] = None
    tp_sk: Optional[String] = None
    tp_tanim: Optional[String] = None
    tp_etiket: Optional[String] = None
    ems_kodu: Optional[String] = None
    gmdn_kategori: Optional[Float] = None
    gmdn_bolum: Optional[Float] = None
    gmdn_kod: Optional[Float] = None
    tp_katalog: Optional[String] = None
    bm_tp_tanim: Optional[String] = None
    ems_sira: Optional[Float] = None
    liste_disi: Optional[String] = None
    gmdn: Optional[String] = None
    ce_sinifi: Optional[String] = None
    bm_durum: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TcksCreate(TcksBase):
    pass

class Tcks(TcksBase):
    id: Optional[int]

    class Config:
        orm_mode = True