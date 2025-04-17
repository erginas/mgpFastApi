from pydantic import BaseModel
from typing import Optional

class VeriDuzeltmeDetayiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    veri_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    kayit_z: Optional[DateTime] = None
    tablo: Optional[String] = None
    saha: Optional[String] = None
    gorunen_adi: Optional[String] = None
    eski_deger: Optional[String] = None
    yeni_deger: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class VeriDuzeltmeDetayiCreate(VeriDuzeltmeDetayiBase):
    pass

class VeriDuzeltmeDetayi(VeriDuzeltmeDetayiBase):
    id: Optional[int]

    class Config:
        orm_mode = True