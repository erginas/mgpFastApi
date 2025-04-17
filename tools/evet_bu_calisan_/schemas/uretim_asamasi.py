from pydantic import BaseModel
from typing import Optional

class UretimAsamasiBase(BaseModel):
    asama_no: Optional[Float] = None
    tercih_onceligi: Optional[Float] = None
    aciklama: Optional[String] = None
    tanim_tarihi: Optional[DateTime] = None
    iptal_tarihi: Optional[DateTime] = None
    kimlik_no: Optional[Float] = None
    iptal_eden: Optional[Float] = None
    recete_no: Optional[Float] = None
    operasyon_no: Optional[Float] = None
    iptal_nedeni: Optional[String] = None
    recete_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UretimAsamasiCreate(UretimAsamasiBase):
    pass

class UretimAsamasi(UretimAsamasiBase):
    id: Optional[int]

    class Config:
        orm_mode = True