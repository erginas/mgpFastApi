from pydantic import BaseModel
from typing import Optional

class UretimTalebiBase(BaseModel):
    yil: Optional[Float] = None
    fis_no: Optional[Float] = None
    teslim_eden: Optional[Float] = None
    teslim_alan: Optional[Float] = None
    duzenleme_tarihi: Optional[DateTime] = None
    tamir_nedeni: Optional[String] = None
    siparis_no: Optional[String] = None
    iade_fis_tarihi: Optional[DateTime] = None
    iade_fis_no: Optional[String] = None
    set_adi: Optional[String] = None
    set_no: Optional[Float] = None
    uretim_emri_tip_kodu: Optional[Float] = None
    aciklama: Optional[String] = None
    durum_fl: Optional[String] = None
    kapanis_tarihi: Optional[DateTime] = None
    onaylayan: Optional[Float] = None
    onay_tarihi: Optional[DateTime] = None
    malzeme_set_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    ref_belge: Optional[String] = None
    sevk_sekli: Optional[String] = None
    stok_amacli_fl: Optional[String] = None
    uubf_no: Optional[String] = None
    siparis_yil: Optional[Float] = None
    siparis_ay: Optional[Float] = None
    siparisno: Optional[Float] = None
    uyg_yil: Optional[Float] = None
    uyg_ay: Optional[Float] = None
    uyg_rapor_no: Optional[Float] = None
    iade_yil: Optional[Float] = None
    iade_ay: Optional[Float] = None
    iade_fisno: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UretimTalebiCreate(UretimTalebiBase):
    pass

class UretimTalebi(UretimTalebiBase):
    id: Optional[int]

    class Config:
        orm_mode = True