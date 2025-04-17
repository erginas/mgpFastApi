from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AstipDepo(Base):
    __tablename__ = 'astip_depo'

    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    adet: Mapped[Optional[Integer]] = mapped_column(Integer)
    skt: Mapped[Optional[String]] = mapped_column(String)
    iade_no: Mapped[Optional[String]] = mapped_column(String)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    iade_sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
