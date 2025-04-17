from pydantic import BaseModel
from typing import Optional

class AlinanSiparisFaturaBase(BaseModel):
    id: Optional[Integer] = None
    yil: Optional[Integer] = None
    ay: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    irsaliye_no: Optional[String] = None
    fatura_no: Optional[String] = None
    tarihi: Optional[DateTime] = None
    hareket_kodu: Optional[Integer] = None
    irsaliye_tarihi: Optional[DateTime] = None
    irsaliye_zamani: Optional[DateTime] = None
    irsaliye_giren: Optional[Integer] = None
    fatura_tarihi: Optional[DateTime] = None
    fatura_zamani: Optional[DateTime] = None
    fatura_giren: Optional[Integer] = None
    firma_kodu: Optional[Integer] = None
    baski_sayisi: Optional[Integer] = None
    kimlik_no: Optional[Integer] = None
    gumruk_bedeli: Optional[Integer] = None
    tasima_bedeli: Optional[Integer] = None
    diger_bedel: Optional[Integer] = None
    beyanname_no: Optional[String] = None
    aciklama: Optional[String] = None
    birim_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class AlinanSiparisFaturaCreate(AlinanSiparisFaturaBase):
    pass

class AlinanSiparisFatura(AlinanSiparisFaturaBase):
    id: Optional[int]

    class Config:
        orm_mode = True