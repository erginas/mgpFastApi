from pydantic import BaseModel
from typing import Optional

class TedarikciEmriBase(BaseModel):
    fason_yil: Optional[Float] = None
    fason_no: Optional[Float] = None
    firma_kodu: Optional[Integer] = None
    duzenleyen_kimlik: Optional[Float] = None
    onaylayan_kimlik: Optional[Float] = None
    ilgili_kisi: Optional[String] = None
    duzenleme_z: Optional[DateTime] = None
    istenen_termin: Optional[DateTime] = None
    termin_t: Optional[DateTime] = None
    yollama_t: Optional[DateTime] = None
    donus_t: Optional[DateTime] = None
    aciklama: Optional[String] = None
    iptal_tarihi: Optional[DateTime] = None
    onerilen_termin: Optional[DateTime] = None
    fason_ay: Optional[Float] = None
    emir_tipi: Optional[String] = None
    siparis_ref_no: Optional[String] = None
    kapandi_fl: Optional[String] = None
    lot_fl: Optional[String] = None
    iptal_eden: Optional[Float] = None
    iptal_nedeni: Optional[String] = None
    kontrol_eden: Optional[Float] = None
    onay_tarihi: Optional[DateTime] = None
    kontrol_tarihi: Optional[DateTime] = None
    siparis_ay: Optional[Float] = None
    siparis_yil: Optional[Float] = None
    siparis_no: Optional[Float] = None
    irsaliye_no: Optional[String] = None
    sertifia_no: Optional[String] = None
    durumu: Optional[String] = None
    satinalma_birimi: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TedarikciEmriCreate(TedarikciEmriBase):
    pass

class TedarikciEmri(TedarikciEmriBase):
    id: Optional[int]

    class Config:
        orm_mode = True