from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rapor(Base):
    __tablename__ = 'rapor'

    rapor_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    rapor_adi: Mapped[Optional[String]] = mapped_column(String)
    icerik: Mapped[Optional[String]] = mapped_column(String)
    id: Mapped[Optional[Integer]] = mapped_column(Integer)
    parent_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    referans_id: Mapped[Optional[Integer]] = mapped_column(Integer)
    turu: Mapped[Optional[Integer]] = mapped_column(Integer)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ic_kayit: Mapped[Optional[Integer]] = mapped_column(Integer)
    versiyon: Mapped[Optional[Integer]] = mapped_column(Integer)
    gorunurluk: Mapped[Optional[Integer]] = mapped_column(Integer)
    kilitli: Mapped[Optional[Integer]] = mapped_column(Integer)
    kopya_sayisi: Mapped[Optional[Integer]] = mapped_column(Integer)
    kagit_boyu: Mapped[Optional[Integer]] = mapped_column(Integer)
    ust_bosluk: Mapped[Optional[Integer]] = mapped_column(Integer)
    alt_bosluk: Mapped[Optional[Integer]] = mapped_column(Integer)
    barkod_yazici_kullan: Mapped[Optional[Integer]] = mapped_column(Integer)
    saat_sinirli: Mapped[Optional[Integer]] = mapped_column(Integer)
    saatler: Mapped[Optional[String]] = mapped_column(String)
    istatistik_tutma: Mapped[Optional[Integer]] = mapped_column(Integer)
    tasarimi_yapan: Mapped[Optional[String]] = mapped_column(String)
    sablon: Mapped[Optional[String]] = mapped_column(String)
    kk: Mapped[Optional[Float]] = mapped_column(Float)
    kts: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    dts: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kodu: Mapped[Optional[String]] = mapped_column(String)
    adi: Mapped[Optional[String]] = mapped_column(String)
    guid: Mapped[Optional[String]] = mapped_column(String)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)