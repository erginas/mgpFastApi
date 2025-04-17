from pydantic import BaseModel
from typing import Optional

class IptalNedeniBase(BaseModel):
    iptal_neden_id: Optional[String] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IptalNedeniCreate(IptalNedeniBase):
    pass

class IptalNedeni(IptalNedeniBase):
    id: Optional[int]

    class Config:
        orm_mode = True