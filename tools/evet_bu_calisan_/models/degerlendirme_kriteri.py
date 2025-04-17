from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DegerlendirmeKriteri(Base):
    __tablename__ = 'degerlendirme_kriteri'

    kriter_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    dusuk_puani: Mapped[Optional[Float]] = mapped_column(Float)
    yuksek_puani: Mapped[Optional[Float]] = mapped_column(Float)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    yayin_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='degerlendirme_kriteri')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='degerlendirme_kriteri')