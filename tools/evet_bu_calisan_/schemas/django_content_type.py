from pydantic import BaseModel
from typing import Optional

class DjangoContentTypeBase(BaseModel):
    id: Optional[Float] = None
    app_label: Optional[String] = None
    model: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DjangoContentTypeCreate(DjangoContentTypeBase):
    pass

class DjangoContentType(DjangoContentTypeBase):
    id: Optional[int]

    class Config:
        orm_mode = True