from pydantic import BaseModel
from typing import Optional

class UretimEmriTipiYetkilisiBase(BaseModel):
    uretim_emri_tip_kodu: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class UretimEmriTipiYetkilisiCreate(UretimEmriTipiYetkilisiBase):
    pass

class UretimEmriTipiYetkilisi(UretimEmriTipiYetkilisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True