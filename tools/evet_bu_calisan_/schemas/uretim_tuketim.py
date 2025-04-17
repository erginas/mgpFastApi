from pydantic import BaseModel
from typing import Optional

class UretimTuketimBase(BaseModel):
    asama_no: Optional[Float] = None
    sira_no: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    uretim_tuketim_fl: Optional[String] = None
    giris_cikis_fl: Optional[String] = None
    miktar: Optional[Float] = None
    tarihi: Optional[DateTime] = None
    aciklama: Optional[String] = None
    nedeni: Optional[String] = None
    birimi: Optional[String] = None
    kimlik_no: Optional[Float] = None
    boy: Optional[Float] = None
    en: Optional[Float] = None
    cap: Optional[Float] = None
    recete_detay_id: Optional[Integer] = None
    yeni: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class UretimTuketimCreate(UretimTuketimBase):
    pass

class UretimTuketim(UretimTuketimBase):
    id: Optional[int]

    class Config:
        orm_mode = True