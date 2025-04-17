from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FazlaMesai(Base):
    __tablename__ = 'fazla_mesai'

    mesai_kalan: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    yil: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    ay: Mapped[Optional[Float]] = mapped_column(Float, nullable=False)
    sira_no: Mapped[Optional[Integer]] = mapped_column(Integer, nullable=False)
    duzenleyen: Mapped[Optional[Float]] = mapped_column(Float)
    onaylayan: Mapped[Optional[Float]] = mapped_column(Float)
    duzenlenme_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    istenen_baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    istenen_bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    istenen_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    sure_tipi: Mapped[Optional[String]] = mapped_column(String)
    neden: Mapped[Optional[String]] = mapped_column(String)
    iptal_eden: Mapped[Optional[Float]] = mapped_column(Float)
    iptal_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    iptal_nedeni: Mapped[Optional[String]] = mapped_column(String)
    kontrol_eden: Mapped[Optional[Float]] = mapped_column(Float)
    kontrol_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiili_baslama_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiili_bitis_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    fiili_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    durumu: Mapped[Optional[String]] = mapped_column(String)
    onay_t: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    acil_siparis_fl: Mapped[Optional[String]] = mapped_column(String)
    mesai_nedeni: Mapped[Optional[String]] = mapped_column(String)
    birimi: Mapped[Optional[String]] = mapped_column(String)
    dusulen_sure: Mapped[Optional[Integer]] = mapped_column(Integer)
    ekleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    ensonguncelleyen_kullanici_kimlik_no: Mapped[Optional[String]] = mapped_column(String)
    eklenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    enson_guncellenme_zamani: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    kisi: Mapped[Optional['Kisi']] = relationship(back_populates='fazla_mesai')
    kisi_1: Mapped[Optional['Kisi']] = relationship(back_populates='fazla_mesai')
    kisi_1_2: Mapped[Optional['Kisi']] = relationship(back_populates='fazla_mesai')
    kisi_1_2_3: Mapped[Optional['Kisi']] = relationship(back_populates='fazla_mesai')
    kisi_1_2_3_4: Mapped[Optional['Kisi']] = relationship(back_populates='fazla_mesai')