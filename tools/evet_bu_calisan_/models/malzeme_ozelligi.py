from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MalzemeOzelligi(Base):
    __tablename__ = 'malzeme_ozelligi'

    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ozellik_sinif_kodu: Mapped[Optional[Float]] = mapped_column(Float)
    ozellik: Mapped[Optional[String]] = mapped_column(String)
    secenek_no: Mapped[Optional[Float]] = mapped_column(Float)
    etiket_sirasi: Mapped[Optional[Float]] = mapped_column(Float)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='malzeme_ozelligi')
    ozellik_secenegi: Mapped[Optional['OzellikSecenegi']] = relationship(back_populates='malzeme_ozelligi')
    ozellik_sinifi: Mapped[Optional['OzellikSinifi']] = relationship(back_populates='malzeme_ozelligi')