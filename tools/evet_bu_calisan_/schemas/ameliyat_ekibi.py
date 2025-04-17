from pydantic import BaseModel
from typing import Optional

class AmeliyatEkibiBase(BaseModel):
    yil: Optional[Float] = None
    ay: Optional[Float] = None
    siparis_no: Optional[Float] = None
    kimlik_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class AmeliyatEkibiCreate(AmeliyatEkibiBase):
    pass

class AmeliyatEkibi(AmeliyatEkibiBase):
    id: Optional[int]

    class Config:
        orm_mode = True