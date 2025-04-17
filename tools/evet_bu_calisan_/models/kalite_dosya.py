from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class KaliteDosya(Base):
    __tablename__ = 'kalite_dosya'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    dosya_no: Mapped[Optional[String]] = mapped_column(String)
    dosya_adi: Mapped[Optional[String]] = mapped_column(String)
    icerik: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)