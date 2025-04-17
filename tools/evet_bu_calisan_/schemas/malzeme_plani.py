from pydantic import BaseModel
from typing import Optional

class MalzemePlaniBase(BaseModel):
    donem_no: Optional[Float] = None
    malzeme_no: Optional[Integer] = None
    miktar_eldeki: Optional[Float] = None
    tarih_eldeki: Optional[DateTime] = None
    miktar_bloke: Optional[Float] = None
    miktar_uretim: Optional[Float] = None
    tarih_uretim: Optional[DateTime] = None
    miktar_emniyet_1: Optional[Float] = None
    miktar_emniyet_2: Optional[Float] = None
    miktar_hesap: Optional[Float] = None
    miktar_hedef: Optional[Float] = None
    miktar_oncelikli_hedef: Optional[Float] = None
    oncelik: Optional[String] = None
    aciklama: Optional[String] = None
    bitis_tarihi: Optional[DateTime] = None
    surum: Optional[Float] = None
    miktar_fasonda: Optional[Float] = None
    miktar_fasona: Optional[Float] = None
    miktar_satinalma: Optional[Float] = None
    miktar_satinalinacak: Optional[Float] = None
    miktar_is_emri: Optional[Float] = None
    miktar_acilmamis_ie: Optional[Float] = None
    miktar_bekleme_bolgesi: Optional[Float] = None
    miktar_iptal: Optional[Float] = None
    miktar_bek_bol_cikilan: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MalzemePlaniCreate(MalzemePlaniBase):
    pass

class MalzemePlani(MalzemePlaniBase):
    id: Optional[int]

    class Config:
        orm_mode = True