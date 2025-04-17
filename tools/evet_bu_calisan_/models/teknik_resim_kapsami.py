from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TeknikResimKapsami(Base):
    __tablename__ = 'teknik_resim_kapsami'

    teknik_resim_kapsam_id: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer)
    teknik_resim_id: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='teknik_resim_kapsami')
    teknik_resim: Mapped[Optional['TeknikResim']] = relationship(back_populates='teknik_resim_kapsami')