from pydantic import BaseModel
from typing import Optional

class RoleBase(BaseModel):
    id: Optional[Float] = None
    name: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: Optional[int]

    class Config:
        orm_mode = True