from pydantic import BaseModel
from typing import Optional

class SiparisSevkKolisiBase(BaseModel):
    sevk_yil: Optional[Float] = None
    sevk_ay: Optional[Float] = None
    sevk_no: Optional[Float] = None
    koli_no: Optional[Float] = None
    agirlik: Optional[Float] = None
    ebat: Optional[String] = None
    koli_id: Optional[Integer] = None
    koli_tanim: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class SiparisSevkKolisiCreate(SiparisSevkKolisiBase):
    pass

class SiparisSevkKolisi(SiparisSevkKolisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True