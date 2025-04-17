from pydantic import BaseModel
from typing import Optional

class ValidasyonDetayBase(BaseModel):
    id: Optional[Float] = None
    aciklama: Optional[String] = None
    kts: Optional[DateTime] = None
    kk_id: Optional[Float] = None
    menu_kodu: Optional[Float] = None
    onay_durumu: Optional[Float] = None
    ust_menu: Optional[Float] = None
    validasyon_id: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ValidasyonDetayCreate(ValidasyonDetayBase):
    pass

class ValidasyonDetay(ValidasyonDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True