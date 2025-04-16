from sqlalchemy import Column, Integer, String, Numeric, DateTime, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

Base = declarative_base()

class IsEmriOperasyonu(Base):
    __tablename__ = "IS_EMRI_OPERASYONU"

    ISLEM_SIRASI = Column(Integer, primary_key=True)
    OPERASYON_NO = Column(Integer, primary_key=True)
    DURUS_DETAY_KODU = Column(Integer, nullable=True)
    DURUMU = Column(CHAR(1), default='P')
    DURUS_BASLANGIC = Column(DateTime, nullable=True)
    DURUS_BITIS = Column(DateTime, nullable=True)
    ISLEM_BASLANGIC = Column(DateTime, nullable=True)
    ISLEM_BITIS = Column(DateTime, nullable=True)
    ISLEM_SURESI = Column(Numeric(10, 5), nullable=True)
    ISEMRI_NO = Column(String(10), nullable=False)
    MIKTAR_GIREN = Column(Numeric(10, 3), nullable=True)
    MIKTAR_KABUL = Column(Numeric(10, 3), nullable=True)
    MIKTAR_RED = Column(Numeric(10, 3), nullable=True)
    MIKTAR_SARTLI_KABUL = Column(Numeric(10, 3), nullable=True)
    KIMLIK_NO = Column(Numeric(15), nullable=True)
    TEZGAH_NO = Column(String(10), nullable=True)
    ACIKLAMA = Column(String(1024), nullable=True)
    PROSES_RAPOR_NO = Column(String(10), nullable=True)
    MIKTAR_KONTROL = Column(Numeric(10, 3), nullable=True)
    MIKTAR_KAYIT = Column(Numeric(10, 3), nullable=True)
    MIKTAR_CIKAN = Column(Numeric(10, 3), nullable=True)
    MIKTAR_PARCA_RED = Column(Numeric(10, 3), nullable=True)
    RECETE_NO = Column(Integer, nullable=True)
    KAYIT_NO = Column(Integer, nullable=True)
    UYG_YIL = Column(Integer, nullable=True)
    UYG_AY = Column(Integer, nullable=True)
    UYG_RAPOR_NO = Column(Integer, nullable=True)
    SK_PLAN_KODU = Column(Integer, nullable=True)
    FIRMA_KODU = Column(Integer, nullable=True)
    VAKUM_DEGERI = Column(Integer, nullable=True)
    YAPISTIRMA_SURESI = Column(Integer, nullable=True)
    BEKLEME_SURESI = Column(Integer, nullable=True)
    RECETE_DETAY_ID = Column(Integer, nullable=True)
    VAKUM_SURESI = Column(Integer, nullable=True)
    EKLEYEN_KULLANICI_KIMLIK_NO = Column(Integer, nullable=True)
    ENSONGUNCELLEYEN_KULLANICI_KIMLIK_NO = Column(Integer, nullable=True)
    EKLENME_ZAMANI = Column(DateTime, nullable=True)
    ENSON_GUNCELLENME_ZAMANI = Column(DateTime, nullable=True)
    MAC_ADDRESS = Column(String(48), nullable=True)
    GUNCELLEYEN_MAC_ADDRESS = Column(String(48), nullable=True)

# SQLAlchemy modelinden Pydantic modeli oluşturma
IslemSırasıSchema = sqlalchemy_to_pydantic(IsEmriOperasyonu)

# İsteğe bağlı olarak, sadece belirli alanları dahil etmek için:
IslemSırasıCreateSchema = sqlalchemy_to_pydantic(
    IsEmriOperasyonu,
    exclude=["EKLENME_ZAMANI", "ENSON_GUNCELLENME_ZAMANI"]
)