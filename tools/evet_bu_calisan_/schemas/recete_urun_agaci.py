from pydantic import BaseModel
from typing import Optional

class ReceteUrunAgaciBase(BaseModel):
    id: Optional[Integer] = None
    recete_id: Optional[Integer] = None
    recete_detay_id: Optional[Integer] = None
    adi: Optional[String] = None
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    miktar: Optional[Float] = None
    birim: Optional[String] = None
    boy: Optional[Float] = None
    en: Optional[Float] = None
    cap: Optional[Float] = None
    sira_no: Optional[Integer] = None
    parent_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteUrunAgaciCreate(ReceteUrunAgaciBase):
    pass

class ReceteUrunAgaci(ReceteUrunAgaciBase):
    id: Optional[int]

    class Config:
        orm_mode = True