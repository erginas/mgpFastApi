from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class IsEmriOperasyonuBase(BaseModel):
    ISLEM_SIRASI: int
    OPERASYON_NO: int
    ISEMRI_NO: str

    DURUS_DETAY_KODU: Optional[int] = None
    DURUMU: Optional[str] = "P"
    DURUS_BASLANGIC: Optional[datetime] = None
    DURUS_BITIS: Optional[datetime] = None
    ISLEM_BASLANGIC: Optional[datetime] = None
    ISLEM_BITIS: Optional[datetime] = None
    ISLEM_SURESI: Optional[float] = None
    MIKTAR_GIREN: Optional[float] = None
    MIKTAR_KABUL: Optional[float] = None
    MIKTAR_RED: Optional[float] = None
    MIKTAR_SARTLI_KABUL: Optional[float] = None
    KIMLIK_NO: Optional[int] = None
    TEZGAH_NO: Optional[str] = None
    ACIKLAMA: Optional[str] = None
    PROSES_RAPOR_NO: Optional[str] = None
    MIKTAR_KONTROL: Optional[float] = None
    MIKTAR_KAYIT: Optional[float] = None
    MIKTAR_CIKAN: Optional[float] = None
    MIKTAR_PARCA_RED: Optional[float] = None
    RECETE_NO: Optional[int] = None
    KAYIT_NO: Optional[int] = None
    UYG_YIL: Optional[int] = None
    UYG_AY: Optional[int] = None
    UYG_RAPOR_NO: Optional[int] = None
    SK_PLAN_KODU: Optional[int] = None
    FIRMA_KODU: Optional[int] = None
    VAKUM_DEGERI: Optional[int] = None
    YAPISTIRMA_SURESI: Optional[int] = None
    BEKLEME_SURESI: Optional[int] = None
    RECETE_DETAY_ID: Optional[int] = None
    VAKUM_SURESI: Optional[int] = None
    EKLEYEN_KULLANICI_KIMLIK_NO: Optional[int] = None
    ENSONGUNCELLEYEN_KULLANICI_KIMLIK_NO: Optional[int] = None
    EKLENME_ZAMANI: Optional[datetime] = None
    ENSON_GUNCELLENME_ZAMANI: Optional[datetime] = None
    MAC_ADDRESS: Optional[str] = None
    GUNCELLEYEN_MAC_ADDRESS: Optional[str] = None

class IsEmriOperasyonuCreate(IsEmriOperasyonuBase):
    pass

class IsEmriOperasyonuOut(IsEmriOperasyonuBase):
    class Config:
        from_attributes = True  # ORM nesnelerini desteklemek için