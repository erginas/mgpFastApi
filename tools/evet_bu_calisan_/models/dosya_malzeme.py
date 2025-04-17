from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DosyaMalzeme(Base):
    __tablename__ = 'dosya_malzeme'

    kalite_dosya_id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kalite_dosya: Mapped[Optional['KaliteDosya']] = relationship(back_populates='dosya_malzeme')
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='dosya_malzeme')