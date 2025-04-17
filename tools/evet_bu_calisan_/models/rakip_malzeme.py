from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RakipMalzeme(Base):
    __tablename__ = 'rakip_malzeme'

    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_kodu: Mapped[Optional[String]] = mapped_column(String)
    malzeme_adi: Mapped[Optional[String]] = mapped_column(String)
    marka: Mapped[Optional[String]] = mapped_column(String)
    firma_adi: Mapped[Optional[String]] = mapped_column(String)
    turu: Mapped[Optional[String]] = mapped_column(String)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kombine_urun: Mapped[Optional[String]] = mapped_column(String)
    doviz1: Mapped[Optional[Float]] = mapped_column(Float)
    dovizcinsi1: Mapped[Optional[String]] = mapped_column(String)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)