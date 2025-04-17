from pydantic import BaseModel
from typing import Optional

class IsEmriAktarmaIslemiBase(BaseModel):
    tekrar: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    aktarma_tarihi: Optional[DateTime] = None
    miktar_aktarilan: Optional[Float] = None
    geldigi_isemri: Optional[String] = None
    gittigi_isemri: Optional[String] = None
    gerekcesi: Optional[String] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriAktarmaIslemiCreate(IsEmriAktarmaIslemiBase):
    pass

class IsEmriAktarmaIslemi(IsEmriAktarmaIslemiBase):
    id: Optional[int]

    class Config:
        orm_mode = True