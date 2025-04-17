from pydantic import BaseModel
from typing import Optional

class IslemMerkeziBase(BaseModel):
    islem_merkezi_id: Optional[String] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    yayinlama_tarihi: Optional[DateTime] = None
    iptal_tarihi: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class IslemMerkeziCreate(IslemMerkeziBase):
    pass

class IslemMerkezi(IslemMerkeziBase):
    id: Optional[int]

    class Config:
        orm_mode = True