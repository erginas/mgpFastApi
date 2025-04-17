from pydantic import BaseModel
from typing import Optional

class OrganizasyonBirimiBase(BaseModel):
    birim_no: Optional[Integer] = None
    bagimli_birim: Optional[Integer] = None
    kisa_kod: Optional[String] = None
    adi: Optional[String] = None
    kimlik_no: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_nedeni: Optional[String] = None
    cesidi: Optional[String] = None
    gizli: Optional[Float] = None
    aktif: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class OrganizasyonBirimiCreate(OrganizasyonBirimiBase):
    pass

class OrganizasyonBirimi(OrganizasyonBirimiBase):
    id: Optional[int]

    class Config:
        orm_mode = True