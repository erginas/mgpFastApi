from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Tanim(Base):
    __tablename__ = 'tanim'

    ean_kodu: Mapped[Optional[String]] = mapped_column(String)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    en_tanim: Mapped[Optional[String]] = mapped_column(String)
    tr_tanim: Mapped[Optional[String]] = mapped_column(String)
    standart_1: Mapped[Optional[String]] = mapped_column(String)
    materyal_1: Mapped[Optional[String]] = mapped_column(String)
    standart_2: Mapped[Optional[String]] = mapped_column(String)
    materyal_2: Mapped[Optional[String]] = mapped_column(String)
    standart_3: Mapped[Optional[String]] = mapped_column(String)
    materyal_3: Mapped[Optional[String]] = mapped_column(String)
    kaplama: Mapped[Optional[String]] = mapped_column(String)
    olcu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)