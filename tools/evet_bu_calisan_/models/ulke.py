from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Ulke(Base):
    __tablename__ = 'ulke'

    kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    iso_kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    tr_adi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    en_adi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)