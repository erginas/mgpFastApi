from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Kullanici(Base):
    __tablename__ = 'kullanici'

    kullanici_kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    sifre_eski: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='kullanici')