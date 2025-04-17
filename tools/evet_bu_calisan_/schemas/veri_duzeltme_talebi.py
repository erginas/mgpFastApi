from pydantic import BaseModel
from typing import Optional

class VeriDuzeltmeTalebiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    veri_no: Optional[Float] = None
    kayit_yili: Optional[Float] = None
    kayit_no: Optional[Float] = None
    hata_sebebi: Optional[String] = None
    yapilacak_islem: Optional[String] = None
    duzenleyen: Optional[Float] = None
    duzenleme_t: Optional[DateTime] = None
    onaylayan: Optional[Float] = None
    onaylama_t: Optional[DateTime] = None
    duzelten: Optional[Float] = None
    duzeltme_t: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class VeriDuzeltmeTalebiCreate(VeriDuzeltmeTalebiBase):
    pass

class VeriDuzeltmeTalebi(VeriDuzeltmeTalebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True