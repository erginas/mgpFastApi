from pydantic import BaseModel
from typing import Optional

class UretimTalepDetayBase(BaseModel):
    fis_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    lot_no: Optional[String] = None
    miktar: Optional[Float] = None
    yapilacak_islem: Optional[String] = None
    yil: Optional[Float] = None
    miktar_talep: Optional[Float] = None
    tarih_talep: Optional[DateTime] = None
    miktar_is_emri: Optional[Float] = None
    aciklama: Optional[String] = None
    oncelik: Optional[String] = None
    miktar_iptal: Optional[Float] = None
    istenen_lot_no: Optional[String] = None
    istenen_malzeme_no: Optional[Integer] = None
    bekleme_sebebi: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    siparis_sira_no: Optional[Integer] = None
    iade_sira_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UretimTalepDetayCreate(UretimTalepDetayBase):
    pass

class UretimTalepDetay(UretimTalepDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True