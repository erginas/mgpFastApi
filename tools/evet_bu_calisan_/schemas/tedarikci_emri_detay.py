from pydantic import BaseModel
from typing import Optional

class TedarikciEmriDetayBase(BaseModel):
    fason_yil: Optional[Float] = None
    fason_ay: Optional[Float] = None
    fason_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    miktar: Optional[Float] = None
    oncelik: Optional[String] = None
    kayit_tarihi: Optional[DateTime] = None
    giris_cikis_fl: Optional[String] = None
    talep_tarihi: Optional[DateTime] = None
    gerekce: Optional[Float] = None
    aciklama: Optional[String] = None
    iptal_tarihi: Optional[DateTime] = None
    kimlik_no: Optional[Float] = None
    onerilen_tarih: Optional[DateTime] = None
    kesinlesen_tarih: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    iptal_eden: Optional[Float] = None
    kapandi_fl: Optional[String] = None
    kapanma_nedeni: Optional[String] = None
    siparis_sevk_tarihi: Optional[DateTime] = None
    sevk_miktari: Optional[Float] = None
    siparis_edilen_miktar: Optional[Float] = None
    siparis_teslim_tarihi: Optional[DateTime] = None
    stok_kodu: Optional[String] = None
    opsn: Optional[String] = None
    malzeme_adi: Optional[String] = None
    lot_no: Optional[String] = None
    materyal: Optional[String] = None
    ce_bilgisi: Optional[String] = None
    ambalaj: Optional[String] = None
    etiket: Optional[String] = None
    markalama: Optional[String] = None
    kontrol_lot_no: Optional[String] = None
    birim_fiyati: Optional[Integer] = None
    para_birimi: Optional[String] = None
    isemri_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TedarikciEmriDetayCreate(TedarikciEmriDetayBase):
    pass

class TedarikciEmriDetay(TedarikciEmriDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True