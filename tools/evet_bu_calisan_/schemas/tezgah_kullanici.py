from pydantic import BaseModel
from typing import Optional

class TezgahKullaniciBase(BaseModel):
    id: Optional[Integer] = None
    tezgah_grup_no: Optional[Integer] = None
    kimlik_no: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TezgahKullaniciCreate(TezgahKullaniciBase):
    pass

class TezgahKullanici(TezgahKullaniciBase):
    id: Optional[int]

    class Config:
        orm_mode = True