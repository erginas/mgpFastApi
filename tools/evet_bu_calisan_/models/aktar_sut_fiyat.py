from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AktarSutFiyat(Base):
    __tablename__ = 'aktar_sut_fiyat'

    sut_kodu: Mapped[Optional[String]] = mapped_column(String)
    fiyat: Mapped[Optional[Integer]] = mapped_column(Integer)
    iskonto: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    ean: Mapped[Optional[String]] = mapped_column(String)
    gecerlik_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    astip_fiyat: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)