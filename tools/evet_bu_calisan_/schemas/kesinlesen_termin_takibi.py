from pydantic import BaseModel
from typing import Optional

class KesinlesenTerminTakibiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    kesinlesen_termin: Optional[DateTime] = None
    kayit_z: Optional[DateTime] = None
    musteri_termini: Optional[DateTime] = None
    aciklama: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class KesinlesenTerminTakibiCreate(KesinlesenTerminTakibiBase):
    pass

class KesinlesenTerminTakibi(KesinlesenTerminTakibiBase):
    id: Optional[int]

    class Config:
        orm_mode = True