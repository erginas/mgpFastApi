from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ParaBirimiDetay(Base):
    __tablename__ = 'para_birimi_detay'

    id: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    alis: Mapped[Optional[Float]] = mapped_column(Float)
    satis: Mapped[Optional[Float]] = mapped_column(Float)
    forex_alis: Mapped[Optional[Float]] = mapped_column(Float)
    forex_satis: Mapped[Optional[Float]] = mapped_column(Float)
    para_birimi: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    kur_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    para_birimi: Mapped[Optional['ParaBirimi']] = relationship(back_populates='para_birimi_detay')