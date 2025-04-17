from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Banka(Base):
    __tablename__ = 'banka'

    banka_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    sube_adi: Mapped[Optional[String]] = mapped_column(String)
    eft_kodu: Mapped[Optional[String]] = mapped_column(String)
    swift_kodu: Mapped[Optional[String]] = mapped_column(String)
    il: Mapped[Optional[String]] = mapped_column(String)
    ilce: Mapped[Optional[String]] = mapped_column(String)
    sube_kodu: Mapped[Optional[String]] = mapped_column(String)
    doviz_cinsi: Mapped[Optional[String]] = mapped_column(String)
    hesap_no: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
