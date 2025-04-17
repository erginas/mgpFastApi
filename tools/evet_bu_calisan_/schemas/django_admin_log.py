from pydantic import BaseModel
from typing import Optional

class DjangoAdminLogBase(BaseModel):
    id: Optional[Float] = None
    action_time: Optional[DateTime] = None
    object_id: Optional[String] = None
    object_repr: Optional[String] = None
    action_flag: Optional[Float] = None
    change_message: Optional[String] = None
    content_type_id: Optional[Float] = None
    user_id: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DjangoAdminLogCreate(DjangoAdminLogBase):
    pass

class DjangoAdminLog(DjangoAdminLogBase):
    id: Optional[int]

    class Config:
        orm_mode = True