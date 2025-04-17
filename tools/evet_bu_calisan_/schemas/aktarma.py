from pydantic import BaseModel
from typing import Optional

class AktarmaBase(BaseModel):
    stok_kodu: Optional[String] = None
    lot_no: Optional[String] = None
    ktlg_tr_tanimi: Optional[String] = None
    ktg_en_tanimi: Optional[String] = None
    metaryal_1: Optional[String] = None
    metaryal_2: Optional[String] = None
    standart_1: Optional[String] = None
    standart_2: Optional[String] = None
    tr_olcu: Optional[String] = None
    miktar: Optional[String] = None
    malzeme_no: Optional[Integer] = None
    koli: Optional[String] = None
    uts_onay: Optional[String] = None
    mo_malzeme_no: Optional[Integer] = None
    opsn: Optional[String] = None
    uts_mataryal: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AktarmaCreate(AktarmaBase):
    pass

class Aktarma(AktarmaBase):
    id: Optional[int]

    class Config:
        orm_mode = True