from pydantic import BaseModel
from typing import Optional

class ReceteOzelligiBase(BaseModel):
    id: Optional[Integer] = None
    master_id: Optional[Integer] = None
    sinif_id: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    operasyon_no: Optional[Integer] = None
    yari_mamul: Optional[Integer] = None
    miktar: Optional[Integer] = None
    boy: Optional[Integer] = None
    en: Optional[Integer] = None
    cap: Optional[Integer] = None
    birimi: Optional[String] = None
    temin_sekli: Optional[String] = None
    teknik_resim_no: Optional[String] = None
    net_sure: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteOzelligiCreate(ReceteOzelligiBase):
    pass

class ReceteOzelligi(ReceteOzelligiBase):
    id: Optional[int]

    class Config:
        orm_mode = True