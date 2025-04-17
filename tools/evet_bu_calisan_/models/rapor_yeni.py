from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RaporYeni(Base):
    __tablename__ = 'rapor_yeni'

    id: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    parent_id: Mapped[Optional[Float]] = mapped_column(Float)
    referans_id: Mapped[Optional[Float]] = mapped_column(Float)
    adi: Mapped[Optional[String]] = mapped_column(String, nullable=False)
    turu: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ic_kayit: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    versiyon: Mapped[Optional[Float]] = mapped_column(Float)
    gorunurluk: Mapped[Optional[Float]] = mapped_column(Float)
    kilitli: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    kopya_sayisi: Mapped[Optional[Float]] = mapped_column(Float)
    kagit_boyu: Mapped[Optional[Float]] = mapped_column(Float)
    ust_bosluk: Mapped[Optional[Float]] = mapped_column(Float)
    alt_bosluk: Mapped[Optional[Float]] = mapped_column(Float)
    barkod_yazici_kullan: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    saat_sinirli: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    saatler: Mapped[Optional[String]] = mapped_column(String)
    istatistik_tutma: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    tasarimi_yapan: Mapped[Optional[String]] = mapped_column(String)
    sablon: Mapped[Optional[String]] = mapped_column(String)
    kts: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    dts: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=False)
    kodu: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    rapor_yeni: Mapped[Optional['RaporYeni']] = relationship(back_populates='rapor_yeni')
    rapor_yeni_1: Mapped[Optional['RaporYeni']] = relationship(back_populates='rapor_yeni')