from pydantic import BaseModel
from typing import Optional

class AlembicVersionBase(BaseModel):
    version_num: Optional[String] = None

class AlembicVersionCreate(AlembicVersionBase):
    pass

class AlembicVersion(AlembicVersionBase):
    id: Optional[int]

    class Config:
        orm_mode = True