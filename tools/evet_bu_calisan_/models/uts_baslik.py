from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UtsBaslik(Base):
    __tablename__ = 'uts_baslik'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    veri_yolu: Mapped[Optional[String]] = mapped_column(String)
    bildirim_tipi: Mapped[Optional[String]] = mapped_column(String)
    iptal_fl: Mapped[Optional[Integer]] = mapped_column(Integer)
    kodu: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)