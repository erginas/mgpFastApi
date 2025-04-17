from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HaberlerMakale(Base):
    __tablename__ = 'haberler_makale'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yazar: Mapped[Optional[String]] = mapped_column(String)
    baslik: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    metin: Mapped[Optional[String]] = mapped_column(String)
    sehir: Mapped[Optional[String]] = mapped_column(String)
    yayinlanma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    aktif: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yaratilma_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    guncelleme_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)