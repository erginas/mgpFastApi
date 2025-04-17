from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Uygunsuzluk(Base):
    __tablename__ = 'uygunsuzluk'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    rapor_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    fonksiyon: Mapped[Optional[String]] = mapped_column(String)
    tespit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tespit_yeri: Mapped[Optional[String]] = mapped_column(String)
    konu: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    eski_rapor_no: Mapped[Optional[String]] = mapped_column(String)
    kapandi_fl: Mapped[Optional[String]] = mapped_column(String)
    kapandi_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    etiket_fl: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='uygunsuzluk')
    firma: Mapped[Optional['Firma']] = relationship(back_populates='uygunsuzluk')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='uygunsuzluk')