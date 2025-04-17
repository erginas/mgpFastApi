from pydantic import BaseModel
from typing import Optional

class IsEmriPlanlananAdimBase(BaseModel):
    isemri_no: Optional[String] = None
    adim_no: Optional[Float] = None
    tezgah_no: Optional[String] = None
    operasyon_no: Optional[Float] = None
    pl_bas_zamani: Optional[DateTime] = None
    pl_bit_zamani: Optional[DateTime] = None
    pl_miktar: Optional[Float] = None
    aciklama: Optional[String] = None
    durumu: Optional[String] = None
    teknik_dokuman: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class IsEmriPlanlananAdimCreate(IsEmriPlanlananAdimBase):
    pass

class IsEmriPlanlananAdim(IsEmriPlanlananAdimBase):
    id: Optional[int]

    class Config:
        orm_mode = True