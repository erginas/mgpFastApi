from pydantic import BaseModel
from typing import Optional

class AlinanSiparisFaturaDetayBase(BaseModel):
    id: Optional[Float] = None
    als_fatura_id: Optional[Integer] = None
    depo_kodu: Optional[Integer] = None
    hareket_no: Optional[Integer] = None
    uretim_bildirim_no: Optional[String] = None
    verme_bildirim_no: Optional[String] = None
    adet: Optional[Integer] = None
    iptal_eden: Optional[String] = None
    iptal_zamani: Optional[DateTime] = None
    iptal_aciklama: Optional[String] = None
    muadil_malzeme_no: Optional[Integer] = None
    muadil_fiyat: Optional[Integer] = None
    muadil_iskonto: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanSiparisFaturaDetayCreate(AlinanSiparisFaturaDetayBase):
    pass

class AlinanSiparisFaturaDetay(AlinanSiparisFaturaDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True