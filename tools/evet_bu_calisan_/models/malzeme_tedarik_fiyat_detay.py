from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeTedarikFiyatDetay(Base):
    __tablename__ = 'malzeme_tedarik_fiyat_detay'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    mlz_ted_fiyat_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    birim_fiyati: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    para_birimi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    kts: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)