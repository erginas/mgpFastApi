from pydantic import BaseModel
from typing import Optional

class MalzemeReceteBase(BaseModel):
    recete_no: Optional[Float] = None
    adi: Optional[String] = None
    aciklama: Optional[String] = None
    resim_no: Optional[String] = None
    ust_recete: Optional[Float] = None
    sira_no: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class MalzemeReceteCreate(MalzemeReceteBase):
    pass

class MalzemeRecete(MalzemeReceteBase):
    id: Optional[int]

    class Config:
        orm_mode = True