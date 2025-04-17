from pydantic import BaseModel
from typing import Optional

class UretimEmriTipiBase(BaseModel):
    uretim_emri_tip_kodu: Optional[Float] = None
    adi: Optional[String] = None
    acik_nesne: Optional[String] = None
    tamir_malzeme_fl: Optional[String] = None
    tamir_lot_fl: Optional[String] = None
    uretim_malzeme_fl: Optional[String] = None
    uretim_lot_fl: Optional[String] = None
    gerekcesi: Optional[String] = None
    oncelik: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UretimEmriTipiCreate(UretimEmriTipiBase):
    pass

class UretimEmriTipi(UretimEmriTipiBase):
    id: Optional[int]

    class Config:
        orm_mode = True