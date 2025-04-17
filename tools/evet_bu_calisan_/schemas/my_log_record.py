from pydantic import BaseModel
from typing import Optional

class MyLogRecordBase(BaseModel):
    log_record_id: Optional[String] = None
    create_date: Optional[DateTime] = None
    create_session: Optional[String] = None
    delete_date: Optional[DateTime] = None
    delete_session: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class MyLogRecordCreate(MyLogRecordBase):
    pass

class MyLogRecord(MyLogRecordBase):
    id: Optional[int]

    class Config:
        orm_mode = True