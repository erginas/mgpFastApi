from pydantic import BaseModel
from typing import Optional

class AlinanSiparisDetayBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    teslim_sira_no: Optional[Integer] = None
    iade_yil: Optional[Float] = None
    iade_ay: Optional[Float] = None
    iade_fis_no: Optional[Float] = None
    kaydeden: Optional[Float] = None
    iptal_eden: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    aciklama: Optional[String] = None
    termin_tarihi: Optional[DateTime] = None
    iptal_z: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    kayit_z: Optional[DateTime] = None
    sevk_z: Optional[DateTime] = None
    kesinlesme_z: Optional[DateTime] = None
    stok_kodu: Optional[String] = None
    lot_no: Optional[String] = None
    tanimi: Optional[String] = None
    ambalaj: Optional[String] = None
    miktar: Optional[Float] = None
    tutar: Optional[Float] = None
    para_birimi: Optional[String] = None
    uygulanan_iskonto: Optional[Float] = None
    gerekce: Optional[Float] = None
    istenilen_termin_t: Optional[DateTime] = None
    onerilen_termin_t: Optional[DateTime] = None
    ce_fl: Optional[String] = None
    temin_fl: Optional[String] = None
    miktar_iade: Optional[Float] = None
    miktar_uretim: Optional[Float] = None
    miktar_donusum: Optional[Integer] = None
    miktar_karsilanacak: Optional[Float] = None
    bagimli_sira_no: Optional[Integer] = None
    miktar_tedarikci: Optional[Integer] = None
    miktar_eldeki: Optional[Float] = None
    miktar_fason: Optional[Float] = None
    miktar_satinalma: Optional[Float] = None
    miktar_mp_uretim: Optional[Float] = None
    etiket_fl: Optional[String] = None
    ce_numarasi: Optional[String] = None
    markalama: Optional[String] = None
    miktar_iade_siparis: Optional[Float] = None
    miktar_musteri: Optional[Float] = None
    teknik_ozellik: Optional[String] = None
    adi: Optional[String] = None
    bagimli_yil: Optional[Float] = None
    bagimli_ay: Optional[Float] = None
    bagimli_siparis_no: Optional[Float] = None
    urun_grup_no: Optional[Float] = None
    tarife_no: Optional[Float] = None
    log_record_id: Optional[String] = None
    etiket_firma: Optional[String] = None
    son_kullanma_t: Optional[DateTime] = None
    ce_bilgisi: Optional[String] = None
    hareket_kodu: Optional[Float] = None
    irsaliye_no: Optional[String] = None
    iade_sira_no: Optional[Integer] = None
    yeni_program: Optional[Integer] = None
    sut_fiyat_id: Optional[Integer] = None
    bilgiislem_note: Optional[String] = None
    istenen_stok_kodu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None
    udi_barcode: Optional[String] = None

class AlinanSiparisDetayCreate(AlinanSiparisDetayBase):
    pass

class AlinanSiparisDetay(AlinanSiparisDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True