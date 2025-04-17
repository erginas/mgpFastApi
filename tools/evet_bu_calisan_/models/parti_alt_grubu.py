from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PartiAltGrubu(Base):
    __tablename__ = 'parti_alt_grubu'

    refakat_no: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    isemri_no: Mapped[Optional[String]] = mapped_column(String)
    miktar: Mapped[Optional[Float]] = mapped_column(Float)
    nedeni: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    is_emri: Mapped[Optional['IsEmri']] = relationship(back_populates='parti_alt_grubu')