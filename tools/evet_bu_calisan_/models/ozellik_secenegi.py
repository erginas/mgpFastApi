from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OzellikSecenegi(Base):
    __tablename__ = 'ozellik_secenegi'

    ozellik_sinif_kodu: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    secenek_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    adi: Mapped[Optional[String]] = mapped_column(String)
    tanim_parcasi: Mapped[Optional[String]] = mapped_column(String)
    stok_kodu_parcasi: Mapped[Optional[String]] = mapped_column(String)
    ust_secenek: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ozellik_sinifi: Mapped[Optional['OzellikSinifi']] = relationship(back_populates='ozellik_secenegi')
    ozellik_secenegi: Mapped[Optional['OzellikSecenegi']] = relationship(back_populates='ozellik_secenegi')