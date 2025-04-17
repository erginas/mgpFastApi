from pydantic import BaseModel
from typing import Optional

class KadroBase(BaseModel):
    kadro_no: Optional[Float] = None
    kisa_kodu: Optional[String] = None
    adi: Optional[String] = None
    birim_no: Optional[Integer] = None
    bagimli_kadro: Optional[Float] = None
    kaydeden: Optional[Float] = None
    kapatan: Optional[Float] = None
    acilma_z: Optional[DateTime] = None
    kapanma_z: Optional[DateTime] = None
    acik_kadro: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KadroCreate(KadroBase):
    pass

class Kadro(KadroBase):
    id: Optional[int]

    class Config:
        orm_mode = True