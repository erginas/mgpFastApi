from pydantic import BaseModel
from typing import Optional

class PerformansVerisiBase(BaseModel):
    malzeme_no: Optional[Integer] = None
    veri_no: Optional[Float] = None
    tipi: Optional[String] = None
    a_degeri: Optional[Float] = None
    b_degeri: Optional[Float] = None
    umin: Optional[Float] = None
    umax: Optional[Float] = None
    devir: Optional[Float] = None
    aciklama: Optional[String] = None
    ek_bilgi: Optional[String] = None
    nokta: Optional[String] = None
    katsayi: Optional[String] = None
    musteri: Optional[String] = None
    siparis_ref_no: Optional[String] = None
    debi: Optional[Float] = None
    basinc: Optional[Float] = None
    test_sicakligi: Optional[Float] = None
    olcum_capi: Optional[Float] = None
    rakim: Optional[Float] = None
    motor_markasi: Optional[String] = None
    motor_verimi: Optional[Float] = None
    motor_devri: Optional[Float] = None
    etiket_cos_fi: Optional[Float] = None
    test_tarihi: Optional[DateTime] = None
    etiket_verimi: Optional[Float] = None
    etiket_akimi: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class PerformansVerisiCreate(PerformansVerisiBase):
    pass

class PerformansVerisi(PerformansVerisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True