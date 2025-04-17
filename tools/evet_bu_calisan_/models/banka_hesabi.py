from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BankaHesabi(Base):
    __tablename__ = 'banka_hesabi'

    banka_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    hesap_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    hesap_no: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    acilis_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kapanis_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iban_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    banka: Mapped[Optional['Banka']] = relationship(back_populates='banka_hesabi')
