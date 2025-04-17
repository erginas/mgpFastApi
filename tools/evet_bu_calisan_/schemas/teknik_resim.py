from pydantic import BaseModel
from typing import Optional

class TeknikResimBase(BaseModel):
    teknik_resim_id: Optional[String] = None
    resim_kodu: Optional[String] = None
    malzeme_adi: Optional[String] = None
    asama_adi: Optional[String] = None
    yayinlandigi_tarih: Optional[DateTime] = None
    iptal_tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TeknikResimCreate(TeknikResimBase):
    pass

class TeknikResim(TeknikResimBase):
    id: Optional[int]

    class Config:
        orm_mode = True