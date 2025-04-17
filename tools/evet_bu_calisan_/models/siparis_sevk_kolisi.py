from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class SiparisSevkKolisi(Base):
    __tablename__ = 'siparis_sevk_kolisi'

    sevk_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sevk_ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sevk_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    koli_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    agirlik: Mapped[Optional[Float]] = mapped_column(Float)
    ebat: Mapped[Optional[String]] = mapped_column(String)
    koli_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    koli_tanim: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    alinan_siparis_sevkiyati: Mapped[Optional['AlinanSiparisSevkiyati']] = relationship(back_populates='siparis_sevk_kolisi')