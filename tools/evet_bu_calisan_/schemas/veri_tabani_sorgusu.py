from pydantic import BaseModel
from typing import Optional

class VeriTabaniSorgusuBase(BaseModel):
    sorgu_no: Optional[Float] = None
    adi: Optional[String] = None
    gerekcesi: Optional[String] = None
    sorgu_vc: Optional[String] = None
    sorgu: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class VeriTabaniSorgusuCreate(VeriTabaniSorgusuBase):
    pass

class VeriTabaniSorgusu(VeriTabaniSorgusuBase):
    id: Optional[int]

    class Config:
        orm_mode = True