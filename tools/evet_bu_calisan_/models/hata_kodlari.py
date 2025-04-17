from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class HataKodlari(Base):
    __tablename__ = 'hata_kodlari'

    hata_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    bagimli_hata_no: Mapped[Optional[Float]] = mapped_column(Float)
    kodu: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    hata_kodlari: Mapped[Optional['HataKodlari']] = relationship(back_populates='hata_kodlari')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='hata_kodlari')