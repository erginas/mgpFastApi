from pydantic import BaseModel
from typing import Optional

class KitaplarYorumBase(BaseModel):
    id: Optional[Float] = None
    yorum: Optional[String] = None
    yaratilma_tarihi: Optional[DateTime] = None
    guncellenme_tarihi: Optional[DateTime] = None
    degerlendirme: Optional[Float] = None
    kitap_id: Optional[Float] = None
    yorum_sahibi_id: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class KitaplarYorumCreate(KitaplarYorumBase):
    pass

class KitaplarYorum(KitaplarYorumBase):
    id: Optional[int]

    class Config:
        orm_mode = True