from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TakipliKonuAsamasi(Base):
    __tablename__ = 'takipli_konu_asamasi'

    takip_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    takip_ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    takip_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    cesidi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    cozum_fl: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='takipli_konu_asamasi')
    takipli_konu: Mapped[Optional['TakipliKonu']] = relationship(back_populates='takipli_konu_asamasi')