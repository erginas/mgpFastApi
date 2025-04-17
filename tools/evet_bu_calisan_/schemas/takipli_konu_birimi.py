from pydantic import BaseModel
from typing import Optional

class TakipliKonuBirimiBase(BaseModel):
    takip_yil: Optional[Float] = None
    takip_ay: Optional[Float] = None
    takip_no: Optional[Float] = None
    cesidi: Optional[String] = None
    birim_no: Optional[Integer] = None
    problemi_belirleme_fl: Optional[String] = None
    cozecek_fl: Optional[String] = None
    ilgili_fl: Optional[String] = None
    cozuldu_fl: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TakipliKonuBirimiCreate(TakipliKonuBirimiBase):
    pass

class TakipliKonuBirimi(TakipliKonuBirimiBase):
    id: Optional[int]

    class Config:
        orm_mode = True