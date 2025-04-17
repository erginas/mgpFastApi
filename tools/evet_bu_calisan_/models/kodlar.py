from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Kodlar(Base):
    __tablename__ = 'kodlar'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    turu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    kodu: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    aktif: Mapped[Optional[Integer]] = mapped_column(Integer)
    sira: Mapped[Optional[Integer]] = mapped_column(Integer)
    grup_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)