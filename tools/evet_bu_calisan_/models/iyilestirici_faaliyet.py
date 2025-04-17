from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class IyilestiriciFaaliyet(Base):
    __tablename__ = 'iyilestirici_faaliyet'

    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    konu: Mapped[Optional[String]] = mapped_column(String)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='iyilestirici_faaliyet')