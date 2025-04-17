from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Recete(Base):
    __tablename__ = 'recete'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    onayli: Mapped[Optional[String]] = mapped_column(String)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)