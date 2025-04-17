from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HammaddeSertifikaReferansi(Base):
    __tablename__ = 'hammadde_sertifika_referansi'

    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    hareket_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sertifika_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='hammadde_sertifika_referansi')
    hammadde_sertifikasi: Mapped[Optional['HammaddeSertifikasi']] = relationship(back_populates='hammadde_sertifika_referansi')
    malzeme_hareketi: Mapped[Optional['MalzemeHareketi']] = relationship(back_populates='hammadde_sertifika_referansi')