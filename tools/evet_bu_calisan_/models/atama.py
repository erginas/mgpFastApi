from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Atama(Base):
    __tablename__ = 'atama'

    kadro_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    atayan: Mapped[Optional[Float]] = mapped_column(Float)
    azleden: Mapped[Optional[Float]] = mapped_column(Float)
    atanma_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    azil_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    atama_durumu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kadro: Mapped[Optional['Kadro']] = relationship(back_populates='atama')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='atama')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='atama')
    kisi_1_2: Mapped[Optional['Kisi']] = relationship(back_populates='atama')
