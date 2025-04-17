from pydantic import BaseModel
from typing import Optional

class FiyatTarifesiBase(BaseModel):
    tarife_no: Optional[Float] = None
    aciklama: Optional[String] = None
    adi: Optional[String] = None
    urun_grup_no: Optional[Float] = None
    bitis_t: Optional[DateTime] = None
    yayinlandi_fl: Optional[String] = None
    baslangic_t: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class FiyatTarifesiCreate(FiyatTarifesiBase):
    pass

class FiyatTarifesi(FiyatTarifesiBase):
    id: Optional[int]

    class Config:
        orm_mode = True