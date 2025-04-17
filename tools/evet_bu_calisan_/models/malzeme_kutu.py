from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeKutu(Base):
    __tablename__ = 'malzeme_kutu'

    id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    en: Mapped[Optional[String]] = mapped_column(String)
    yukseklik: Mapped[Optional[String]] = mapped_column(String)
    boy: Mapped[Optional[String]] = mapped_column(String)
    tip: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)