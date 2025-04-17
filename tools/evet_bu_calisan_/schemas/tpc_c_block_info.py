from pydantic import BaseModel
from typing import Optional

class TpcCBlockInfoBase(BaseModel):
    tablename: Optional[String] = None
    current_block: Optional[Integer] = None
    max_block: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TpcCBlockInfoCreate(TpcCBlockInfoBase):
    pass

class TpcCBlockInfo(TpcCBlockInfoBase):
    id: Optional[int]

    class Config:
        orm_mode = True