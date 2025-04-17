from pydantic import BaseModel
from typing import Optional

class SorguYetkilisiBase(BaseModel):
    sorgu_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    okuma: Optional[String] = None
    calistirma: Optional[String] = None
    yazma: Optional[String] = None
    yetkilendirme: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class SorguYetkilisiCreate(SorguYetkilisiBase):
    pass

class SorguYetkilisi(SorguYetkilisiBase):
    id: Optional[int]

    class Config:
        orm_mode = True