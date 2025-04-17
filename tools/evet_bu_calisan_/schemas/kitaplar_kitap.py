from pydantic import BaseModel
from typing import Optional

class KitaplarKitapBase(BaseModel):
    id: Optional[Float] = None
    isim: Optional[String] = None
    yazar: Optional[String] = None
    aciklama: Optional[String] = None
    yaratilma_tarihi: Optional[DateTime] = None
    guncellenme_tarihi: Optional[DateTime] = None
    yayin_tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class KitaplarKitapCreate(KitaplarKitapBase):
    pass

class KitaplarKitap(KitaplarKitapBase):
    id: Optional[int]

    class Config:
        orm_mode = True