from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    id: Optional[Float] = None
    name: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: Optional[int]

    class Config:
        orm_mode = True