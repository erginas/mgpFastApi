from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DegerlendirmeTablosu(Base):
    __tablename__ = 'degerlendirme_tablosu'

    gun_sayisi: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    oncelik_a: Mapped[Optional[Integer]] = mapped_column(Integer)
    oncelik_b: Mapped[Optional[Integer]] = mapped_column(Integer)
    oncelik_c: Mapped[Optional[Integer]] = mapped_column(Integer)
    oncelik_d: Mapped[Optional[Integer]] = mapped_column(Integer)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)