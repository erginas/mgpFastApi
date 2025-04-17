from pydantic import BaseModel
from typing import Optional

class MalzemeHareketi03012025Base(BaseModel):
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    raf_omru: Optional[Float] = None
    aciklama: Optional[String] = None
    lot_no: Optional[String] = None
    giris_cikis_fl: Optional[String] = None
    miktar: Optional[Float] = None
    birim: Optional[String] = None
    gel_isemri_no: Optional[String] = None
    geldigi_isemri: Optional[String] = None
    git_isemri_no: Optional[String] = None
    gittigi_isemri: Optional[String] = None
    hareket_kodu: Optional[Float] = None
    yil: Optional[Float] = None
    giris_no: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    belge_tipi: Optional[String] = None
    belge_tarihi: Optional[DateTime] = None
    belge_no: Optional[String] = None
    tarihi: Optional[DateTime] = None
    son_kullanma_t: Optional[DateTime] = None
    fas_yil: Optional[Float] = None
    fas_no: Optional[Float] = None
    isemri_no: Optional[String] = None
    teslim_eden: Optional[Float] = None
    teslim_alan: Optional[Float] = None
    fas_sira_no: Optional[Integer] = None
    fas_ay: Optional[Float] = None
    durumu: Optional[String] = None
    kk_rapor_no: Optional[Float] = None
    kk_yil: Optional[Float] = None
    kk_sira_no: Optional[Integer] = None
    kk_sonucu: Optional[String] = None
    ref_depo_kodu: Optional[Integer] = None
    ref_hareket_no: Optional[Float] = None
    krslm_malzeme_no: Optional[Integer] = None
    siparis_yil: Optional[Float] = None
    siparis_ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    siparis_sira_no: Optional[Integer] = None
    uyg_yil: Optional[Float] = None
    uyg_ay: Optional[Float] = None
    uyg_rapor_no: Optional[Float] = None
    bekleten: Optional[Float] = None
    bekleme_tarihi: Optional[DateTime] = None
    bekleme_sebebi: Optional[String] = None
    arsiv_lot_no: Optional[String] = None
    iade_yil: Optional[Float] = None
    iade_ay: Optional[Float] = None
    iade_fis_no: Optional[Float] = None
    ce_bilgisi: Optional[String] = None
    kayit_yili: Optional[Float] = None
    kayit_no: Optional[Float] = None
    kisa_kodu: Optional[String] = None
    birim_fiyati: Optional[Float] = None
    sevk_yil: Optional[Float] = None
    sevk_ay: Optional[Float] = None
    sevk_no: Optional[Float] = None
    koli_no: Optional[Float] = None
    set_malzeme_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    set_lot_no: Optional[String] = None
    bim_aciklama: Optional[String] = None
    yeni_program: Optional[Integer] = None
    satis_onayi: Optional[Float] = None
    iade_siparis_sira_no: Optional[Integer] = None
    uts_lot_no: Optional[String] = None
    uts_uretim_tarihi: Optional[DateTime] = None
    uts_miktar: Optional[Integer] = None
    uts_bildirim_durumu: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemeHareketi03012025Create(MalzemeHareketi03012025Base):
    pass

class MalzemeHareketi03012025(MalzemeHareketi03012025Base):
    id: Optional[int]

    class Config:
        orm_mode = True