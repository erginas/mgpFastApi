from pydantic import BaseModel
from typing import Optional

class DjangoMigrationsBase(BaseModel):
    id: Optional[Float] = None
    app: Optional[String] = None
    name: Optional[String] = None
    applied: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class DjangoMigrationsCreate(DjangoMigrationsBase):
    pass

class DjangoMigrations(DjangoMigrationsBase):
    id: Optional[int]

    class Config:
        orm_mode = True