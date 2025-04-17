from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SutFiyatMaster(Base):
    __tablename__ = 'sut_fiyat_master'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    sut_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ozel_aciklama: Mapped[Optional[String]] = mapped_column(String)
    aktif: Mapped[Optional[Integer]] = mapped_column(Integer)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)