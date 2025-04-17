from pydantic import BaseModel
from typing import Optional

class TezgahBase(BaseModel):
    tezgah_no: Optional[String] = None
    adi: Optional[String] = None
    org_birimi: Optional[String] = None
    grup_no: Optional[Float] = None
    diagram_no: Optional[Float] = None
    x_pos: Optional[Float] = None
    y_pos: Optional[Float] = None
    cap: Optional[Float] = None
    iptal_t: Optional[DateTime] = None
    iptal_eden: Optional[Float] = None
    iptal_nedeni: Optional[String] = None
    ilk_calisma_tarihi: Optional[DateTime] = None
    guc: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TezgahCreate(TezgahBase):
    pass

class Tezgah(TezgahBase):
    id: Optional[int]

    class Config:
        orm_mode = True