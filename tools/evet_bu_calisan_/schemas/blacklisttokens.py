from pydantic import BaseModel
from typing import Optional

class BlacklisttokensBase(BaseModel):
    id: Optional[String] = None
    expire: Optional[DateTime] = None
    created_at: Optional[DateTime] = None

class BlacklisttokensCreate(BlacklisttokensBase):
    pass

class Blacklisttokens(BlacklisttokensBase):
    id: Optional[int]

    class Config:
        orm_mode = True