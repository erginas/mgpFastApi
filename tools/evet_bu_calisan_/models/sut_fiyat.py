from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SutFiyat(Base):
    __tablename__ = 'sut_fiyat'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    gecerlik_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    sut_kodu: Mapped[Optional[String]] = mapped_column(String)
    ean: Mapped[Optional[String]] = mapped_column(String)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    fiyat: Mapped[Optional[Integer]] = mapped_column(Integer)
    iskonto: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    aktif: Mapped[Optional[String]] = mapped_column(String)
    islem_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    s_fiyat_master_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)