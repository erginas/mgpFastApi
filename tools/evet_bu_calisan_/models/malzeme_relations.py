from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeRelations(Base):
    __tablename__ = 'malzeme_relations'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    grup_adi: Mapped[Optional[String]] = mapped_column(String)
    temel_stok_kodu: Mapped[Optional[String]] = mapped_column(String)
    tipi: Mapped[Optional[String]] = mapped_column(String)
    pasif: Mapped[Optional[Float]] = mapped_column(Float)
    ortak_grup: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)