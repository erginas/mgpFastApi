from pydantic import BaseModel
from typing import Optional

class UygunsuzlukSorumlusuBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    karar_no: Optional[Float] = None
    sorumlu_no: Optional[Float] = None
    hata_no: Optional[Float] = None
    adet: Optional[Float] = None
    hatayi_yapan: Optional[String] = None
    kimlik_no: Optional[Float] = None
    firma_kodu: Optional[Integer] = None
    tezgah_no: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukSorumlusuCreate(UygunsuzlukSorumlusuBase):
    pass

class UygunsuzlukSorumlusu(UygunsuzlukSorumlusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True