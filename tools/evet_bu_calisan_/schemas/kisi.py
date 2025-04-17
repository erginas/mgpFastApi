from pydantic import BaseModel
from typing import Optional

class KisiBase(BaseModel):
    kimlik_no: Optional[Float] = None
    adi: Optional[String] = None
    soyadi: Optional[String] = None
    baba_adi: Optional[String] = None
    ana_adi: Optional[String] = None
    meslegi: Optional[String] = None
    dogum_yeri: Optional[String] = None
    dogum_tarihi: Optional[DateTime] = None
    kan_grubu: Optional[String] = None
    cinsiyeti: Optional[String] = None
    medeni_hali: Optional[String] = None
    ev_tel: Optional[String] = None
    cep_tel: Optional[String] = None
    is_tel: Optional[String] = None
    adres: Optional[String] = None
    ssk_no: Optional[String] = None
    ilgili_sirket: Optional[String] = None
    ise_giris_tarihi: Optional[DateTime] = None
    isten_cikis_t: Optional[DateTime] = None
    vergi_dairesi: Optional[String] = None
    vergi_no: Optional[String] = None
    birim_no: Optional[Integer] = None
    gorevi: Optional[String] = None
    mesai_fl: Optional[String] = None
    aciklama: Optional[String] = None
    gorev_kodu: Optional[Integer] = None
    egitim_durumu: Optional[String] = None
    takma_ad: Optional[String] = None
    sifre: Optional[String] = None
    ayakkabi_no: Optional[String] = None
    ust_beden: Optional[String] = None
    alt_beden: Optional[String] = None
    sifresi: Optional[String] = None
    kilit: Optional[Float] = None
    id: Optional[Integer] = None
    password: Optional[String] = None
    last_login: Optional[DateTime] = None
    is_superuser: Optional[Float] = None
    username: Optional[String] = None
    first_name: Optional[String] = None
    email: Optional[String] = None
    is_staff: Optional[Float] = None
    is_active: Optional[Float] = None
    date_joined: Optional[DateTime] = None
    aktif: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KisiCreate(KisiBase):
    pass

class Kisi(KisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True