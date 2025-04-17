from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KisiYetkinligi(Base):
    __tablename__ = 'kisi_yetkinligi'

    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    yetkinlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    seviye: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    yetkinlik: Mapped[Optional['Yetkinlik']] = relationship(back_populates='kisi_yetkinligi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='kisi_yetkinligi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='kisi_yetkinligi')