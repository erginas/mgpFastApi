from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ArizaKaydi(Base):
    __tablename__ = 'ariza_kaydi'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    tarih: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tezgah_no: Mapped[Optional[String]] = mapped_column(String)
    ariza_turu: Mapped[Optional[String]] = mapped_column(String)
    ariza_nedeni: Mapped[Optional[String]] = mapped_column(String)
    yapilan_islem: Mapped[Optional[String]] = mapped_column(String)
    baslama_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bitis_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kaydi_acan: Mapped[Optional[Integer]] = mapped_column(Integer)
    tamiri_yapan: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
