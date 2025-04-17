from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Parametre(Base):
    __tablename__ = 'parametre'

    parametre: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kullanici_kodu: Mapped[Optional[String]] = mapped_column(String)
    deger: Mapped[Optional[String]] = mapped_column(String)
    blg_sira_no: Mapped[Optional[String]] = mapped_column(String)
    property: Mapped[Optional[String]] = mapped_column(String)
    opsiyon: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='parametre')
    kullanici: Mapped[Optional['Kullanici']] = relationship(back_populates='parametre')
    bilgisayar: Mapped[Optional['Bilgisayar']] = relationship(back_populates='parametre')