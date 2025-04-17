from pydantic import BaseModel
from typing import Optional

class CariKayitBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    sira_no: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    araci_firma_kodu: Optional[Integer] = None
    kisa_kodu: Optional[String] = None
    kaydeden: Optional[Float] = None
    iptal_eden: Optional[Float] = None
    iade_yil: Optional[Float] = None
    iade_ay: Optional[Float] = None
    iade_fis_no: Optional[Float] = None
    siparis_yil: Optional[Float] = None
    siparis_ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    banka_kodu: Optional[Float] = None
    hesap_kodu: Optional[Float] = None
    kayit_z: Optional[DateTime] = None
    vade_t: Optional[DateTime] = None
    tutar: Optional[Float] = None
    kredi_bitis_t: Optional[DateTime] = None
    aciklama: Optional[String] = None
    islem_gerekcesi: Optional[Float] = None
    borc_alacak_fl: Optional[String] = None
    islem_ref_belge: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class CariKayitCreate(CariKayitBase):
    pass

class CariKayit(CariKayitBase):
    id: Optional[int]

    class Config:
        orm_mode = True