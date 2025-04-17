from pydantic import BaseModel
from typing import Optional

class RolePermissionsBase(BaseModel):
    id: Optional[Float] = None
    role_id: Optional[Float] = None
    permission_id: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class RolePermissionsCreate(RolePermissionsBase):
    pass

class RolePermissions(RolePermissionsBase):
    id: Optional[int]

    class Config:
        orm_mode = True