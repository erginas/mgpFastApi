from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SevkiyatLog(Base):
    __tablename__ = 'sevkiyat_log'

    sip_yil: Mapped[Optional[Integer]] = mapped_column(Integer)
    sip_ay: Mapped[Optional[Integer]] = mapped_column(Integer)
    sip_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    sevk_yil: Mapped[Optional[Integer]] = mapped_column(Integer)
    sevk_ay: Mapped[Optional[Integer]] = mapped_column(Integer)
    sevk_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    kk: Mapped[Optional[Integer]] = mapped_column(Integer)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    sql: Mapped[Optional[String]] = mapped_column(String)
    kts: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)