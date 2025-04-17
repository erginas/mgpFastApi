from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GeciciStok(Base):
    __tablename__ = 'gecici_stok'

    giris_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    kontrol_eden: Mapped[Optional[Float]] = mapped_column(Float)
    teslim_alan: Mapped[Optional[Float]] = mapped_column(Float)
    teslim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    irsaliye_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    alma_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kontrol_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    hareket_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    sertifika_ref_no: Mapped[Optional[Float]] = mapped_column(Float)
    referans_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    depo: Mapped[Optional['Depo']] = relationship(back_populates='gecici_stok')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='gecici_stok')
    firma: Mapped[Optional['Firma']] = relationship(back_populates='gecici_stok')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='gecici_stok')
    hareket_sebebi: Mapped[Optional['HareketSebebi']] = relationship(back_populates='gecici_stok')