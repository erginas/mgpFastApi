from pydantic import BaseModel
from typing import Optional

class MalzemeBase(BaseModel):
    malzeme_no: Optional[Integer] = None
    grup_no: Optional[Integer] = None
    malzeme_adi: Optional[String] = None
    birimi: Optional[String] = None
    birim_agirligi: Optional[Float] = None
    tanim_tarihi: Optional[DateTime] = None
    iptal_tarihi: Optional[DateTime] = None
    etiket_cinsi: Optional[Integer] = None
    opsn: Optional[String] = None
    set_fl: Optional[Float] = None
    tanimi: Optional[String] = None
    miktar_emniyet_1: Optional[Float] = None
    temin_suresi: Optional[Integer] = None
    sure_kodu: Optional[String] = None
    miktar_emniyet_2: Optional[Float] = None
    miktar_urun_agac: Optional[Float] = None
    opsiyon_adi: Optional[String] = None
    plan_fl: Optional[String] = None
    resim_no: Optional[String] = None
    recete_no: Optional[Float] = None
    siralama: Optional[Float] = None
    sk_plan_kodu: Optional[Float] = None
    uretim_alarmi: Optional[Float] = None
    iptal_nedeni: Optional[String] = None
    miktar_eldeki: Optional[Float] = None
    tarih_eldeki: Optional[DateTime] = None
    miktar_bloke: Optional[Float] = None
    tarih_uretim: Optional[DateTime] = None
    miktar_hesap: Optional[Float] = None
    miktar_hedef: Optional[Float] = None
    miktar_oncelikli_hedef: Optional[Float] = None
    miktar_fasonda: Optional[Float] = None
    miktar_fasona: Optional[Float] = None
    miktar_satinalma: Optional[Float] = None
    miktar_satinalinacak: Optional[Float] = None
    oncelik: Optional[String] = None
    aciklama: Optional[String] = None
    bitis_tarihi: Optional[DateTime] = None
    miktar_is_emri: Optional[Float] = None
    miktar_acilmamis_ie: Optional[Float] = None
    miktar_mp_uretim: Optional[Float] = None
    miktar_bekleme_bolgesi: Optional[Float] = None
    miktar_bek_bol_cikilan: Optional[Float] = None
    urun_grup_no: Optional[Float] = None
    birimi_2: Optional[String] = None
    donusum_katsayisi: Optional[Float] = None
    kisa_kodu: Optional[String] = None
    edinme_maliyeti: Optional[Float] = None
    bagimli_malzeme_no: Optional[Integer] = None
    teknik_ozellik: Optional[String] = None
    ubb_fl: Optional[String] = None
    tpsn_malzeme_no: Optional[Integer] = None
    log_record_id: Optional[String] = None
    skt_fl: Optional[Integer] = None
    resim_id: Optional[Integer] = None
    gercek_resim_id: Optional[Integer] = None
    ce_fl: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    stok_konsinye: Optional[String] = None
    gecici_stok_kodu: Optional[String] = None
    kisa_adi: Optional[String] = None
    recete_id: Optional[Integer] = None
    malzeme_relation_id: Optional[Integer] = None
    kutu_id: Optional[Integer] = None
    euromed_stok_kodu: Optional[String] = None
    miktar_konsinye: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeCreate(MalzemeBase):
    pass

class Malzeme(MalzemeBase):
    id: Optional[int]

    class Config:
        orm_mode = True