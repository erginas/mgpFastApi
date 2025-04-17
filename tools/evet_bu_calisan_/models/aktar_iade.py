from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AktarIade(Base):
    __tablename__ = 'aktar_iade'

    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    lot_no: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Integer]] = mapped_column(Integer)
    skt: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ozel_olcu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)