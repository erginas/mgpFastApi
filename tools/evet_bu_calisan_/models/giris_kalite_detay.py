from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GirisKaliteDetay(Base):
    __tablename__ = 'giris_kalite_detay'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    giris_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kayit_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    miktar_kontrol: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_numune: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_kabul: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_sartli: Mapped[Optional[Float]] = mapped_column(Float)
    miktar_red: Mapped[Optional[Float]] = mapped_column(Float)
    uygunsuzluk_raporu: Mapped[Optional[Float]] = mapped_column(Float)
    depo_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    hareket_no: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    gecici_stok: Mapped[Optional['GeciciStok']] = relationship(back_populates='giris_kalite_detay')
    malzeme_hareketi: Mapped[Optional['MalzemeHareketi']] = relationship(back_populates='giris_kalite_detay')