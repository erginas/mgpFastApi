from pydantic import BaseModel
from typing import Optional

class OperasyonBase(BaseModel):
    operasyon_no: Optional[Float] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    ust_operasyon: Optional[Float] = None
    isleme_sinifi: Optional[String] = None
    bilgisayarli_fl: Optional[String] = None
    tezgah_fl: Optional[String] = None
    personel_fl: Optional[String] = None
    recete_bagimsiz: Optional[String] = None
    iscilik_maliyeti: Optional[Float] = None
    firma_ister_fl: Optional[String] = None
    recete_olustururken_gosterme: Optional[Integer] = None
    vakum_ister: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class OperasyonCreate(OperasyonBase):
    pass

class Operasyon(OperasyonBase):
    id: Optional[int]

    class Config:
        orm_mode = True