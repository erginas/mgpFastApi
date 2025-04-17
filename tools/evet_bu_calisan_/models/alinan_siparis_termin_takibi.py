from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlinanSiparisTerminTakibi(Base):
    __tablename__ = 'alinan_siparis_termin_takibi'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    siparis_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    termin_tipi: Mapped[Optional[String]] = mapped_column(String)
    termin_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    is_gunu: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    iptal_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    tolerans: Mapped[Optional[String]] = mapped_column(String)
    gun_opsiyonu: Mapped[Optional[Float]] = mapped_column(Float)
    gonderilme_z: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis: Mapped[Optional['AlinanSiparis']] = relationship(back_populates='alinan_siparis_termin_takibi')
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='alinan_siparis_termin_takibi')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='alinan_siparis_termin_takibi')
