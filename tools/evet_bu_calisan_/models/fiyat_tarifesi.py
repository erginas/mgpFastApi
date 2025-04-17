from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FiyatTarifesi(Base):
    __tablename__ = 'fiyat_tarifesi'

    tarife_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    urun_grup_no: Mapped[Optional[Float]] = mapped_column(Float)
    bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    yayinlandi_fl: Mapped[Optional[String]] = mapped_column(String)
    baslangic_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)