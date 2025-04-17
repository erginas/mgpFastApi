from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FirmaSertifikasi(Base):
    __tablename__ = 'firma_sertifikasi'

    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sertifika_no: Mapped[Optional[String]] = mapped_column(String)
    gecerlilik_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    cinsi: Mapped[Optional[String]] = mapped_column(String)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    sinifi: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    firma: Mapped[Optional['Firma']] = relationship(back_populates='firma_sertifikasi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='firma_sertifikasi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='firma_sertifikasi')