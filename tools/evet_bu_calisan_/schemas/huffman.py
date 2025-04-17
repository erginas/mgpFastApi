from pydantic import BaseModel
from typing import Optional

class HuffmanBase(BaseModel):
    indis: Optional[String] = None
    deger: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class HuffmanCreate(HuffmanBase):
    pass

class Huffman(HuffmanBase):
    id: Optional[int]

    class Config:
        orm_mode = True