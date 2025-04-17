from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Toplanti(Base):
    __tablename__ = 'toplanti'

    toplanti_yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    toplanti_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    konu: Mapped[Optional[String]] = mapped_column(String)
    yeri: Mapped[Optional[String]] = mapped_column(String)
    baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kimlik_no: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    kayit_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    goster_fl: Mapped[Optional[String]] = mapped_column(String)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    toplanti_cagrisi: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='toplanti')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='toplanti')