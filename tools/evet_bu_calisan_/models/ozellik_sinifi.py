from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OzellikSinifi(Base):
    __tablename__ = 'ozellik_sinifi'

    ozellik_sinif_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    secenek_sabit_fl: Mapped[Optional[String]] = mapped_column(String)
    stok_kod_uzunlugu: Mapped[Optional[Integer]] = mapped_column(Integer)
    eski_kod: Mapped[Optional[String]] = mapped_column(String)
    gezgin_sirasi: Mapped[Optional[Float]] = mapped_column(Float)
    siniflandirma_bitti: Mapped[Optional[String]] = mapped_column(String)
    siniflandirma_kodlu: Mapped[Optional[String]] = mapped_column(String)
    otomatik_aktar: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)