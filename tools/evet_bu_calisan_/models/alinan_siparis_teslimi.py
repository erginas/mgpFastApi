from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlinanSiparisTeslimi(Base):
    __tablename__ = 'alinan_siparis_teslimi'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    siparis_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    teslim_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    fiili_teslim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    teslim_saati: Mapped[Optional[String]] = mapped_column(String)
    gidis_sekli: Mapped[Optional[String]] = mapped_column(String)
    tasiyici_firma: Mapped[Optional[String]] = mapped_column(String)
    tasiyici_firma_ref: Mapped[Optional[String]] = mapped_column(String)
    sevk_irsaliyesi: Mapped[Optional[String]] = mapped_column(String)
    fatura_no: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis: Mapped[Optional['AlinanSiparis']] = relationship(back_populates='alinan_siparis_teslimi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='alinan_siparis_teslimi')
