from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class VeriDuzeltmeDetayi(Base):
    __tablename__ = 'veri_duzeltme_detayi'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    veri_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tablo: Mapped[Optional[String]] = mapped_column(String)
    saha: Mapped[Optional[String]] = mapped_column(String)
    gorunen_adi: Mapped[Optional[String]] = mapped_column(String)
    eski_deger: Mapped[Optional[String]] = mapped_column(String)
    yeni_deger: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    veri_duzeltme_talebi: Mapped[Optional['VeriDuzeltmeTalebi']] = relationship(back_populates='veri_duzeltme_detayi')