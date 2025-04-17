from pydantic import BaseModel
from typing import Optional

class MyLogSessionBase(BaseModel):
    log_session_id: Optional[String] = None
    application_user: Optional[String] = None
    start_time: Optional[DateTime] = None
    end_time: Optional[DateTime] = None
    connect_info: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MyLogSessionCreate(MyLogSessionBase):
    pass

class MyLogSession(MyLogSessionBase):
    id: Optional[int]

    class Config:
        orm_mode = True