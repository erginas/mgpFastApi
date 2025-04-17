from pydantic import BaseModel
from typing import Optional

class DovizKuruBase(BaseModel):
    gecerlilik_tarihi: Optional[DateTime] = None
    para_birimi: Optional[String] = None
    temel_para_birimi: Optional[String] = None
    kayit_zamani: Optional[DateTime] = None
    kur: Optional[Float] = None
    doviz_alis: Optional[Float] = None
    doviz_satis: Optional[Float] = None
    efektif_alis: Optional[Float] = None
    efektif_satis: Optional[Float] = None
    katsayi: Optional[Float] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None

class DovizKuruCreate(DovizKuruBase):
    pass

class DovizKuru(DovizKuruBase):
    id: Optional[int]

    class Config:
        orm_mode = True