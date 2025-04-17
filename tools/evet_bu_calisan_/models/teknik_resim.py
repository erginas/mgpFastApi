from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TeknikResim(Base):
    __tablename__ = 'teknik_resim'

    teknik_resim_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    resim_kodu: Mapped[Optional[String]] = mapped_column(String)
    malzeme_adi: Mapped[Optional[String]] = mapped_column(String)
    asama_adi: Mapped[Optional[String]] = mapped_column(String)
    yayinlandigi_tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)