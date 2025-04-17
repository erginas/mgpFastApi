from pydantic import BaseModel
from typing import Optional

class GeciciStokDetayBase(BaseModel):
    giris_no: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    malzeme_adi: Optional[String] = None
    miktar_gelen: Optional[Float] = None
    miktar_red: Optional[Float] = None
    miktar_sartli: Optional[Float] = None
    miktar_kabul: Optional[Float] = None
    giris_kk_rapor_no: Optional[String] = None
    aktarilan_sartli: Optional[Float] = None
    aktarilan_kabul: Optional[Float] = None
    yil: Optional[Float] = None
    hareket_kodu: Optional[Float] = None
    birimi: Optional[String] = None
    uretici_lot_no: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class GeciciStokDetayCreate(GeciciStokDetayBase):
    pass

class GeciciStokDetay(GeciciStokDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True