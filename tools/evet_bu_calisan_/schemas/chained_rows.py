from pydantic import BaseModel
from typing import Optional

class ChainedRowsBase(BaseModel):
    owner_name: Optional[String] = None
    table_name: Optional[String] = None
    cluster_name: Optional[String] = None
    partition_name: Optional[String] = None
    subpartition_name: Optional[String] = None
    head_rowid: Optional[String] = None
    analyze_timestamp: Optional[DateTime] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class ChainedRowsCreate(ChainedRowsBase):
    pass

class ChainedRows(ChainedRowsBase):
    id: Optional[int]

    class Config:
        orm_mode = True