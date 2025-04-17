from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Aktarma(Base):
    __tablename__ = 'aktarma'

    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    ktlg_tr_tanimi: Mapped[Optional[String]] = mapped_column(String)
    ktg_en_tanimi: Mapped[Optional[String]] = mapped_column(String)
    metaryal_1: Mapped[Optional[String]] = mapped_column(String)
    metaryal_2: Mapped[Optional[String]] = mapped_column(String)
    standart_1: Mapped[Optional[String]] = mapped_column(String)
    standart_2: Mapped[Optional[String]] = mapped_column(String)
    tr_olcu: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[String]] = mapped_column(String)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    koli: Mapped[Optional[String]] = mapped_column(String)
    uts_onay: Mapped[Optional[String]] = mapped_column(String)
    mo_malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    uts_mataryal: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)