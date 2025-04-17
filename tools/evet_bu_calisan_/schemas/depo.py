from pydantic import BaseModel
from typing import Optional

class DepoBase(BaseModel):
    depo_kodu: Optional[Integer] = None
    adi: Optional[String] = None
    e_kodu: Optional[String] = None
    rengi: Optional[Float] = None
    kisa_kodu: Optional[String] = None
    emniyet_stok_fl: Optional[String] = None
    davranis_sekli: Optional[Float] = None
    ce_bilgisi: Optional[String] = None
    uygunsuzluk_bilgisi: Optional[String] = None
    karsi_hareket: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DepoCreate(DepoBase):
    pass

class Depo(DepoBase):
    id: Optional[int]

    class Config:
        orm_mode = True