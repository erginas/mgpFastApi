from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KesinlesenTerminTakibi(Base):
    __tablename__ = 'kesinlesen_termin_takibi'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    siparis_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kesinlesen_termin: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    musteri_termini: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis: Mapped[Optional['AlinanSiparis']] = relationship(back_populates='kesinlesen_termin_takibi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='kesinlesen_termin_takibi')