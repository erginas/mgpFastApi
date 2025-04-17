from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AlinanSiparisSevkiyati(Base):
    __tablename__ = 'alinan_siparis_sevkiyati'

    sevk_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sevk_ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sevk_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    fiili_teslim_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    teslim_saati: Mapped[Optional[String]] = mapped_column(String)
    gidis_sekli: Mapped[Optional[String]] = mapped_column(String)
    tasiyici_firma: Mapped[Optional[String]] = mapped_column(String)
    tasiyici_firma_referansi: Mapped[Optional[String]] = mapped_column(String)
    irsaliye_no: Mapped[Optional[String]] = mapped_column(String)
    fatura_no: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    firma_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    birim_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    irs_fat_fl: Mapped[Optional[Integer]] = mapped_column(Integer)
    hareket_kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    otomatik_fl: Mapped[Optional[Integer]] = mapped_column(Integer)
    iade_no: Mapped[Optional[String]] = mapped_column(String)
    beyanname_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='alinan_siparis_sevkiyati')
    firma: Mapped[Optional['Firma']] = relationship(back_populates='alinan_siparis_sevkiyati')
    organizasyon_birimi: Mapped[Optional['OrganizasyonBirimi']] = relationship(
        back_populates='alinan_siparis_sevkiyati')
