from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Performans(Base):
    __tablename__ = 'performans'

    performans_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    performans_ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    performans_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    tipi: Mapped[Optional[String]] = mapped_column(String)
    degerlendirme_puani: Mapped[Optional[Float]] = mapped_column(Float)
    olumlu_fl: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='performans')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='performans')
    kisi_1_2: Mapped[Optional['Kisi']] = relationship(back_populates='performans')