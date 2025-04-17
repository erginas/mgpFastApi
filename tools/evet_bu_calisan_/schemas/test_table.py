from pydantic import BaseModel
from typing import Optional

class TestTableBase(BaseModel):
    yil: Optional[Float] = None
    sira: Optional[Float] = None
    deger: Optional[String] = None
    tarih: Optional[DateTime] = None
    log_record_id: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class TestTableCreate(TestTableBase):
    pass

class TestTable(TestTableBase):
    id: Optional[int]

    class Config:
        orm_mode = True