from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeTeminYeri(Base):
    __tablename__ = 'malzeme_temin_yeri'

    temin_sekil_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sertifika_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    tedarikci_kodu: Mapped[Optional[String]] = mapped_column(String)
    tahmini_temin_suresi: Mapped[Optional[Float]] = mapped_column(Float)
    min_temin_miktari: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    oncelik: Mapped[Optional[Float]] = mapped_column(Float)
    marka: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    eko_temin_miktari: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme_temin_sekli: Mapped[Optional['MalzemeTeminSekli']] = relationship(back_populates='malzeme_temin_yeri')
    firma: Mapped[Optional['Firma']] = relationship(back_populates='malzeme_temin_yeri')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='malzeme_temin_yeri')
    firma_sertifikasi: Mapped[Optional['FirmaSertifikasi']] = relationship(back_populates='malzeme_temin_yeri')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='malzeme_temin_yeri')