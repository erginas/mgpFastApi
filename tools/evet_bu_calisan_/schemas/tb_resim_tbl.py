from pydantic import BaseModel
from typing import Optional

class TbResimTblBase(BaseModel):
    resim_grubu: Optional[String] = None
    sira_no: Optional[String] = None
    asama_adi: Optional[String] = None
    kod: Optional[String] = None
    tanim: Optional[String] = None
    uretim: Optional[String] = None
    proses: Optional[String] = None
    son_kk: Optional[String] = None
    giris_kk: Optional[String] = None
    teknik_dosya: Optional[String] = None
    cnc: Optional[String] = None
    diger: Optional[String] = None
    markalama: Optional[String] = None
    aciklama: Optional[String] = None
    goruntu_no: Optional[Float] = None
    yk_resim: Optional[String] = None
    dagitim_1: Optional[String] = None
    dagitim_2: Optional[String] = None
    dagitim_3: Optional[String] = None
    dagitim_4: Optional[String] = None
    dagitim_5: Optional[String] = None
    dagitim_6: Optional[String] = None
    dagitim_7: Optional[String] = None
    revizyon_1: Optional[String] = None
    revizyon_2: Optional[String] = None
    revizyon_3: Optional[String] = None
    revizyon_4: Optional[String] = None
    revizyon_5: Optional[String] = None
    revizyon_6: Optional[String] = None
    revizyon_7: Optional[String] = None
    tedarikci1: Optional[String] = None
    tedarikci2: Optional[String] = None
    tedarikci3: Optional[String] = None
    tedarikci4: Optional[String] = None
    tedarikci5: Optional[String] = None
    kritik_olcu: Optional[String] = None
    tb__sira_no: Optional[String] = None
    tb__resim_grubu: Optional[String] = None
    firma_kodu: Optional[Integer] = None
    bilgiler_tam: Optional[String] = None
    dis_tic: Optional[String] = None
    elektronik: Optional[String] = None
    ekleyen_kullanici_kimlik_no: Optional[String] = None
    ensonguncelleyen_kullanici_kimlik_no: Optional[String] = None
    eklenme_zamani: Optional[DateTime] = None
    enson_guncellenme_zamani: Optional[DateTime] = None
    mac_address: Optional[String] = None
    guncelleyen_mac_address: Optional[String] = None

class TbResimTblCreate(TbResimTblBase):
    pass

class TbResimTbl(TbResimTblBase):
    id: Optional[int]

    class Config:
        orm_mode = True