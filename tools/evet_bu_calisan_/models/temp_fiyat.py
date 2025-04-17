from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TempFiyat(Base):
    __tablename__ = 'temp_fiyat'

    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    fiyat: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn_0: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn_700: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn_780: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn_800: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn_810: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)