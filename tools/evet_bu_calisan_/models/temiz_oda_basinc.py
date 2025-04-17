from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TemizOdaBasinc(Base):
    __tablename__ = 'temiz_oda_basinc'

    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    deger: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kayit_sikligi: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kayit_birim: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    birim: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)