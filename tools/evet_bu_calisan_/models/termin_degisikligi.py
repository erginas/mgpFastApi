from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TerminDegisikligi(Base):
    __tablename__ = 'termin_degisikligi'

    isemri_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    degistirilme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    eski_oncelik: Mapped[Optional[String]] = mapped_column(String)
    eski_teslim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    gerekce: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='termin_degisikligi')
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='termin_degisikligi')