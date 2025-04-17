from pydantic import BaseModel
from typing import Optional

class UygunsuzlukKarariBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    rapor_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    karar: Optional[String] = None
    miktar: Optional[Float] = None
    uygulanacak_islem: Optional[String] = None
    karar_no: Optional[Float] = None
    tedarikci_raporu: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    aciklama: Optional[String] = None
    etiket_basma_fl: Optional[String] = None
    etiket_malzeme_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UygunsuzlukKarariCreate(UygunsuzlukKarariBase):
    pass

class UygunsuzlukKarari(UygunsuzlukKarariBase):
    id: Optional[int]

    class Config:
        orm_mode = True