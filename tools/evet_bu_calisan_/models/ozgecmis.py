from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Ozgecmis(Base):
    __tablename__ = 'ozgecmis'

    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kaydeden: Mapped[Optional[Float]] = mapped_column(Float)
    turu: Mapped[Optional[String]] = mapped_column(String)
    bilgi: Mapped[Optional[String]] = mapped_column(String)
    baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='ozgecmis')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='ozgecmis')