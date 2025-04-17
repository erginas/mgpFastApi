from pydantic import BaseModel
from typing import Optional

class Scheduler$JobArgBase(BaseModel):
    job_name: Optional[String] = None
    arg_name: Optional[String] = None
    arg_position: Optional[Integer] = None
    value: Optional[String] = None
    flags: Optional[Integer] = None
    enabled: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class Scheduler$JobArgCreate(Scheduler$JobArgBase):
    pass

class Scheduler$JobArg(Scheduler$JobArgBase):
    id: Optional[int]

    class Config:
        orm_mode = True