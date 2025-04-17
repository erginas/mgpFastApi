from pydantic import BaseModel
from typing import Optional

class IsEmriOperasyonuBase(BaseModel):
    islem_sirasi: Optional[Float] = None
    operasyon_no: Optional[Float] = None
    durus_detay_kodu: Optional[Float] = None
    durumu: Optional[String] = None
    durus_baslangic: Optional[DateTime] = None
    durus_bitis: Optional[DateTime] = None
    islem_baslangic: Optional[DateTime] = None
    islem_bitis: Optional[DateTime] = None
    islem_suresi: Optional[Float] = None
    isemri_no: Optional[String] = None
    miktar_giren: Optional[Float] = None
    miktar_kabul: Optional[Float] = None
    miktar_red: Optional[Float] = None
    miktar_sartli_kabul: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    tezgah_no: Optional[String] = None
    aciklama: Optional[String] = None
    proses_rapor_no: Optional[String] = None
    miktar_kontrol: Optional[Float] = None
    miktar_kayit: Optional[Float] = None
    miktar_cikan: Optional[Float] = None
    miktar_parca_red: Optional[Float] = None
    recete_no: Optional[Float] = None
    kayit_no: Optional[Float] = None
    uyg_yil: Optional[Float] = None
    uyg_ay: Optional[Float] = None
    uyg_rapor_no: Optional[Float] = None
    sk_plan_kodu: Optional[Float] = None
    firma_kodu: Optional[Integer] = None
    vakum_degeri: Optional[Integer] = None
    yapistirma_suresi: Optional[Integer] = None
    bekleme_suresi: Optional[Integer] = None
    recete_detay_id: Optional[Integer] = None
    vakum_suresi: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriOperasyonuCreate(IsEmriOperasyonuBase):
    pass

class IsEmriOperasyonu(IsEmriOperasyonuBase):
    id: Optional[int]

    class Config:
        orm_mode = True