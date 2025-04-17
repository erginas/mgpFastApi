from pydantic import BaseModel
from typing import Optional

class TpcCLoadProgressBase(BaseModel):
    tablename: Optional[String] = None
    version: Optional[Integer] = None
    setnumber: Optional[Integer] = None
    prop_name: Optional[String] = None
    prop_value: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TpcCLoadProgressCreate(TpcCLoadProgressBase):
    pass

class TpcCLoadProgress(TpcCLoadProgressBase):
    id: Optional[int]

    class Config:
        orm_mode = True