from pydantic import BaseModel
from typing import Optional

class ReceteDetayBase(BaseModel):
    id: Optional[Integer] = None
    recete_id: Optional[Integer] = None
    sira_no: Optional[Integer] = None
    adi: Optional[String] = None
    operasyon_no: Optional[Integer] = None
    teknik_resim_no: Optional[String] = None
    tezgah_grup_no: Optional[Integer] = None
    net_sure: Optional[Integer] = None
    aciklama: Optional[String] = None
    alt_recete_id: Optional[Integer] = None
    parent_id: Optional[Integer] = None
    malzeme_no: Optional[Integer] = None
    stok_kodu: Optional[String] = None
    yari_mamul: Optional[Integer] = None
    miktar: Optional[Integer] = None
    boy: Optional[Integer] = None
    en: Optional[Integer] = None
    cap: Optional[Integer] = None
    birimi: Optional[String] = None
    temin_sekli: Optional[String] = None
    temp_id: Optional[Integer] = None
    temp_parent: Optional[Integer] = None
    master_operasyon_no: Optional[Integer] = None
    bilesen: Optional[Float] = None
    master_id: Optional[Integer] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class ReceteDetayCreate(ReceteDetayBase):
    pass

class ReceteDetay(ReceteDetayBase):
    id: Optional[int]

    class Config:
        orm_mode = True