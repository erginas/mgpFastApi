from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PerformansVerisi(Base):
    __tablename__ = 'performans_verisi'

    malzeme_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    veri_no: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    tipi: Mapped[Optional[String]] = mapped_column(String)
    a_degeri: Mapped[Optional[Float]] = mapped_column(Float)
    b_degeri: Mapped[Optional[Float]] = mapped_column(Float)
    umin: Mapped[Optional[Float]] = mapped_column(Float)
    umax: Mapped[Optional[Float]] = mapped_column(Float)
    devir: Mapped[Optional[Float]] = mapped_column(Float)
    aciklama: Mapped[Optional[String]] = mapped_column(String)
    ek_bilgi: Mapped[Optional[String]] = mapped_column(String)
    nokta: Mapped[Optional[String]] = mapped_column(String)
    katsayi: Mapped[Optional[String]] = mapped_column(String)
    musteri: Mapped[Optional[String]] = mapped_column(String)
    siparis_ref_no: Mapped[Optional[String]] = mapped_column(String)
    debi: Mapped[Optional[Float]] = mapped_column(Float)
    basinc: Mapped[Optional[Float]] = mapped_column(Float)
    test_sicakligi: Mapped[Optional[Float]] = mapped_column(Float)
    olcum_capi: Mapped[Optional[Float]] = mapped_column(Float)
    rakim: Mapped[Optional[Float]] = mapped_column(Float)
    motor_markasi: Mapped[Optional[String]] = mapped_column(String)
    motor_verimi: Mapped[Optional[Float]] = mapped_column(Float)
    motor_devri: Mapped[Optional[Float]] = mapped_column(Float)
    etiket_cos_fi: Mapped[Optional[Float]] = mapped_column(Float)
    test_tarihi: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    etiket_verimi: Mapped[Optional[Float]] = mapped_column(Float)
    etiket_akimi: Mapped[Optional[Float]] = mapped_column(Float)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    mac_address: Mapped[Optional[String]] = mapped_column(String)
    guncelleyen_mac_address: Mapped[Optional[String]] = mapped_column(String)
    malzeme: Mapped[Optional['Malzeme']] = relationship(back_populates='performans_verisi')