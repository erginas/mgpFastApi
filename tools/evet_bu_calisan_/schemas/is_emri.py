from pydantic import BaseModel
from typing import Optional

class IsEmriBase(BaseModel):
    tanzim_eden: Optional[Float] = None
    teslim_alan: Optional[Float] = None
    lot_no: Optional[String] = None
    teslim_saati: Optional[String] = None
    talep_tarihi: Optional[DateTime] = None
    ek_bilgi: Optional[String] = None
    teslim_tarihi: Optional[DateTime] = None
    aciklama: Optional[String] = None
    is_emri_gerekcesi: Optional[String] = None
    ref_belge_no: Optional[String] = None
    oncelik: Optional[String] = None
    kk_rapor_no: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    miktar_talep: Optional[Float] = None
    miktar_uretim: Optional[Float] = None
    miktar_red: Optional[Float] = None
    baski_sayisi: Optional[Float] = None
    recete_no: Optional[Float] = None
    arsiv_fl: Optional[String] = None
    ue_fis_no: Optional[Float] = None
    ue_yil: Optional[Float] = None
    isemri_no: Optional[String] = None
    dogus_lotno: Optional[String] = None
    miktar_kabul: Optional[Float] = None
    miktar_sartli_kabul: Optional[Float] = None
    ue_sira_no: Optional[Integer] = None
    depo_kodu: Optional[Integer] = None
    urun_lotsuz: Optional[String] = None
    hareket_kodu: Optional[Float] = None
    kapanis_zamani: Optional[DateTime] = None
    durumu: Optional[String] = None
    ce_fl: Optional[Float] = None
    termin_tarihi: Optional[DateTime] = None
    iptal_kimlik: Optional[Float] = None
    iptal_zamani: Optional[DateTime] = None
    iptal_gerekcesi: Optional[String] = None
    grup_is_emri: Optional[String] = None
    siparis_no: Optional[String] = None
    uyg_yil: Optional[Float] = None
    uyg_ay: Optional[Float] = None
    uyg_rapor_no: Optional[Float] = None
    siparis_yil: Optional[Float] = None
    siparis_ay: Optional[Float] = None
    sip_siparis_no: Optional[Float] = None
    siparis_sira_no: Optional[Integer] = None
    kayit_no: Optional[Float] = None
    refakat_kart_no: Optional[String] = None
    miktar_reserve: Optional[Float] = None
    kayit_zamani: Optional[DateTime] = None
    iade_yil: Optional[Float] = None
    iade_ay: Optional[Float] = None
    iade_fis_no: Optional[Float] = None
    steril_fl: Optional[String] = None
    islem_merkezi_id: Optional[String] = None
    isemri_yil: Optional[Integer] = None
    tek_barkod: Optional[String] = None
    ce_resim_id: Optional[Integer] = None
    int_lot: Optional[Integer] = None
    uretim_tarihi: Optional[DateTime] = None
    recete_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None
    udi_human: Optional[String] = None
    udi_barcode: Optional[String] = None

class IsEmriCreate(IsEmriBase):
    pass

class IsEmri(IsEmriBase):
    id: Optional[int]

    class Config:
        orm_mode = True