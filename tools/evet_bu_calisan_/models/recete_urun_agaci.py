from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ReceteUrunAgaci(Base):
    __tablename__ = 'recete_urun_agaci'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    recete_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    recete_detay_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    adi: Mapped[Optional[String]] = mapped_column(String)
    stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    opsn: Mapped[Optional[String]] = mapped_column(String)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    miktar: Mapped[Optional[Float]] = mapped_column(Float)
    birim: Mapped[Optional[String]] = mapped_column(String)
    boy: Mapped[Optional[Float]] = mapped_column(Float)
    en: Mapped[Optional[Float]] = mapped_column(Float)
    cap: Mapped[Optional[Float]] = mapped_column(Float)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)