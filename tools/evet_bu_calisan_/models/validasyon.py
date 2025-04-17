from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Validasyon(Base):
    __tablename__ = 'validasyon'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yayin_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    modul_versiyon: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    degisiklik_tipi: Mapped[Optional[Float]] = mapped_column(Float)
    modul_id: Mapped[Optional[Float]] = mapped_column(Float)
    yayinlandi: Mapped[Optional[Float]] = mapped_column(Float)
    yayinlayan: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kodlar: Mapped[Optional['Kodlar']] = relationship(back_populates='validasyon')
    modul: Mapped[Optional['Modul']] = relationship(back_populates='validasyon')
    kodlar_1: Mapped[Optional['Kodlar']] = relationship(back_populates='validasyon')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='validasyon')