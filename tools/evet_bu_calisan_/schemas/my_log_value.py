from pydantic import BaseModel
from typing import Optional

class MyLogValueBase(BaseModel):
    log_value_id: Optional[String] = None
    log_field: Optional[String] = None
    log_value: Optional[String] = None
    log_session_id: Optional[String] = None
    log_key_id: Optional[String] = None
    chg_date: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MyLogValueCreate(MyLogValueBase):
    pass

class MyLogValue(MyLogValueBase):
    id: Optional[int]

    class Config:
        orm_mode = True