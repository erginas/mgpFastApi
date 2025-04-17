from pydantic import BaseModel
from typing import Optional

class TakipliKonuBase(BaseModel):
    takip_yil: Optional[Float] = None
    takip_ay: Optional[Float] = None
    takip_no: Optional[Float] = None
    cesidi: Optional[String] = None
    yoneten_kimlik: Optional[Float] = None
    cozen_kimlik: Optional[Float] = None
    sorumlu_birim: Optional[Integer] = None
    sorunlu_birim: Optional[Integer] = None
    bagimli_takip_yil: Optional[Float] = None
    bagimli_takip_ay: Optional[Float] = None
    bagimli_takip: Optional[Float] = None
    bagimli_cesidi: Optional[String] = None
    aciklama: Optional[String] = None
    durumu: Optional[String] = None
    ilk_termin: Optional[DateTime] = None
    gecerli_termin: Optional[DateTime] = None
    cozum: Optional[String] = None
    referans: Optional[String] = None
    acilma_tarihi: Optional[DateTime] = None
    kapanma_tarihi: Optional[DateTime] = None
    oncelik: Optional[String] = None
    toplanti_yil: Optional[Float] = None
    toplanti_no: Optional[Float] = None
    kisa_konu: Optional[String] = None
    cozumleme_tarihi: Optional[DateTime] = None
    sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TakipliKonuCreate(TakipliKonuBase):
    pass

class TakipliKonu(TakipliKonuBase):
    id: Optional[int]

    class Config:
        orm_mode = True